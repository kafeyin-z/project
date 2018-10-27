from django.contrib.auth.models import User
from django.db import models


# FIXME: Yüklenen resim boyutu sınırı yok
class Product(models.Model):
    title = models.CharField(null=True, blank=False, max_length=100)
    content = models.TextField(null=True, blank=False, max_length=1000)
    images = models.ImageField(null=True, blank=True, upload_to='product')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    outline = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Template de kullanımı {{ post.get_image }}
    def get_image(self):
        if self.images:
            return self.images.url
        else:
            return None
