from django.urls import path
from .views import crear_cuentaBancaria, persona_lista 


app_name = 'persona'
urlpatterns = [
    path('cuenta/',crear_cuentaBancaria,name='crear_cuenta_bancaria'),
    path('lista/',persona_lista,name='listaPersona')
]
