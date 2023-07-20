from .views import *

from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('register', register_attempt, name="register_attempt"),
    path('login', login_attempt, name="login_attempt"),
    path('token', token_send, name="token_send"),
    path('success', success, name="success"),
    path('verify/<auth_token>', verify, name="verify"),
    path('error', error_page, name="error"),
    path('attente', attente, name="attente"),
    path('verification', verification_attempt, name="verification_attempt"),
    path('renvoyer',renvoie, name="renvoie"),
    path('registerfinal', register_final, name="register_final"),
    path('livret', livret_electronique, name="livret_electronique"),
    path('livret_home', livret_home, name="livret_home"),
    path('suggestion', suggestion_client, name="suggestion_client")
]