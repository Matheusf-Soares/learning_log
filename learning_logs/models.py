from django.db import models

# Create your models here.

class Topic(models.Model):
    """Um tópico que o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma representação de string do modelo"""
        return self.text
    
class Entry(models.Model):
    """Algo específico aprendido sobre um tópico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna uma string simples representando a entrada"""
        return f'{self.text[:50]}'