from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):

    # The changefreq and priority attributes indicate the change frequency of your post pages
    # and their relevance in your website (the maximum value is 1).
    changefreq = 'weekly'
    priority = 0.9

    # items() method returns the QuerySet of objects to include in this sitemap.
    def items(self):
        return Post.published.all()

    # lastmod method receives each object returned by items() and
    # returns the last time the object was modified.
    def lastmod(self, obj):
        return obj.updated
