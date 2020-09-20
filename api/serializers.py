"""API's serializers."""
from api.models import Post, Like

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Serializes post's model."""

    author_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Defining metadata for post's model serializer."""

        model = Post
        fields = [
            "id",
            "content",
            "creation_date",
            "author_name",
            "liked_by_users"
        ]

    @staticmethod
    def get_author_name(obj):
        """Represent author's name as just name instead of user's object."""
        return obj.author.username


class LikeSerializer(serializers.ModelSerializer):
    """Serializes like's model."""

    class Meta:
        """Defining metadata for like's model serializer."""

        model = Like
        fields = ["user", "post", "like_date"]


class PostAnalyticsSerializer(serializers.ModelSerializer):
    """Serializes Like analytics."""
    like_date = serializers.DateField()
    total_likes = serializers.IntegerField()

    class Meta:
        """Defining metadata for like's analytics serializer."""
        model = Post
        fields = ('like_date', 'total_likes')
