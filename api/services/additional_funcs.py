from django.utils import timezone


def update_extended_user(self, user):
    if self.request.user.is_authenticated:
        user.objects.filter(user__id=self.request.user.id) \
            .update(last_activity=timezone.now())
