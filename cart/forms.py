
from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    street_address = forms.CharField(max_length=255, label="Street Address")
    apartment_address = forms.CharField(max_length=255, required=False, label="Apartment Address")
    city = forms.CharField(max_length=100, label="Town / City")
    phone = forms.CharField(max_length=15, label="Phone")
    email = forms.EmailField(label="Email Address")
