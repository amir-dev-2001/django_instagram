from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError(_('The username you entered is already existing'))
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_('The email you entered is already existing'))

        return self.cleaned_data
    
    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data['username']).first()
        if user is None:
            raise forms.ValidationError(_('The username does not exist'))
        
        # if not user.check_password(self.cleaned_data['password']):
        #     raise forms.ValidationError(_('wrong password'))

        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError(_('unable to authenticate user with this username and password'))
        
        self.cleaned_data['user'] = user
        return self.cleaned_data
    

    
