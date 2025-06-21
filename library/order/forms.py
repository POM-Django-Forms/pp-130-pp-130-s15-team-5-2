# forms.py
from django import forms
from django.utils import timezone
from .models import Order

class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['plated_end_at']

    plated_end_at = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Planned Return Date"
    )

    def clean_plated_end_at(self):
        plated_end_at = self.cleaned_data['plated_end_at']
        today = timezone.now().date()

        if plated_end_at <= today:
            raise forms.ValidationError("Planned return date must be after today.")
        return plated_end_at
