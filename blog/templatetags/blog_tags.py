from django import template
from ..models import Post

register = template.Library()


# A simple template tag that returns no. of posts published.
@register.simple_tag
def total_posts():
    return Post.published.count()

# An inclusion tag to display the latest posts in the sidebar of our blog.
# We render a template with context variables returned by the template tag.
# Specify the template that has to be rendered with the returned values
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
