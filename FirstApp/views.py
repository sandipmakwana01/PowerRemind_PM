from django.shortcuts import render, redirect , get_object_or_404
from FirstApp.models import *
from FirstApp.forms import *
from django.contrib.auth import logout as logoutuser
from django.contrib import messages


def index(request): # client page
    if request.session.get('user_name'):
        user = Authentication.objects.get(user_name=request.session['user_name'])
        client_details =  Client.objects.filter(user=user)

       
        return render(request,'index.html',{"client_details":client_details})
    else:
        return redirect('login')

def client_add_view(request):
    if request.session.get('user_name'):
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                client = form.save(commit=False)
                client.user = Authentication.objects.get(user_name=request.session['user_name'])
                client.save()
                messages.success(request, 'Client added successfully.')
                return redirect('client')
            else:
                print(form.errors)
        else:
            form = ClientForm()

        return render(request,"Menu/client-add.html")
    else:
        return redirect('login')

def client_update_view(request,id):
    if request.session.get('user_name'):
        user = Authentication.objects.get(user_name=request.session['user_name'])
        client_details = get_object_or_404(Client, id=id,user=user)
        if request.method == 'POST':
            form = ClientUpdateForm(request.POST, instance=client_details)
            if form.is_valid():
                form.save()
                messages.success(request, 'Client details updated successfully.')
                return redirect('client')
        else:
            form = ClientUpdateForm(instance=client_details)

        return render(request,"Menu/client-update.html" ,{"client":client_details})
    else:
        return redirect('login')

def profile(request):   
    if request.session.get('user_name'):
        return render(request , 'Menu/profile.html')
    else:
        return redirect('login')

### Authentication ###
def register(request):
    if request.method == 'POST':

        user_name = request.POST['user_name']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not (user_name and password and confirm_password):
            messages.warning(request,'Please fill in all the required fields.')
        elif password != confirm_password:
            messages.error(request,'Passwords and Confirm Password do not match.') 
        elif Authentication.objects.filter(user_name = user_name):
            messages.error(request,'This Username is already Registerd. Please enter a different Username') 
        else:
            authentication_data = { 
                'user_name' : user_name,
                'password' : password, 
            }

            authentication_form = Authentication_Form(authentication_data)
            if authentication_form.is_valid():
                authentication_form.save()
                return redirect('login')
            
    return render(request , 'Authentication/register.html')

def login(request):
    if request.method == 'POST':
        # print(User.username)
        user_name = request.POST['user_name']
        password = request.POST['password']

        if not (user_name and password):
            messages.warning(request,'Please fill in all the required fields.')
        else:
            check_user_name = Authentication.objects.filter(user_name = user_name)
            check_password = Authentication.objects.filter(password = password)

            if check_user_name and check_password:
                messages.success(request, "Your Login successfully!")
                get_data = Authentication.objects.get(user_name = user_name)
                request.session['user_name'] = get_data.user_name
                request.session['password'] = get_data.password

                return redirect('client')
            else:
                messages.error(request,'Incorect Username and Password')

    return render(request , 'Authentication/login.html')
def logout(request):
    logoutuser(request)
    return redirect('login')


