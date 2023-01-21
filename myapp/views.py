from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Like

#def index(request):
    #return render(request, 'index.html')

def like_dislike(request):
    like_dislike = Like.objects.first()
    if not like_dislike:
        like_dislike = Like.objects.create()

    if request.method == 'POST':
        if request.POST.get('like'):
            like_dislike.likes += 1
        elif request.POST.get('dislike'):
            like_dislike.dislike += 1

        like_dislike.save()

    return render(request, 'index.html',{'like_count': like_dislike.likes, 'dislike_count': like_dislike.dislike})
    #JsonResponse({'like_count': like_dislike.likes, 'dislike_count': like_dislike.dislike})
    #render(request, 'index.html',{'like_count': like_dislike.likes, 'dislike_count': like_dislike.dislike})