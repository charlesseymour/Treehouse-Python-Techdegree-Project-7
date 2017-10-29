import bleach
from django import forms
from django.core import validators
from django.core.validators import MinLengthValidator

from . import models


class AccountForm(forms.ModelForm):

    email_confirm = forms.EmailField(max_length=255, label='Confirm email')

    class Meta:
        model = models.Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'email_confirm',
            'birth_date',
            'bio',
            'avatar'
        ]

    def clean_bio(self):
        data = self.cleaned_data['bio']
        if len(data) < 10:
            raise forms.ValidationError('''Bio should be 10 characters
                                        or longer''')
        data = bleach.clean(data)
        return data

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('email_confirm')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")
