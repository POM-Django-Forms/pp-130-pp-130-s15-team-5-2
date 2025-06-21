from django import forms
from django.core.validators import MinLengthValidator
from .models import Author

class AuthorForm(forms.ModelForm):
    name = forms.CharField(
        max_length=20,
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        validators=[MinLengthValidator(2, message="Name must be at least 2 characters long.")]
    )

    surname = forms.CharField(
        max_length=20,
        label="Surname",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
        validators=[MinLengthValidator(2, message="Surname must be at least 2 characters long.")]
    )

    patronymic = forms.CharField(
        max_length=20,
        required=False,
        label="Patronymic",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patronymic'})
    )

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
