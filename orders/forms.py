from django import forms
from .models import Order


class OrderForm(forms.ModelForm): # create a form for the Order model 不用每次创建了
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_note']
