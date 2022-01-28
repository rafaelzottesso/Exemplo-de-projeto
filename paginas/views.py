from django.views.generic import TemplateView
from cadastros.models import Cidade, Estado


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['cidades'] = Cidade.objects.all()

        cidade = Cidade()
        
        context['atributos'] = cidade.__dict__

        return context


class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'


