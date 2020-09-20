from rest_framework import generics

from api.models import Post, Like
from api.serializers import PostSerializer, LikeSerializer, \
    PostAnalyticsSerializer
from api.services.additional_funcs import update_extended_user

from django.db import IntegrityError

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import ExtendedUser


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""

    queryset = Post.objects.select_related("author")
    serializer_class = PostSerializer

    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def like_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            user = request.user
            """Updates extended_user model (last_activity field)."""
            update_extended_user(self, ExtendedUser)
        try:
            like = Like.objects.create(post=post, user=user)
            serializer = LikeSerializer(like, many=False)
            response = {'message': 'Post liked!', 'result': serializer.data}
            return Response(response)
        except IntegrityError as exc:
            if 'UNIQUE' in str(exc):
                response = {'message': 'You already liked this post!'}
                return Response(response)
        return Response({'message': 'Something goes wrong'})

    @action(methods=['POST'], detail=True)
    def unlike_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            user = request.user
            """Updates extended_user model (last_activity field)."""
            update_extended_user(self, ExtendedUser)
        try:
            Like.objects.filter(post=post, user=user).delete()
            response = {'message': 'Post is not liked now!'}
            return Response(response)
        except IntegrityError as exc:
            if 'UNIQUE' in str(exc):
                response = {'message': 'You did not like this post!'}
                return Response(response)
        return Response({'message': 'Something goes wrong'})

    def perform_create(self, serializer):
        """Create posts by current user authenticated via JWT
         and updates extended_user model (last_activity field)."""
        serializer.save(author=self.request.user)
        update_extended_user(self, ExtendedUser)

    def retrieve(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(PostViewSet, self).retrieve(request)

    def list(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(PostViewSet, self).list(request)

    def update(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(PostViewSet, self).update(request)

    def partial_update(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(PostViewSet, self).partial_update(request)

    def destroy(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(PostViewSet, self).destroy(request)


class LikeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""

    queryset = Like.objects.select_related("user")
    serializer_class = LikeSerializer

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create likes by current user authenticated via JWT
        and updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        serializer.save(user_id=self.request.user.pk,
                        post_id=self.request.data['post_id'])

    def retrieve(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(LikeViewSet, self).retrieve(request)

    def list(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(LikeViewSet, self).list(request)

    def update(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(LikeViewSet, self).update(request)

    def partial_update(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(LikeViewSet, self).partial_update(request)

    def destroy(self, request, *args, **kwargs):
        """Updates extended_user model (last_activity field)."""
        update_extended_user(self, ExtendedUser)
        return super(LikeViewSet, self).destroy(request)


class AnalyticsViewSet(generics.ListAPIView):
    """API endpoint for likes per day analytics."""
    serializer_class = PostAnalyticsSerializer

    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('date_from')
        end_date = self.request.query_params.get('date_to')

        likes_analytic = Like.objects.raw(
            "SELECT id, like_date AS day, COUNT(*) AS total_likes "
            "FROM api_like "
            "WHERE day BETWEEN %s and %s"
            "GROUP BY day;", [start_date, end_date]
        )
        context = []
        for row in likes_analytic:
            tmp = {'day': row.day, 'total_likes': row.total_likes}
            context.append(tmp)
        return Response(context)
