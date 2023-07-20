import datetime
import time
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone

from datetime import timedelta
import string


# Create your views here.

@login_required(login_url="/")
def home(request):
    return render(request, 'compte/index.html')


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('pass')

        user_obj = User.objects.filter(username=username).first()
        profile_obj = Client.objects.filter(user=user_obj).first()
        if user_obj is None:
            messages.success(request, 'Utilisateur introuvable.')
            return redirect('/login')

        

        if  profile_obj is None:
            messages.success(request, 'Utilisateur Int.')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Mot de Passe incorrect.')
            return redirect('/login')
        login(request, user)
        return redirect('/livret')

    return render(request, 'compte/login.html')



def register_attempt(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        if phone == "email":
            try:
                validate_email(email)
                code = random.randint(100000, 999999)
                timestamp = time.time()
                expiration_time = timestamp + 180

                print(code)
                request.session['verification_code']=code
                request.session['verification_expiration']=expiration_time
                request.session['email']=email
                # mail deja existant
                if Profile.objects.filter(phone_mail=email).exists():
                    profile=Profile.objects.filter(phone_mail=email).first()
                
                    if profile:
                        if profile.phone_mail==email:
                            if profile.en_attente=="refuser":
                                return redirect("/registerfinal")
                    else:
                        return redirect("/attente")   
                else:
                    messages.success(request, 'Cet e-mail est déjà utilisé. Veuillez en choisir un autre')
                    return render(request, 'compte/register.html')
                    

                send_mail_after_registration(email, code)
                messages.success(request, 'veuillez entrer le code envoye par mail. Valide pour 3 mins')
                return redirect('/verification')
            
            except ValidationError:
                messages.success(request, 'veuillez entrer un email valide')
                 
                return redirect('/register')
        else:
            return redirect('/register')

    return render(request, 'compte/register.html')



def success(request):
    return render(request, 'compte/success.html')


def token_send(request):
    return render(request, 'compte/token_send.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        print(profile_obj)
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
    return redirect('/')


def error_page(request):
    return render(request, "compte/error.html")


def send_mail_after_registration(email, code):
    subject = 'Your account need to be verified'
    message = f'Votre code de verification est {code}'
    email_from = settings.EMAIL_HOST_USER
    
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def send_sms(phone_number, message):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        
        body =message,
        to = phone_number
    )

def attente(request):
    return render(request, "compte/attente.html")



# Create your views here.

def verification_attempt(request):

    if request.method == 'POST':
            codes = request.POST.get('code')
            stored_code = request.session.get('verification_code')
            expiration = request.session.get('verification_expiration')
            print(stored_code)

            

            if time.time() > expiration :
                messages.error(request,"code expire. veuillez renvoyer le code")
                return redirect('/renvoyer')
            else:
                print(type(codes) )
                nbr = int(codes)
                if nbr == stored_code:
           
                    messages.success(request, 'Votre profile est verifier')
                    return redirect('/registerfinal')
                else:
                    messages.error(request, 'code incorrect')
                    return redirect('/verification')

    return render(request, 'compte/verification.html')
   

def renvoie(request):
    email = request.session.get('email')
    codes = random.randint(100000, 999999)
    timestamp = time.time()
    expiration_time = timestamp + 60

                
    request.session['verification_code']=codes
    request.session['verification_expiration']=expiration_time
    request.session['email']=email
    print(codes)
    send_mail_after_registration(email, codes)
    messages.success(request, 'veuillez entrer le code envoye par mail. Valide pour 1mins')
                
    return redirect('/verification')


    return render(request, 'compte/renvoie.html')


def register_final(request):
     
    if request.method == 'POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        date_naissance=request.POST.get('date_naissance')
        adresse=request.POST.get('adresse')
        cni=request.POST.get('cni')
        profession=request.POST.get('profession')
        Type_compte=request.POST.get('type_compte')
        Zone=request.POST.get('Zone')
        Frais_tontine=request.POST.get('Frais_tontine')
        nom_garant=request.POST.get('nom_garant')
        prenom_garant=request.POST.get('prenom_garant')
        telephone_garant=request.POST.get('telephone_garant')
        adresse_garant=request.POST.get('adresse_garant')
        cni_garant=request.POST.get('cni_garant')
        profession_garant=request.POST.get('profession_garant')

        phone_mail = request.session.get('email')
        print(phone_mail)
        
        print(nom,prenom)
        # Erreur si tous les champs ne sont pa saisi
        if not (nom and prenom and date_naissance and adresse and cni and profession and Type_compte and
                nom_garant and prenom_garant and telephone_garant and adresse_garant and cni_garant and profession_garant and Zone and Frais_tontine):
            
            messages.error(request,'Veuillez remplir tous les champs requis.')
            print(messages.error)
            return redirect('/registerfinal')
           
        
        client = Profile(
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            phone_mail = phone_mail,
            adresse=adresse,
            cni=cni,
            profession=profession,
            Zone=Zone,
            Frais_tontine=Frais_tontine,
            Type_compte=Type_compte,
            nom_garant=nom_garant,
            prenom_garant=prenom_garant,
            telephone_garant=telephone_garant,
            adresse_garant=adresse_garant,
            cni_garant=cni_garant,
            profession_garant=profession_garant
        )

        client.save()

        
        return redirect('/attente')


    return render(request, 'compte/registerfinal.html')


def livret_electronique(request):
    return render(request, "admin/comptable.html")

def livret_home(request):
    return render(request, "compte/livret_home.html")



def suggestion_client(request):
    if request.method == 'POST':
        suggestion_title = request.POST.get('suggestionTitle')
        suggestion_content = request.POST.get('suggestionContent')
        email= 'gestionepargne4@gmail.com'
        # Envoi de l'e-mail à l'administrateur
        send_mail_after_registration(email, suggestion_content)

        # Ajout du message d'alerte info
        messages.info(request, 'Votre suggestion a été envoyée avec succès.')

        # Redirection vers une page de confirmation ou autre
        return redirect('suggestion')

    return render(request, 'compte/suggestion.html')

