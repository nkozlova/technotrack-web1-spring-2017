from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import CreateComment


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', login_required(CreateComment.as_view()), name="create_comment"),
]
