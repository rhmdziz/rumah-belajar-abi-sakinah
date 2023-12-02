from django.shortcuts import render, get_object_or_404, redirect

from .models import *

def index(request):
    testi = Testimoni.objects.all()
    teacher = Teacher.objects.all()
    gallery = Gallery.objects.all()
    blog = Blog.objects.all()

    context = {
        'testi': testi,
        'teacher': teacher,
        'gallery': gallery,
        'blog': blog,
    }

    return render(request, "index.html", context)

def galleryView(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery,
    }

    return render(request, "gallery.html", context)

def blogViews(request, id):
    blog = get_object_or_404(Blog, pk=id)
    context = {
        'blog': blog,
    }
    return render(request, "blog.html", context)


