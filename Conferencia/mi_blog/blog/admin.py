from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_creacion']
    list_filter = ['fecha_creacion', 'autor']
    search_fields = ['titulo', 'contenido']