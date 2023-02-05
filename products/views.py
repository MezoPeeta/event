from django.shortcuts import render, redirect
from .models import Products, Order, OrderItem, Customer, ShippingAddress
import datetime
# from django.template.loader import render_to_string
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError


def store(request):
    products = Products.objects.all()
    context = {
        "Products": products,
        "title": "Store",
    }
    return render(request, "products/store.html", context)


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
        context = {
            "Products": products_list,
            "title": "Store",
            "search_query": search_query,
        }
        return context


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = "dashboard/PR/new_products.html"
    fields = ["image", "price"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def products(request, pk):
    product = Products.objects.get(id=pk)

    if request.method == "POST":
        product = Products.objects.get(id=pk)
        try:
            customer = request.user.customer
        except (Customer.DoesNotExist, AttributeError):
            device = request.COOKIES["device"]
            customer, _ = Customer.objects.get_or_create(device=device)
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, _ = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity = request.POST["quantity"]
        order_item.save()

        return redirect("Cart")

    context = {"product": product}
    return render(request, "products/products.html", context)


def cart(request):
    try:
        customer = request.user.customer
    except AttributeError:
        device = request.COOKIES["device"]
        customer, _ = Customer.objects.get_or_create(device=device)

    order, _ = Order.objects.get_or_create(customer=customer, complete=False)

    context = {"order": order}

    return render(request, "products/cart.html", context)


def checkout(request):
    device = request.COOKIES["device"]

    customer, _ = Customer.objects.get_or_create(device=device)

    order = Order.objects.get(customer=customer, complete=False)

    transaction_id = datetime.datetime.now().timestamp()

    total = order.get_cart_total

    if request.method == "POST":
        order.complete = True
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zipcode = request.POST["zipcode"]
        phone_number = request.POST["phone_number"]

        customer.name = name
        customer.email = email
        customer.save()
        order.transaction_id = transaction_id
        order.save()
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=address,
            phone_number=phone_number,
            city=city,
            state=state,
            zipcode=zipcode,
        )

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

        return redirect("Store")

    return render(request, "products/checkout.html", {"total": total})


def delete(request, pk):
    order = OrderItem.objects.filter(order=pk)
    if request.method == "POST":
        order.delete()

        return redirect("Cart")

    context = {"order": order}

    return render(request, "products/delete.html", context)