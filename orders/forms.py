from django import forms
from localflavor.au.forms import AUPostCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = AUPostCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
