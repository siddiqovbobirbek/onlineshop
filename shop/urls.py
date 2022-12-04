from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('sidebar/', views.sidebar, name="sidebar"),
    path('prodetail/', views.products, name="products"),
    path('login/', views.login, name="login"),
    path('checkout/', views.checkout, name="checkout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
