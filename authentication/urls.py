from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('accounts/', views.accountsPage, name="accounts"),
	path('login/', views.LogIn, name="login"),
	path('register/', views.SignUp, name="register"),
    path('forgot/', views.Forget, name="forgot"),
	path('reset/<token>/', views.Reset, name="reset"),
    path('logout/', views.logoutView, name="logout"),
]