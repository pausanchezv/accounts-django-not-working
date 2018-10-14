from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        """ Meta """

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        """ Save method """
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    """ Edit form """

    class Meta:
        """ Meta """

        model = User

        # only django user fields (not one to one relationship object)
        fields = (
            'username',
            'first_name',
            'last_name',
            'password' #mandatory
        )
