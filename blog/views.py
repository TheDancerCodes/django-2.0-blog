from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm


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


class PostListView(ListView):
    """Class Based View to display the Post List objects."""

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    """The View that shares the Post via email."""
    # Retrieve post by ID
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post,
                                                        'form': form})
