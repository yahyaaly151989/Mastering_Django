from django.shortcuts import render,  get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
                                Post, 
                                status=Post.Status.PUBLISHED, 
                                slug=post,
                                publish__year=year, 
                                publish__month=month, 
                                publish__day=day
                            )
    return render(request, 'blog/post/detail.html', {'post': post})