from django.urls import path
from . import views
from .views import teacher_login_view, teacher_dashboard
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/add-question/', views.add_question, name='add_question'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('add-question/', views.add_question, name='add_question'),
    path('attempt-exam/', views.attempt_exam, name='attempt_exam'),
    path('results/', views.results_view, name='results'),
    path('teacher/login/', views.teacher_login_view, name='teacher_login'),
]