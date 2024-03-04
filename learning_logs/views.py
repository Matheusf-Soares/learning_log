from django.shortcuts import render

from .models import Topic

def index(request):
    """A pátina inicial para o Registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    context= {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)