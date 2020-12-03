from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
class SignUpForm(forms.ModelForm):

    password=forms.CharField(label='password', widget=forms.PasswordInput)
    Confirm_password = forms.CharField(label='Confirm_password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password','Confirm_password','first_name','last_name','email',]


    def clean_Confirm_password(self):
        cd=self.cleaned_data
        if cd['password'] != cd['Confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['Confirm_password']
