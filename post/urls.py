from django.urls import path
from .views import *
urlpatterns = [
    path('index/', post_index),
    path('<int:id>', post_detail),
    path('create/', post_create),
    path('update/', post_update),
    path('delete/', post_delete)
]
