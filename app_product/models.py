from django.contrib.auth.models import User
from django.db import models


# class ProductQuerySet(models.query.QuerySet):
#     def active(self):
#         return self.filter(active=True)
#
#     def outline(self):
#         return self.filter(outline=True)
#
#
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)
#
#     def all(self):
#         return self.get_queryset().active().outline()
#
#     def get_by_id(self, id):
#         return self.get_queryset().filter(id=id)
#
#     def get_my_outline(self, author_id):
#         return self.get_queryset().filter(author=author_id)

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

    # objects = ProductManager()

    # Template de kullanımı {{ post.get_image }}
    def get_image(self):
        if self.images:
            return self.images.url
        else:
            return None

    def get_username(self):
        if self.author:
            return self.author
        else:
            return None
