"""Auth's urls."""
from django.urls import include, path

from rest_framework import routers

from users import views
from users.views import ExtendedUserRecordView

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("extended_user/", ExtendedUserRecordView.as_view())
]
