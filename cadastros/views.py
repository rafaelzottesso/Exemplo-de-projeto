from .models import Cidade, Estado

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estados'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Estado'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context


class EstadoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Estado
    template_name = 'cadastros/listas/estados.html'


#######################################


class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidades'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cidade'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context


class CidadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Cidade
    template_name = 'cadastros/listas/cidades.html'

#######################################
