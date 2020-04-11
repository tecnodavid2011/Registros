from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import tablaregistros, tablaaulas
from .forms import formulario, formaula

# Create your views here.

#def inicioview(request):
#    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
    
class inicioview(CreateView,ListView):
    model = tablaregistros
    template_name = 'index.html'
    form_class = formulario
    success_url = reverse_lazy('index')

class aulatabla(CreateView, ListView):
    model = tablaaulas
    template_name = 'aulas.html'
    form_class = formaula
    success_url = reverse_lazy('aula')


class inicioedit(UpdateView):
    model = tablaregistros
    template_name = 'indexedit.html'
    form_class = formulario
    success_url = reverse_lazy('index')


#def inicioedit(request, id):
#    regedit = tablaregistros.objects.get(id = id)
#    if request.method == 'GET':
#        form = formulario(instance=regedit)
#    else:
#        form = formulario(request.POST, instance=regedit)
#        if form.is_valid():
#            form.save()
#        return redirect('http://localhost:8000/inicioedit/indexedit.html')
#    return render(request, 'index.html', {'form': form})
    