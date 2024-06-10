"""
Defines a Django form for creating and updating instances of the UserModel model.

This form allows users to input data for various fields including user name, password, email, phone, and address.
Additionally, it provides custom validation to ensure the uniqueness of the user name and email fields.

Attributes:
    UserModelForm: A subclass of forms.ModelForm representing the form for UserModel model.
"""
from django import forms
from adminapp.models import Adminmodel


class AdminModelForm(forms.ModelForm):
    class Meta:
        model = Adminmodel
        fields = ['Username', 'Password', 'Email', 'Phonenumber']



        widgets = {
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Username': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_username(self):
        """
        Custom validation method to ensure the uniqueness of the user name.

        Raises:
            forms.ValidationError: If the user name already exists in the database.
        """
        Username = self.cleaned_data.get('Username')
        if Adminmodel.objects.filter(user_name=Username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        return Username

    def clean_Email(self):
        """
        Custom validation method to ensure the uniqueness of the email address.

        Raises:
            forms.ValidationError: If the email address already exists in the database.
        """
        Email = self.cleaned_data.get('Wmail')
        if Adminmodel.objects.filter(user_email=Email).exists():
            raise forms.ValidationError("Email address already exists. Please use a different one.")
        return Email
