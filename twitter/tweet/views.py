from django.shortcuts import render,redirect
from .models import tweet

# Create your views here.
def index(request):
    tweets = tweet.objects.all().filter().order_by('-id')
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('body') :
            post = tweet()
            post.name = request.POST.get('name')
            post.body = request.POST.get('body')
            post.save()


    return render(request,'index.html',{'tweets':tweets})

def delete(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            print(request.POST.get('id'))
            tweet_obj=tweet.objects.get(id=request.POST.get('id')) 
            tweet_obj.delete()

    return redirect('/')
        

def add(request):
    if request.method=='POST':
        print(request.FILES.get('tweet_image'))
        tweet_obj=tweet(username='anything',name='ramaun',tweet_text=request.POST.get('tweet_text'),
         tweet_img=request.FILES.get('tweet_image'))
        tweet_obj.save()
    return redirect('/')


def edit(request,id):
    if request.method=='GET':
        tweet_obj=tweet.objects.get(id=id)
        return render(request,'edit-tweet.html',{'tweet':tweet_obj})

def update(request):
    if request.method=='POST':
        id=request.POST.get('id')
        text=request.POST.get('tweet_text')
        tweet_obj=tweet.objects.get(id=id)
        tweet_obj.tweet_text=text
        tweet_obj.save()
        return redirect('/')
