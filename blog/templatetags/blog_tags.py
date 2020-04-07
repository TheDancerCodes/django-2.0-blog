from django import template
from django.db.models import Count

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

# A tag to display the most commented posts.
# A simple template tag that stores the result in a variable that can be reused
# rather than directly outputting it.
# Build a QuerySet using the annotate() function to aggregate the total number of comments
# for each post.
# Use the Count aggregation function to store the number of comments in the
# computed field total_comments for each Post object.
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
