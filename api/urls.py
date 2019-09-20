from django.conf.urls import url, include
from .views import CreateView
from .views import DetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^bucketlistapi/$', CreateView.as_view(), name="create"),
    url(r'^bucketlistapi/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)