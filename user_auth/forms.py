from django import forms

from user_auth.models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields=["first_name","last_name","username", "email", "password","phone_number","role"]
        


class LoginForm(forms.ModelForm):
    class Meta:
        model:CustomUser
        fields = ['username', 'password']
        
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number',"password"]