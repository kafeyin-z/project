from django.urls import path
from .views import kayit, giris, cikis, profil

urlpatterns = [
    path('kayit/', kayit, name='user-kayit'),
    path('giris/', giris, name='user-giris'),
    path('cikis/', cikis, name='user-cikis'),
    path('profil/', profil, name='user-profil'),
]
