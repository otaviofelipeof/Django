from django.urls import path
 from . import views
# Importa as views da pasta atual 
urlpatterns = [ path('', views.home, name='home'), # Rota Vazia ]
