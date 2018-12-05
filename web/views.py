from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from web.forms import EmpleadoForm, RegistroForm


def vista_inicio(request):
    return render(request, "inicio.html")


class vista_registrar(CreateView):
    model = User
    template_name = 'registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('inicio')


def vista_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})
