from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


# Create your views here.
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request):
    post = get_object_or_404(Post, id=2)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    return HttpResponse('Post Create Sayfası')


def post_update(request):
    return HttpResponse('Post Update Sayfası')


def post_delete(request):
    return HttpResponse('Post Delete Sayfası')
