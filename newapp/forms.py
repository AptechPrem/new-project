from newapp.models import Login
from django import forms
class LoginModel(forms.ModelForm):
    class Meta:
        model = Login
        fields = ("username","password","emailaddress")
        widgets = {'password':forms.PasswordInput} 