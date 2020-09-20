"""Auth's views."""
from django.contrib.auth.models import Group, User

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import ExtendedUser
from users.serializers import ExtendedUserSerializer, GroupSerializer, \
    UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ExtendedUserRecordView(APIView):
    """A class based view for creating and fetching extended_user records."""

    def get(self, request, format=None):
        """
        Get all the extended_user records.
        :param format: Format of the extended_user records to return to
        :return: Returns a list of extended_user records
        """
        context = {'request': request}
        queryset = ExtendedUser.objects.all()
        serializer = ExtendedUserSerializer(queryset,
                                            context=context,
                                            many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a extended_user record.
        :param format: Format of the extended_user records to return to
        :param request: Request object for creating extended_user
        :return: Returns a extended_user record
        """
        serializer = ExtendedUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)
