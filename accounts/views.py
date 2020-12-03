from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from .form import SignUpForm

# def signup(request):
#     if request.method=='POST':
#         # todo : POST입력방식(주소창 입력)으로 입력 받은 내용으로 회원 객체를 생성한다.
#         username=request.POST.get('username')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#
#         print(username,password,password2)
#
#         user=User()
#         user.username=username
#         user.set_password(password)
#         user.save()
#         return render(request,'account/signup_complete.html')
#     else:
#         # todo: 일반적인 방식으로 form 객체를 만들어서 전달한다.
#         context_values={'form':'this is form'}
#         return render(request,'accounts/signup.html',context_values)

def signup(request):
    if request.method=='POST':
        # todo : POST입력방식(주소창 입력)으로 입력 받은 내용으로 회원 객체를 생성한다.
        signup_form=SignUpForm(request.POST)
        if signup_form.is_valid():
            user_instance=signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request,'accounts/signup_complete.html',{'username':user_instance.username})
    else:
        # todo: 일반적인 방식으로 form 객체를 만들어서 전달한다.
        signup_form=SignUpForm()
    return render(request,'accounts/signup.html',{'form':signup_form})

