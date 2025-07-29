from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, QuestionForm
from .models import UserProfile, Question, Result
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def register(request):
    return render(request, 'exam/register.html')



# Adjust path as per your templates folder


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, role=form.cleaned_data['role'])
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def register_view(request):
    return render(request, 'exam/register.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                role = UserProfile.objects.get(user=user).role
                if role == 'student':
                    return redirect('student_dashboard')
                else:
                    return redirect('teacher_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_dashboard(request):
    questions = Question.objects.all()
    return render(request, 'student_dashboard.html', {'questions': questions})

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.created_by = request.user
            q.save()
            return redirect('teacher_dashboard')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'exam/home.html')  # If file is in templates/exam/home.html

# exam/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile  # Make sure this model contains user roles like 'student' or 'teacher'

@login_required
def dashboard_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        
        if profile.role == 'student':
            return render(request, 'student_dashboard.html', {'user': request.user})
        elif profile.role == 'teacher':
            return render(request, 'teacher_dashboard.html', {'user': request.user})
        else:
            return render(request, 'dashboard.html', {'user': request.user})
            
    except UserProfile.DoesNotExist:
        return redirect('login')  # Redirect if profile not found
    
    
    from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def add_question(request):
    return render(request, 'add_question.html')

@login_required
def attempt_exam(request):
    return render(request, 'attempt_exam.html')

@login_required
def results_view(request):
    return render(request, 'results.html')

def register_view(request):
    return render(request, 'exam/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Optional: Check if the user is a teacher
            # if not user.profile.is_teacher:
            #     messages.error(request, "Access denied. Not a teacher.")
            #     return render(request, 'teacher_login.html')

            login(request, user)
            return redirect('teacher_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'teacher_login.html')
    else:
        return render(request, 'teacher_login.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.groups.filter(name='Teachers').exists():
            login(request, user)
            return redirect('teacher_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not a teacher.')
    return render(request, 'teacher_login.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user belongs to "Teachers" group
            if user.groups.filter(name='Teachers').exists():
                login(request, user)
                return redirect('teacher_dashboard')  # Make sure this URL name exists
            else:
                messages.error(request, 'You are not authorized as a teacher.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'teacher_login.html')  # Make sure this template exists

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')
