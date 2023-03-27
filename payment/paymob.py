from accept.payment import *

API_KEY = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnVZVzFsSWpvaWFXNXBkR2xoYkNJc0ltTnNZWE56SWpvaVRXVnlZMmhoYm5RaUxDSndjbTltYVd4bFgzQnJJam8zTWpnMk1UTjkuaUc3bUFJMGs3bW1LMHhwOWhRQ1RyU2VFX194Rl9mRDBtQnVvNmpZUDkwQ2FoZl9oZEk0Qk9NZmNUOW90XzJiblEzX0gwZGdlXzc1empTS1g1ejNfV0E="

accept = AcceptAPI(API_KEY)

auth_token = accept.retrieve_auth_token()

def paymob_iframe(cents:int,quantity:int,is_ticket:bool = False,items:list = []):
    OrderData = {
        "auth_token": auth_token,
        "delivery_needed": "false",
        "amount_cents": str(cents),
        "currency": "EGP",
        "items": items
    }     
    if is_ticket:
        OrderData["items"] = [
        {
            "name": "Ticket",
            "amount_cents": str(cents),
            "description": "Ticket",
            "quantity": str(quantity),
        
        }
        ],

    order = accept.order_registration(OrderData)

    Request = {
        "auth_token": auth_token,
        "amount_cents": str(cents),
        "expiration": 3600,
        "order_id": order.get("id"),
        "billing_data": {
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+86(8)9135210487",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah",
        },
        "currency": "EGP",
        "integration_id": 3692904,
    }
    payment_token = accept.payment_key_request(Request)

    iframeURL = accept.retrieve_iframe(iframe_id="746134", payment_token=payment_token)

    return iframeURL

