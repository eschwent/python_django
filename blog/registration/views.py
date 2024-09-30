from django.shortcuts import render
from registration import forms, models

# Create your views here.
def index(request):
    return render(request, "index.html")

def regview(request):
    registration_form = forms.UserInfoForm()
    
    if request.method =="POST":
        registration_form = forms.UserInfoForm(data=request.POST)
        
        if registration_form.is_valid():
            registration_form.save(commit=True)
    else:
        print("Something is wrong")
    my_dictionary = {'register': registration_form}
    return render(request, "registration.html", context = my_dictionary)
    
def mylogin(request) :
    login_form = forms.UserLoginForm()
    
    if request.method == "POST":
        login_form = forms.UserLoginForm(data=request.POST)
        if login_form.is_valid():
            login_form.save(commit=True)
    else:
        print("Something is wrong")
        login_dictionary = {'userlogin': login_form}
    return render(request, "login.html", context = login_dictionary)