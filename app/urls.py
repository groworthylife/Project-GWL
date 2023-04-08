from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # Main
	path('', views.welcomePage, name="welcome"),
	path('home/', views.homePage, name="home"),
	path('help/', views.helpPage, name="help"),
	
	# Game
	path('game/', views.gamePage, name="game"),
	path('avatar/', views.avatarPage, name="avatar"),
	path('mad-block/', views.madBlockPage, name="mad-block"),
	
	# Quiz
	path('quiz/', views.quizPage, name="quiz"),
    
	# Academics
	path('academics/', views.academicsPage, name="academics"),
	path('subjects/<class_id>/', views.subjectPage, name="subjects"),
	path('chapters/<subject_id>/', views.chapterPage, name="chapters"),
]