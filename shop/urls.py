from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import checkout, home, login, products, sidebar, updateItem, cart, contact

urlpatterns = [
    path('', home, name="home"),
    path('sidebar/', sidebar, name="sidebar"),
    path('prodetail/<str:pk>', products, name="product"),
    path('login/', login, name="login"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('contact/', contact, name="contact"),
    path('update_item/', updateItem, name="update_item"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
