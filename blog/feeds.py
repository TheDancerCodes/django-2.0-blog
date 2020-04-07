from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    # items() method retrieves the objects to be included in the feed.
    # Retrieving only the last five published posts for this feed.
    def items(self):
        return Post.published.all()[:5]

    # The item_title() and item_description() methods receive each object returned by items()
    # and return the title and description for each item.
    # We use the truncatewords built-in template filter to build the description of the
    # blog post with the first 30 words.
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
