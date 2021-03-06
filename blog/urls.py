from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # Post Views
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    # URL Pattern to list posts by tag
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # Instantiate the feed
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # URL pattern to perform search
    path('search/', views.post_search, name='post_search')
]
