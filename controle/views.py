
import uuid

from django.urls import reverse

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from controle.send_sms import send_sms
from .models import *
from accounts.models import *
from django.core.mail import send_mail
from django.conf import settings
import random
import string



def controle(request):
    template = loader.get_template('admin/index1.html')
    return HttpResponse(template.render())

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         #        print(username,password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Connecte l'utilisateur
            
            if user.is_superuser:
                # Redirection de l'administrateur vers la page admin.html
                return redirect('/index2')
            elif user.is_staff: 
                # Redirection de l'agent de crédit vers la page crédit.html
                return redirect('')
        
    # Si les informations d'identification sont invalides ou si la méthode HTTP n'est pas POST
    # ou si l'utilisateur n'a pas les autorisations appropriées, redirigez vers une autre page
    return render(request, 'admin/login1.html')






def index2_admin(request):
    dash = Profile.objects.filter(en_attente = "en_attente")
    nb = dash.count()
    print (dash)
    context={
        "nb":nb
    }
    print(nb)

    return render(request, 'admin/index2.html',context)
    

def pause_client(request):
    profiles = Profile.objects.filter(en_attente="en_attente") 

    return render(request, 'admin/pause.html', {'users': profiles})
    

def inscrit_client(request):
    profiles = Client.objects.all()
    
    
    return render(request, 'admin/inscrit.html', {'users': profiles})

#def user_list(request):
    #users = Profile.objects.all()
    #return render(request, 'admin/pause.html', {'users': users})

def delete_user(request, user_id):
    pass
def accept_user(request, user_id):
    pass


def pause_details(request, id):
    print(id)
    client = Profile.objects.filter(id=id).first()
    print(client)

    return render(request, 'admin/pause_details.html', {'client': client})

def inscrit_details(request, id):
    print(id)
    client = Client.objects.filter(identifiant=id).first()
    print(client)
     
    return render(request, 'admin/inscrit_details.html', {'client': client})

def send_mails(email, messag):
    subject = 'Resultat de votre demande'
    message = messag
    email_from = settings.EMAIL_HOST_USER
    
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def accepter(request,id):
    print(id)
    client = Profile.objects.filter(id=id).first()

    nom = client.nom
    phone_mail=client.phone_mail
    deux_premieres_lettres = nom[:2]
    # Extraire la dernière lettre du nom
    derniere_lettre = nom[-1]
    
    # Générer un chiffre aléatoire entre 1000 et 100000
    chiffre_aleatoire = random.randint(100, 1000)
    
    # Générer le mot de passe aléatoire de 8 caractères différents
    caracteres_possibles = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.sample(caracteres_possibles, 8))
    
    # Générer l'identifiant en combinant les parties nécessaires
    identifiant = deux_premieres_lettres + derniere_lettre + str(chiffre_aleatoire)

    print(identifiant, mot_de_passe)

    user_odj = User(username = identifiant )
    user_odj.set_password(mot_de_passe)
    user_odj.save()


    client_inscrit = Client(nom = client.nom,
                            prenom = client.prenom,
                            phone_mail = client.phone_mail,
                            adresse = client.adresse,
                            date_naissance = client.date_naissance,
                            cni = client.cni,
                            Type_compte = client.Type_compte,
                            profession = client.profession,
                            Zone = client.Zone,
                            Frais_tontine = client.Frais_tontine,
                            nom_garant = client.nom_garant,
                            prenom_garant = client.prenom_garant,
                            telephone_garant = client.telephone_garant,
                            adresse_garant = client.adresse_garant,
                            profession_garant = client.profession_garant,
                            cni_garant = client.cni_garant,
                            user = user_odj,
                            identifiant = identifiant)
    
    client_inscrit.save()
    client.delete()

    message = f'Votre identifiant est {identifiant} et votre mot de passe pour vous connecter est {mot_de_passe} ' \
              f'Voici le lien pour se connecter  http://127.0.0.1:8000/login'
    send_mails(phone_mail,message)
    messages.success(request,"La demande du client a ete accetpté")
    

    return redirect('/pause')
    return render(request, 'admin/pause.html')

def refuser(request, id):
    print(id)
    profile = Profile.objects.filter(id=id).first()
    profile.en_attente='refuser'
    profile.save()
    email=profile.phone_mail
    message = f'votre demande a été rejeté, verifier vos informations et reinscrivez vous' \
              f'Voici le lien pour se reinscrire  http://127.0.0.1:8000/register'
    send_mails(email,message)
    messages.success(request,"La demande du client a été rejeté")
    return redirect("/pause")


def comptable_log(request):
    return render(request, "admin/comptable.html")

def mylogout(request):
    logout(request)
    return redirect('/controle')

def myagent(request):
    agent = Agent.objects.all()
    return render(request, "admin/agent.html", {'users': agent})



def agent_register(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        last_name = request.POST.get('prenom')
        date_naissance = request.POST.get('birthdate')
        Email = request.POST.get('Email')
        adresse = request.POST.get('address')
        cni = request.POST.get('cni')
        zone = request.POST.get('zone')
             
        deux_premieres_lettres = username[:2] if len(username) >= 2 else username
        derniere_lettre = username[-1] if username else ''
        chiffre_aleatoire = random.randint(100, 1000)
        caracteres_possibles = string.ascii_letters + string.digits + string.punctuation
        mot_de_passe = ''.join(random.sample(caracteres_possibles, 8))
            
        identifiant = deux_premieres_lettres + derniere_lettre + str(chiffre_aleatoire)
            
        user_obj = User(username=identifiant)
        user_obj.set_password(mot_de_passe)
        user_obj.save()
         
        message = f"Votre Identifiant est : {identifiant}, votre Mot de passe est  : {mot_de_passe}"
        send_mails(Email, message)

        zon = Client.objects.filter(Zone=zone)
        
       
        agent = Agent.objects.create(identifiant=identifiant, nom=username, prenom = last_name,adresse=adresse,date_naissance= date_naissance,Telephone=Email,Zone=zone,cni=cni,user=user_obj)
        ag = agent.Zone
        print(agent.Zone)
        assigned_clients = Client.objects.filter(agent__Zone=ag)
        clien = Client.objects.filter(Zone=zone).exclude(identifiant__in=assigned_clients.values('identifiant'))
        context={
            "clients":clien
        }
        request.session['id']= identifiant
        return render(request, "admin/liste_client.html",context)   
     # Autres actions à effectuer après l'enregistrement de l'agent
            
    return render(request, "admin/agent_register.html")
    


def agent_suivant(request):
    if request.method == 'POST':
        client_ids = request.POST.getlist('clients')
        ids = request.session.get('id')

        agent = Agent.objects.filter(identifiant=ids).first()
        clients = Client.objects.filter(identifiant__in=client_ids)
        agent.clients.set(clients)
        agent.save
        return redirect('/agent_register')
    
def new_assign(request, id):
    ag = Agent.objects.filter(identifiant = id).first()
    zone = ag.Zone
    assigned_clients = Client.objects.filter(agent__Zone=zone)
    clien = Client.objects.filter(Zone=zone).exclude(identifiant__in=assigned_clients.values('identifiant'))
    

    if request.method == 'POST':
        client_ids = request.POST.getlist('clients')
        

        agent = Agent.objects.filter(identifiant=id).first()
        clients = Client.objects.filter(identifiant__in=client_ids)
        agent.clients.set(clients)
        agent.save
        return redirect('/agent')
    return render(request, 'admin/news.html', {'clients': clien})


def agent_detail(request, id):
    print(id)
    agent = Agent.objects.filter(identifiant=id).first()
    print(agent)

    return render(request, 'admin/agent_details.html', {'agent': agent})


def liste(request):
    return render(request, "admin/liste_client.html")


def finance_agent(request):
    return render(request, "agent/finance.html")


def login_agent(request):
    if request.method == 'POST':
        username = request.POST.get('usernames')
        password = request.POST.get('passwords')

        user_obj = User.objects.filter(username=username).first()
        profile_obj = Agent.objects.filter(user=user_obj).first()
        if user_obj is None:
            messages.success(request, 'Utilisateur introuvable.')
            return redirect('/finance_login')

        

        if  profile_obj is None:
            messages.success(request, 'Utilisateur Int.')
            return redirect('/finance_login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Mot de Passe incorrect.')
            return redirect('/finance_login')
        login(request, user)
        return redirect('/agent_connect')

        

    return render(request, "agent/finance_login.html")

def agent_connection(request):
    return render(request, "agent/agent_connect.html")

def agentlogout(request):
    logout(request)
    return redirect('/finance_login')


def agent_identification(request):
    if request.method == 'POST':
        use = request.user.username
        identifiant = request.POST.get('username')
        user = User.objects.filter(username = use).first()
        agent = Agent.objects.filter(user=user).first()
        clients = agent.get_clients()
        
        
        client = Client.objects.filter(identifiant=identifiant).first()
        if client:
            
            
            for client in clients:
                if client.identifiant == identifiant:
                    print(client.nom, client.prenom, client.identifiant)

                    return redirect("/identificationreussi/{}".format(client.identifiant))
                else:
                    messages.error(request,"Client Introuvable")   
                    return redirect('/agent_identifs') 
        else:
            messages.error(request,"Client Introuvable")
            return redirect('/agent_identifs')
            
            


        

    return render(request, "agent/agent_identif.html")

def identif_reussi(request, id):
    client = Client.objects.filter(identifiant=id).first()
    use = request.user.username
    agent=Agent.objects.filter(identifiant= use).first()
    count = Payement.objects.count()
   
    if request.method == 'POST':
        montant_saisi = request.POST.get('montant')
        mtns = int(montant_saisi)
        cotisation_journaliere = client.Frais_tontine
        jours = int(mtns / cotisation_journaliere)
        print(count)
        if count==0 : 
            nbr_restant = 31 - jours
            Payement.objects.create(client=client, agent=agent,montant_total= mtns, montant_payement=mtns, nbr_jours= jours, jours_restant=nbr_restant, debut = True)
            return redirect("/agent_identifs")
        else:
            pay= Payement.objects.filter(client=client).last()
            print(pay)
            if pay:

                total = mtns + int(pay.montant_total)
                print(total,montant_saisi)
                nbr_restant= pay.jours_restant - jours
                print(nbr_restant)
                print(nbr_restant)
                if nbr_restant == 0:
                    nj= pay.nbr_jours + jours
                    print(nj)
                    nj= pay.nbr_jours + jours
                    print(nj,pay.nbr_jours,jours)
                    Payement.objects.create(client=client, agent=agent, montant_payement=mtns, montant_total = total, nbr_jours= nj, jours_restant=nbr_restant, fin = True)
                    Compte.objects.create(client=client, nom_type_compte= client.Type_compte,solde_payement = total)
                elif nbr_restant<0:
                   
                    hy = jours - pay.jours_restant
                    mnt = hy*cotisation_journaliere
                    mt = mtns-mnt
                    if mt<0:
                        mt = mnt-mtns
                    else:
                        mt = mtns-mnt
                    rest =31-hy
                    Payement.objects.create(client=client, agent=agent, montant_payement=mtns, montant_total = total, nbr_jours= 31, jours_restant=0, fin = True)
                    Payement.objects.create(client=client, agent=agent, montant_payement=mnt, montant_total = total, nbr_jours= hy, jours_restant=rest, debut = True)
                    Compte.objects.create(client=client, nom_type_compte= client.Type_compte,solde_payement = total)
                    return redirect("/agent_identifs")
                    
               
                elif nbr_restant < pay.jours_restant :
                    nbr_restant = pay.jours_restant-nbr_restant
                    Payement.objects.create(client=client, agent=agent,montant_total= total, montant_payement=mtns, nbr_jours= jours, jours_restant=nbr_restant)
                    print("...........hhhhh.......")
                    return redirect("/agent_identifs")
            else:
                print('erreur')

        return render(request, "agent/identification_reussi.html",{'client':client})




    return render(request, "agent/identification_reussi.html",{'client':client})
