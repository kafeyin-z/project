from django.urls import path
from .views import kayit, giris, cikis

urlpatterns = [
    path('kayit/', kayit, name='user-kayit'),
    path('giris/', giris, name='user-giris'),
    path('cikis/', cikis, name='user-cikis'),
]
