from django import forms
from registration.models import UserInformation

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserInformation
        fields = '__all__'

class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = UserInformation
        fields = ('username', 'password')