from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view),
    path('about/',about_view),
    path('archieve/',archieve_view),
    path('add-post/',form_view),
    path('blog/<int:pk>/',content_view),
    path('tags/',tags_view),
    path('tags/<str:tag>',tag_post_view),
    path('projects/',project_view),
    path('talks/',talk_view)
]