from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, CommentForm
from .models import Post


# Create your views here.
def post_index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 4)  # Show 5 posts per page.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Yorumunuz Başarılı bir şekilde eklendi')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        raise Http404()
    # if request.method == 'POST':
    #    print(request.POST)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title, content=content)

    # if request.method == 'POST':
    # Formdan gelen bilgileri kaydet
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    # else:
    # Formu kullanıcıya göster
    #    form = PostForm()

    # Refactor
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        raise Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz.', extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        raise Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Başarılı bir şekilde sildiniz.')
    return redirect('post:index')
