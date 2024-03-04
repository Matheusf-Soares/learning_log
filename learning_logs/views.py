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

def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') # O sinal de menos ordena em ordem inversa
    context= {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)