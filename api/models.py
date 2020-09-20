from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post's model."""
    content = models.TextField()
    creation_date = models.DateField(default=date.today())
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author')
    liked_by_users = models.ManyToManyField(User, through='Like')

    def __str__(self):
        return self.content[:20]


class Like(models.Model):
    """Like's through model."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_date = models.DateField(default=date.today())

    class Meta:
        unique_together = ('post', 'user')
        index_together = ('post', 'user')

    def __str__(self):
        str_repr = self.post.content[:20] + ' [' + self.user.username + ']'
        return str_repr
