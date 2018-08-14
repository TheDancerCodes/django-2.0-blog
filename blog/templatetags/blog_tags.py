from django import template
from ..models import Post

register = template.Library()


# A simple template tag that returns no. of posts published.
@register.simple_tag
def total_posts():
    return Post.published.count()
