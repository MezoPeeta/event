import json
from .models import Products, Order, OrderItem, Customer


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
    except KeyError:
        cart = {}
        print("CART:", cart)

    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    cart_items = order["get_cart_items"]

    for i in cart:
        try:
            cart_items += cart[i]["quantity"]

            product = Products.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[i]["quantity"]

            item = {
                "id": product.id,
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": cart[i]["quantity"],
                "digital": product.digital,
                "get_total": total,
            }
            items.append(item)

            if not product.digital:
                order["shipping"] = True
        except Products.DoesNotExist:
            pass

    return {"cartItems": cart_items, "order": order, "items": items}


def cart_data(request):
    cookie_data = cookie_cart(request)
    cart_items = cookie_data["cartItems"]
    order = cookie_data["order"]
    items = cookie_data["items"]

    return {"cartItems": cart_items, "order": order, "items": items}


def guest_order(request, data):
    name = data["form"]["name"]
    email = data["form"]["email"]

    cookie_data = cookie_cart(request)
    items = cookie_data["items"]

    customer, _ = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Products.objects.get(id=item["id"])
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item["quantity"],
        )
    return customer, order
