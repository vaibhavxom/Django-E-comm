from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

    Shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'full name'}),required=True)
    Shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),required=True)
    Shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address1'}),required=True)
    Shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address2'}),required=True)
    Shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),required=True)
    Shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),required=False)
    Shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'zipcode'}),required=False)
    Shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),required=True)

    class Meta:
        model = ShippingAddress
        fields = ['Shipping_full_name','Shipping_email','Shipping_address1','Shipping_address2','Shipping_city','Shipping_state','Shipping_zipcode','Shipping_country']

        exclude =['user',]    