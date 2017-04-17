from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from views import BlogList, BlogView, PostView, CreateBlog, UpdateBlog, CreatePost, CreateCategory, UpdatePost, \
    CategoryView, CreatePostInBlog, PostCommentsView, PostLikeCountView, likes_add


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^new/$', login_required(CreateBlog.as_view()), name="create_blog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="edit_blog"),

    url(r'^(?P<pk>\d+)/new/$', login_required(CreatePostInBlog.as_view()), name="create_post_in_blog"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
    url(r'^post/(?P<pk>\d+)/comments/$', PostCommentsView.as_view(), name="post_comments"),
    url(r'^post/new/$', login_required(CreatePost.as_view()), name="create_post"),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="edit_post"),
    url(r'^post/(?P<pk>\d+)/likes/$', csrf_exempt(PostLikeCountView.as_view()), name="post_likes"),
    url(r'^post/(?P<pk>\d+)/likes/add/$', likes_add, name="post_new_like"),

    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^category/new/$', login_required(CreateCategory.as_view()), name="create_category"),
]
