from django.urls import path
from .views import*
from .views import delete_user, accept_user,pause_client

urlpatterns = [
   path('controle/', controle, name="control"),
   path('log', login_admin, name="log"),
   path('index2', index2_admin, name="index2_admin"),
   path('pause', pause_client, name="pause_client"),
   path('inscrit', inscrit_client, name="inscrit_client"),
   #path('users/', user_list, name='user_list'),
   path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
   path('users/accept/<int:user_id>/', accept_user, name='accept_user'),
   path('pause_details/<int:id>/', pause_details, name="pause_details"),
   path('inscrit_details/<str:id>/', inscrit_details, name="inscrit_details"),
   path('accepter/<int:id>/',accepter, name="accepter"),
   path('refuser/<int:id>/',refuser,name="refuser"),
   path('comptable',comptable_log, name="comptable_log"),
   path('logouts', mylogout, name='logouts'),
   path('agent', myagent, name='agents'),
   path('agent_register', agent_register, name='agents_register'),
   path('suivant', agent_suivant, name='suiv'),
   path('liste_client', liste, name="list_clients"),
   path('agent_details/<str:id>/', agent_detail, name="agent_details"),
   path('news/<str:id>/',new_assign,name="new_assign"),
   path('finance', finance_agent, name="finance_agent"),
   path('finance_login', login_agent, name= "login_agent" ),
   path('agent_connect', agent_connection, name="agent_connection" ),
   path('agent_logout', agentlogout, name="agentlogout"),
   path('agent_identifs', agent_identification, name="agent_identification"),
   path('identificationreussi/<str:id>/', identif_reussi, name="identif_reussi")
]