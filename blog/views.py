from django.shortcuts import render, get_object_or_404
from .models import Blog



def allblogs(request):
    blogs = Blog.objects.order_by('-pub_date')                      # Order by ref: https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})