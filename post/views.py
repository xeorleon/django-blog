from django.shortcuts import render, HttpResponse


# Create your views here.
def post_index(request):
    return HttpResponse('Post İndex Sayfası')


def post_detail(request):
    return HttpResponse('Post Detail Sayfası')


def post_create(request):
    return HttpResponse('Post Create Sayfası')


def post_update(request):
    return HttpResponse('Post Update Sayfası')


def post_delete(request):
    return HttpResponse('Post Delete Sayfası')
