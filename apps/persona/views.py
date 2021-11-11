from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required
from apps.persona.forms import CuentaForm
from apps.persona.models import Persona

# Create your views here.
#solicitamos que tenga el permiso de agregar cuenta
@permission_required('persona.add_cuentabancaria',raise_exception=True)
#Creamos la vista con la logica para crear una cuenta
def crear_cuentaBancaria(request):
    nueva_cuenta = None
    if request.method == 'POST':
        cuenta_form = CuentaForm(request.POST, request.FILES)
        if cuenta_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_cuenta = cuenta_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente una nueva Cuenta {}'.format(nueva_cuenta))
            return redirect(reverse('persona:listaPersona'))
    else:
        cuenta_form = CuentaForm()

    return render(request, 'persona/crecuenta.html',
                  {'form': cuenta_form})
#Validacion de Login
@login_required
#lista de personas ordenados por su dni
def persona_lista(request):
    #Hacemos una consulta con todos los registro de persona y las ordenamos de forma ascendente con respecto a dni
    personas = Persona.objects.all().order_by('dni')
    return render(request, 'persona/listaPersona.html',
                  {'personas': personas})    