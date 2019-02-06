from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer,BandSerializer,PlaylistSerializer
from rest_framework import permissions
from example.models import Band,Playlist

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class BandViewSet(viewsets.ModelViewSet):

    queryset = Band.objects.all().order_by('band')
    serializer_class = BandSerializer

class PlaylistViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer
    def get_queryset(self):
        queryset = super(PlaylistViewSet, self).get_queryset()
        user = self.request.user
        return queryset.filter(user=user)
