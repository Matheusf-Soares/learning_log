from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """Adiciona um tópico novo"""
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados POST enviados; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Exibe um formulário em branco ou inválido
    context = { 'form': form }
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adiciona uma entrada nova para um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if(request.method != 'POST'):
        # Nenhum dado enviado; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados POST enviados; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # Cria um entry sem salvar no banco
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # Exibe um formulário em branco ou inválido
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Requisição inicial; pré-preenche formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados POST enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
