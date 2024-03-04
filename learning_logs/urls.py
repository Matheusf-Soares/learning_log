"""Define padrões de URL para learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Página que mostra todos os tópicos
    path('topics/', views.topics, name='topics'),
    # Página de detalhes para um único tópico
    path('topics/<int:topic_id>/', views.topic, name='topic')
]