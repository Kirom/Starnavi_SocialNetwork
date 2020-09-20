"""Api's urls."""
from django.conf.urls import url

from api.views import PostViewSet, LikeViewSet, AnalyticsViewSet

from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("likes", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    url('^(?P<dates>[\w\-]+)/$', AnalyticsViewSet.as_view())
]
