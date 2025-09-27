from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='blog-home'),
    path('post/<int:pk>/', views.detalle_post, name='post-detail'),
    path('sobre/', views.sobre_nosotros, name='blog-about'),
]