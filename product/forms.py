from django import forms
from .models import Item


class ItemCreateForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'memo', 'price', 'status', 'shipping_burden', 'shipping_area', 'shipping_days')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
