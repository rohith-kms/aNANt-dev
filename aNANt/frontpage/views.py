from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from .forms import UserRegisterForm

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()
from .forms import UserRegisterForm
#from .tokens import account_activation_token

# Create your views here.

def index(request):

    template = loader.get_template('frontpage/index.html')
    context={}

    return HttpResponse(template.render(context, request))

def standard_page(request,heading,content):

    template = loader.get_template('frontpage/template.html')
    context={"heading":heading, "content":content}

    return HttpResponse(template.render(context, request))

def about(request):

    template = loader.get_template('frontpage/about.html')
    context={}

    return HttpResponse(template.render(context, request))

def contact(request):

    template = loader.get_template('frontpage/contact.html')
    context={}

    return HttpResponse(template.render(context, request))

def publications(request):

    template = loader.get_template('frontpage/publications.html')
    context={}

    return HttpResponse(template.render(context, request))

def acknowledgements(request):

    template = loader.get_template('frontpage/acknowledgements.html')
    context={}

    return HttpResponse(template.render(context, request))

def login_page(request):
    return render(request, 'frontpage/login.html')

def login_view(request):
	
	# Ask for login credentials
	
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	
	# Check if user exists in the database of users
	if user is not None:
		
		# Login if user exists
		login(request, user)
		
	else:
		
		messages.error(request,'Invalid login credentials. Please try again.')
	
	# Redirect to homepage
	response = redirect('/')
	return response

def logout_view(request):
	
	logout(request)
	# Redirect to homepage
	response = redirect('/')
	return response
'''
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            user_email = request.POST.get('email')
            
            #########################mail####################################
            # I don't know what exactly is happening in this block of code. 
            # It's not sending anything. I tried with both my e-mail ids.
            
            htmly = get_template('frontpage/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'hello', 'ananttest2020@gmail.com', user_email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            
            form.save()
            username = form.cleaned_data.get('username')
            #first_name = form.cleaned_data.get('first_name')
            #last_name = form.cleaned_data.get('last_name')
            #messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/login_page')
    else:
        form = UserRegisterForm()
    return render(request, 'frontpage/register.html', {'form': form,'title':'reqister here'})
'''

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            user_email = request.POST.get('email')
            
            #########################mail####################################
            
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your ANANT account.'
            message = render_to_string('frontpage/Email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            ##################################################################
            
            #form.save()
            #username = form.cleaned_data.get('username')
            #first_name = form.cleaned_data.get('first_name')
            #last_name = form.cleaned_data.get('last_name')
            #messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request, 'frontpage/registration_email_sent.html')
    else:
        form = UserRegisterForm()
    return render(request, 'frontpage/register.html', {'form': form,'title':'reqister here'})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/login_page')
    else:
        return HttpResponse('Activation link is invalid!')