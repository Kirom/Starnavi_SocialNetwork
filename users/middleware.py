from django.utils import timezone

from users.models import ExtendedUser


class UpdateLastActivityMiddleware:
    """Middleware that updates extended_user model (last_activity field)."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request,
                       'user'), 'The UpdateLastActivityMiddleware requires ' \
                                'authentication middleware to be installed.'
        if request.user.is_authenticated:
            ExtendedUser.objects.filter(user__id=request.user.id) \
                .update(last_activity=timezone.now())
