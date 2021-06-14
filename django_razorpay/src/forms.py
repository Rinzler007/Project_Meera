from django import forms
from .models import Corals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CoralForm(forms.ModelForm):
    class Meta:
        model=Corals
        # fields="__all__"
        fields=['name', 'email', 'contact_no', 'address_1', 'address_2', 'pincode', 'city', 'state', 'country', 'package']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper(self)
        self.helper.layout=Layout(
            'name', 'email', 'contact_no', 'address_1', 'address_2', 'pincode', 'city', 'state', 'country', 'package',
            Submit('submit', 'Confirm')
        )