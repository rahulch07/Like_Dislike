from django.urls import path
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', views.index, name='index'),
     path('like_dislike/', views.like_dislike, name='like_dislike'),
]

#urlpatterns += staticfiles_urlpatterns()