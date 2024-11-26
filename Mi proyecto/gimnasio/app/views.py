from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from .forms import ContactoForm, PlanForm
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioRegistroForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def informacion(request):
    return render(request, 'app/informacion.html')

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje']='Contacto guardado correctamente'
        else:
            data['form'] = formulario

    return render(request, 'app/contacto.html', data)

def planes(request):
    planes = Plan.objects.all()
    data = {
        'planes': planes
    }
    return render(request, 'app/planes.html', data)


def agregar_plan(request):
    data = {
        'form': PlanForm()
        }   
    if request.method == 'POST':
        formulario = PlanForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje']='Plan agregado correctamente'
            return redirect(to='planes')
        else:
            data['form'] = formulario
    return render(request, 'app/planes/agregar.html',data)


def listar_planes(request):
    planes = Plan.objects.all()
    data = {
        'planes': planes
        }
    return render(request, 'app/planes/listar.html', data)


def modificar_plan(request, id):
    plan = get_object_or_404(Plan, pk=id)  
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_planes')
    else:
        form = PlanForm(instance=plan)  
    
    return render(request, 'app/planes/modificar.html', {'form': form})

def eliminar_plan(request,id):
    plan = get_object_or_404(Plan, pk=id)
    plan.delete()
    return redirect(to='listar_planes')

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            password = form.cleaned_data['password']
            tipo_usuario = form.cleaned_data['tipo_usuario'] 
            usuario = Usuario.objects.create_user(
                email=email, 
                nombre=nombre, 
                password=password, 
                tipo_usuario=tipo_usuario
            )

            login(request, usuario)
            return redirect(to='home')
        else:
            print(form.errors)  
            messages.error(request, "Hubo un problema al registrar el usuario.")
    else:
        form = UsuarioRegistroForm()

    return render(request, 'registration/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(to='home')  
        else:
            messages.error(request, "Credenciales incorrectas.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


