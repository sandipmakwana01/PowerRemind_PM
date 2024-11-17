from django.shortcuts import render, redirect , get_object_or_404
from FirstApp.models import *
from FirstApp.forms import *
from django.contrib.auth import logout as logoutuser
from django.contrib import messages


def index(request):
    if request.session.get('user_name'):
        user = Authentication.objects.get(user_name=request.session['user_name'])
        client_details =  Client.objects.filter(user=user)
        return render(request,'index.html',{"client_details":client_details})
    else:
        return redirect('login')

# Menu #
def client_add_view(request):
    if request.session.get('user_name'):
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                client = form.save(commit=False)
                client.user = Authentication.objects.get(user_name=request.session['user_name'])
                client.save()
                messages.success(request, 'Client added successfully.')
                return redirect('home')
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
                return redirect('home')
        else:
            form = ClientUpdateForm(instance=client_details)

        return render(request,"Menu/client-update.html" ,{"client":client_details})
    else:
        return redirect('login')
    

def client_delete_view(request,id):
    if request.session.get('user_name'):

        user = Authentication.objects.get(user_name=request.session['user_name'])
        client_details = get_object_or_404(Client, id=id, user=user)
        
        client_details.delete() 
        messages.success(request, 'Client deleted successfully.')
        return redirect('home')  

    else:
        return redirect('login')

# Authentication #
def login(request):
    if request.method == 'POST':
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

                return redirect('home')
            else:
                messages.error(request,'Incorect Username and Password')

    return render(request , 'Authentication/login.html')

def logout(request):
    logoutuser(request)
    return redirect('login')


