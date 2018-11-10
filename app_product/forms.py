from django import forms
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget

from .models import Product


class ProductForms(forms.ModelForm):
    tags = TagField(required=True, widget=LabelWidget)

    class Meta:
        model = Product
        fields = ['title', 'content', 'images', 'tags', 'draft']

    def clean(self):
        tags = self.cleaned_data.get('tags')
        # print(tags.__len__())
        tags_len = tags.__len__()
        if tags_len > 3:
            raise forms.ValidationError('En fazla üç adet etiket oluşturabilirsiniz.')
