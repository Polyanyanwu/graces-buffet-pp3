""" Custom form for user creation """

from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from .models import Profile


class CustomSignupForm(SignupForm):
    """ Custom signup form """
    first_name = forms.CharField(max_length=30, label='First Name',
                                 required=True, widget=forms.TextInput(
                                  attrs={'placeholder': 'First name'}))

    last_name = forms.CharField(max_length=30, label='Last Name',
                                required=True, widget=forms.TextInput(
                                 attrs={'placeholder': 'Last name'}))

    field_order = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        readonly_fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'special_request')
