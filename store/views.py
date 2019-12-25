import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from . import models

#todo cache this
def frontend_config_js(request):
    configs = [
        "product_image_url_format_pic_small",
        "product_image_url_format_pic_big",
        "product_image_url_format_front_small",
        "product_image_url_format_front_big",
        "product_image_url_prefix",
    ]
    data = {}
    for config in configs:
        data[config] = models.Storesetting.objects.get(name=config).value
    return HttpResponse("frontend_config = "+json.dumps(data))

def products_js(request):
    products = models.Product.objects.filter(enabled=True).order_by("sku")
    product_data = serializers.serialize('json', products)
    return HttpResponse("model_products = "+product_data)


def user_js(request):
    userdata = {}
    if request.user.is_authenticated:
        userdata["login"] = True
        userdata["whatsapp"] = request.user.customer.phone_number
        userdata["cart"] = []
        for prod in request.user.customer.cart.values():
            userdata["cart"].append(
                prod["sku"]
            )
    else:
        userdata["login"] = False
    return HttpResponse("model_user = "+json.dumps(userdata))
    


def home(request):
    return render(request, "store/home.html", {
        
    })
    # return HttpResponse("<html><head><script src='/store/products.js' ></script></head><body></body></html>")
