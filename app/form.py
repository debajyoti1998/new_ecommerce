from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm ,UsernameField,PasswordChangeForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Costomar
class CastomarRegistationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password' ,'class':'form-control'}),
    )

class MyPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
       
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )


class CostomarProfile(forms.ModelForm):
    class Meta:
        model=Costomar
        fields=['name','location','city','state','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


# class student_class(forms.Form):
#     username=forms.CharField(widget=forms.TextInput( attrs={'id':'debajyoti','class':'form-control'}))          #(initial='debajyoti')
#     email=forms.EmailField()
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     key=forms.CharField(widget=forms.HiddenInput)
#     password=forms.CharField(widget=forms.PasswordInput)


