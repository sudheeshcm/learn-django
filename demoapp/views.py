from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import AboutFeature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Welcome to my first Django project!</h1>')
    context = {
        'name': 'John Doe',
        'age': 30,
        'is_student': False,
        'grades': [85, 90, 78, 92, 88],
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zip': '12345'
        }
    }
    return render(request, 'index.html', context)

# Home page - Medilab
def home(request):
    # about1 = AboutFeature(0, 'Fast and Furious', 'Our services are very fast and responsive', True, 'fa-vial-circle-check')
    # about2 = AboutFeature(1, 'Reliable and trustworthy', 'Our services are very reliable with zero downtime', True, 'fa-pump-medical')
    # about3 = AboutFeature(2, '24x7 Support', 'We offer 24x7 support round the clock', False, 'fa-heart-circle-xmark')
    # about4 = AboutFeature(3, 'Affordable and best', 'Our services are affordable and best in quality', True, 'fa-vial-circle-check')

    about_features = AboutFeature.objects.all()

    context = {
        # 'about_features': [about1, about2, about3, about4]
        'about_features': about_features
    }

    return render(request, 'home.html', context)

# Counter page
def counter(request):
    return render(request, 'counter.html')

# Counter results page
def submit_counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'submit-counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')