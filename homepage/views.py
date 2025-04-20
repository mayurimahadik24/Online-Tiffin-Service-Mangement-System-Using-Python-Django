from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from customers import views
from .forms import UserCreateForm
from customers.models import *
# from customers.forms import  CustomerForm




def index(request):
    page = 'login'

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            print("Username does not exist")
        
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('loggedin')
        else:
            print("Username or password is incorrect")

    context = {'page':page}
    return render(request, "homepage/index.html",context)

@login_required(login_url='login')
def loggedIn(request):
    
    return render(request,"homepage/loggedin.html")

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def homepage_pincode_search(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        # perform your search logic here with the pincode entered
        # redirect the user to the homepage with the required data
        return redirect('login')
    else:
        return render(request, 'pincode_search/pincode_search.html')
# user = Customer.objects.get(id =pk)
# print(user)

# def feedback(request):
    
#     user = request.user.id
#     required_user = Customer.objects.get(id = user)
#     print(required_user)
#     # form = CustomerFeedbackForm(instance=required_user)
#     # if request.method == 'POST':
#     #     form = CustomerFeedbackForm(request.POST, instance=required_user)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, "Your feedback sent successfully. Thank you.")
#     # context = {'form':form}
#     return render(request,"homepage/feedback.html")

def registerUser(request):
    page = 'register'
    form = UserCreateForm()

    if request.method=="POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
           
            user.save()
            messages.success(request, 'User account created successfully')

    context={'page':page, 'form':form}
    return render(request, 'homepage/index.html',context)

def homepage(request):
    page='pincode_search'
    # Use the "pincode" parameter to customize the page content
    # For example, display different products or prices based on the user's location
    context = {'page': page}
    return render(request, 'homepage/loggedin.html', context)