from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import movie
from. forms import movieform
# Create your views here.
def index(request):
    movieobj=movie.objects.all()
    content={ 'movie_list':movieobj}
    return render(request,'index.html',content)
def detail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'moviel':m})
def add_movie(request):
    if request.method=="POST":
        name1=request.POST.get('name',)
        desc1=request.POST.get('desc',)
        year1=request.POST.get('year',)
        img1=request.FILES['img']
        movie1=movie(name=name1,desc=desc1,year=year1,img=img1)
        movie1.save()
    return render(request,'add.html')
def update(request,id):
    movie1=movie.objects.get(id=id)
    formv=movieform(request.POST or None,request.FILES,instance=movie1)
    if formv.is_valid():
        formv.save()
        return redirect('/')
    return render(request,'edit.html',{'form':formv,'movie':movie1})
def delete(request,id):
    if request.method=="POST":
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')