from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib import admin
from views import HomePageView, register


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
]
