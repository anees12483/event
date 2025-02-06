from django.forms import forms,Textarea,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserAddform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        


        
        


