from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userproject import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import *


# Create your views here.

def index(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        # username = request.post.get('username')
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # restrictions
        if User.objects.filter(username = username):
            messages.error(request, "Username Already Exists!!")
            return redirect('signup')

        if User.objects.filter(email = email):
            messages.error(request, "Email Already Exists!!")
            return redirect('signup')

        if len(username)>10:
            messages.error(request, "Username Must Be Less Than 10 characters!!")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Password Didn't Match!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "UserName Must Be AlphaNumeric")
            return redirect('signup')
        
        # create user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False
        myuser.save()

        messages.success(request,"Your Account Has Been Successfully Created!! Please Check Your Email For Confirmation")

        #Welcome Email

        subject = "Welcome to My Django App!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to @myDjangoApp\n\nPlease confirm your Email"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)

        
        # email address confirmation  email 

        current_site = get_current_site(request)
        email_subject = "Confirm your email @myDjangoApp"
        message2 = render_to_string('email_conf.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )

        email.fail_silently = True
        email.send()


        return redirect('signin')
    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1= request.POST.get('pass1')

        user = authenticate(username = username, password = pass1)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            messages.success(request, f"Hello {fname}, You Are Successfully Logged In")
            return redirect('home')
            # return render(request, 'index.html', {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk = uid)
    except(TypeError,ValueError,OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Hello, You are successfully logged in")
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

