from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Booking


class BookingForm(forms.ModelForm):
    travel_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = [
            'prefix', 'name', 'country_of_residency', 'email', 'whatsapp_number',
            'destination', 'number_of_days', 'number_of_people', 'travel_date',
            'accommodation', 'budget', 'preferred_activities', 'special_request'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book A Tour'))