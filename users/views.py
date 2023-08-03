from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import User

def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if user with email exists 
        if User.objects.filter(email=email).exists():
            error_message = {'error_message':'User with this email already exists.'}
            return render(request,'users/signup.html',context=error_message)
        
        # Check if password is correct and then create a new user and redirect to login
        if password1 == password2:
            user = User.objects.create(full_name=full_name,email=email)
            user.set_password(password1)
            user.save()
            messages.success(request,'Signup successful. Please login.')
            return redirect('login')
        else:
            error_message = {'error_message':'Incorrect Passwords.'}
            return render(request,'users/signup.html',context=error_message)
    return render(request,'users/signup.html')

def login_view(request):
    """ Login view. Check if request is POST, then get email and password from html form. """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Get the user from email then check if password matches 
        try:
            user = User.objects.get(email=email)
            # if password matches login the current user and redirect to home
            if user.check_password(raw_password=password):
                login(request=request,user=user)
                return redirect('home')
            # else show error message
            else:
                error_message = {'error_message':'Invalid credentials.'}
                return render(request,'users/login.html',context=error_message)
        except User.DoesNotExist:
            error_message = {'error_message':'Invalid credentials.'}
            return render(request,'users/login.html',context=error_message)
    return render(request,'users/login.html')

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    context = {'user':user}
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        photo = request.FILES.get('photo',None)
        user.full_name = full_name
        user.email = email
        if photo:
            user.photo = photo
        user.save()
        context['message'] = 'Profile Updated'
        return render(request,'users/profile.html',context=context)
    return render(request,'users/profile.html',context=context)

def logout_view(request):
    logout(request)
    return redirect('home')