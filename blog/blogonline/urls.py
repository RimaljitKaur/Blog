from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view),
    path('add-post/',form_view),
    path('blog/<int:pk>/',content_view)
]