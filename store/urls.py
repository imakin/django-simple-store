from django.urls import path
from django.conf.urls import url
from store.views import (
    products_js,
    frontend_config_js,
    user_js,
    home
)

urlpatterns = [
    url(r'^store/products.js$', products_js),
    url(r'^store/frontend_config.js$', frontend_config_js),
    url(r'^store/user.js$', user_js),
    url(r'^store/$', home),
    url(r'^store$', home),
]
