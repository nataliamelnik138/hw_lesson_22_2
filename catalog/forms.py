from django import forms

from catalog.models import Product, Version
from config import settings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'image', 'category', 'price',)

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if product_name and set(product_name.lower().split()).intersection(set(settings.FORBIDDEN_WORDS)):
            raise forms.ValidationError('Нельзя использовать запрещенные слова')
        return product_name


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('number', 'name', 'is_activ',)
