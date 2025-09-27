from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})