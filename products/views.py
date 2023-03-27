from django.shortcuts import render, redirect 
from .models import Products, Order, OrderItem, Customer, ShippingAddress
import datetime
# from django.template.loader import render_to_string
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError
from .utils import get_customer
from payment.paymob import paymob_iframe

class ProductListView(ListView):
    model = Products
    template_name = "products/store.html"
    ordering = ["-created_at"]
    paginate_by = 9

    def get_context_data(self, **kwargs):
        try:
            search_query = self.request.GET["search_query"]
        except MultiValueDictKeyError:
            search_query = False
        if search_query:
            products = Products.objects.filter(name__icontains=search_query).order_by("-id")
        else:
            products = Products.objects.all()
        context = super().get_context_data(**kwargs)
        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get("page")
        try:
            products_list = paginator.page(page)
        except PageNotAnInteger:
            products_list = paginator.page(1)
        except EmptyPage:
            products_list = paginator.page(paginator.num_pages)


        order_count = OrderItem.objects.filter(order__customer=get_customer(self.request), order__complete=False).count()
        context = {
            "Products": products_list,
            "title": "Store",
            "search_query": search_query,
            "order_count": order_count,
        }
        return context


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = "dashboard/PR/new_products.html"
    fields = ["image", "price","name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def products(request, pk):
    product = Products.objects.get(id=pk)
    
    if request.method == "POST":
        product = Products.objects.get(id=pk)
    
        order, _ = Order.objects.get_or_create(customer=get_customer(request), complete=False)
        order_item, _ = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity = request.POST["quantity"]
        order_item.save()

        return redirect("Cart")

    context = {"product": product}
    return render(request, "products/products.html", context)


def cart(request):
    
    order, _ = Order.objects.get_or_create(customer=get_customer(request), complete=False)

    context = {"order": order}

    return render(request, "products/cart.html", context)


def checkout(request):

    order = Order.objects.get(customer=get_customer(request), complete=False)

    transaction_id = datetime.datetime.now().timestamp()

    total = order.get_cart_total

    order_items = order.orderitem_set.all()
    products = Products.objects.filter(orderitem__in=order_items).iterator()
    products_data = [product.__dict__ for product in products]
    total_quantity = sum(order.orderitem_set.all().values_list("quantity", flat=True))

    for product in products_data:
        product["amount_cents"] = str(product["price"] * 100) 
        product["quantity"] = str(OrderItem.objects.get(product=product["id"]).quantity)
        product["description"] = product["name"]
        del product["price"]
        del product["_state"]
        del product["id"]
        del product["image"]
        del product["created_at"]
        del product["user_id"]


    # if request.method == "POST":
    #     order.complete = True
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     address = request.POST["address"]
    #     city = request.POST["city"]
    #     state = request.POST["state"]
    #     zipcode = request.POST["zipcode"]
    #     phone_number = request.POST["phone_number"]

    #     Customer.objects.get(pk=get_customer(request).id).update(email=email,name=name)

    #     order.transaction_id = transaction_id
    #     order.save()
    #     ShippingAddress.objects.create(
    #         customer=get_customer(request),
    #         order=order,
    #         address=address,
    #         phone_number=phone_number,
    #         city=city,
    #         state=state,
    #         zipcode=zipcode,
    #     )


        # SEND EMAIIIl
        # order_product = OrderItem.objects.get(order=order).product
        # order_quantity = OrderItem.objects.get(order=order).quantity
        # product_name = order_product.name
        # product_image = order_product.image
        # order_price = order_product.price
        # order_date = order.date_ordered
        # current_time = datetime.datetime.now()
        # subject = "Purchase Confirmation"
        # message = render_to_string(
        #     "products/purchase.html",
        #     {
        #         "name": name,
        #         "total": total,
        #         "quantity": order_quantity,
        #         "product_name": product_name,
        #         "order_price": order_price,
        #         "product_image": product_image,
        #         "order_date": order_date,
        #     },
        # )
        # confirmation_purchase = EmailMessage(subject , message , to=[email])
        # confirmation_purchase.content_subtype = 'html'
        # confirmation_purchase.send()

        # return redirect("Store")

    
    context = {
        "total": total,
        "iframe" : paymob_iframe(cents=total*100,
                                 quantity=total_quantity,
                                 items=products_data,
                                 ),
    }
    return render(request, "products/checkout.html", context)


def delete(request, pk):
    order = OrderItem.objects.get(pk=pk)
    order.delete()
        
    return redirect("Cart")

