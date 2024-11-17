from django import forms
from .models import Authentication , Client

class Authentication_Form(forms.ModelForm):
    class Meta:
        model=Authentication
        # fields='__all__'
        fields=['user_name','password']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact_number', 'start_date', 'amount', 'percentage', 'status']

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact_number','start_date', 'percentage', 'amount_add','amount_delete','interest_add','interest_delete','status',]

