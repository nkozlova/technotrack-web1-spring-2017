from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import BlogList, BlogView, PostView, CreateBlog, UpdateBlog, CreatePost, CreateCategory, UpdatePost, \
    CategoryView, CreatePostInBlog


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^new/$', login_required(CreateBlog.as_view()), name="create_blog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="edit_blog"),

    url(r'^(?P<pk>\d+)/new/$', login_required(CreatePostInBlog.as_view()), name="create_post_in_blog"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
    url(r'^post/new/$', login_required(CreatePost.as_view()), name="create_post"),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="edit_post"),

    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^category/new/$', login_required(CreateCategory.as_view()), name="create_category"),
]
