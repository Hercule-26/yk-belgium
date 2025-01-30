from django.shortcuts import render
from django.views.generic import TemplateView

class HomeViewFR(TemplateView):
    template_name = "appartements/index-fr.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['form'] = "put form here"
        return context    
    
class HomeViewNL(TemplateView):
    template_name = "appartements/index-nl.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['form'] = "put form here"
        return context    