from django.urls import path
from .views import kayit, giris, cikis, profil, sifre_degistir, profil_degistir

urlpatterns = [
    path('kayit/', kayit, name='user-kayit'),
    path('giris/', giris, name='user-giris'),
    path('cikis/', cikis, name='user-cikis'),
    path('', profil, name='user-profil'),
    path('guncelle/', profil_degistir, name='user-profil_guncelle'),
    path('sifre_degistir/', sifre_degistir, name='user-sifre'),
]
