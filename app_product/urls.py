from django.urls import path
from .views import ekle, guncelle, listele, sil, detay

urlpatterns = [
    path('ekle/', ekle, name='product-ekle'),
    path('listele/', listele, name='product-listele'),
    path('sil/<int:pk>', sil, name='product-sil'),
    path('guncelle/<int:pk>', guncelle, name='product-guncelle'),
    path('detay/<int:pk>', detay, name='product-detay'),
]
