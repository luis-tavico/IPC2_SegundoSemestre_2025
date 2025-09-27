from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # 5 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/lista_posts.html', context)

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/detalle_post.html', context)

def sobre_nosotros(request):
    return render(request, 'blog/sobre_nosotros.html')

