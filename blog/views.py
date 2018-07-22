from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """A View to display a list of posts."""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page.
    page = request.GET.get('page')  # Indicates current page number.
    try:
        posts = paginator.page(page)  # Obtain objects for the desired page.
    except PageNotAnInteger:
        #  If page is not an integer deliver the first page.
        posts = paginator.page(1)
    except EmptyPage:
        #  If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    """A View to display a single post."""
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
