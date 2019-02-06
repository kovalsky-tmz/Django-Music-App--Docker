from django.contrib.auth.models import User, Group
from rest_framework import serializers
from example.models import Band,Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
	playlists =serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username','password', 'email', 'groups','playlists','id')

class BandSerializer(serializers.HyperlinkedModelSerializer):
	albums =serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Band
		fields = ('band', 'year','image', 'id', 'albums')

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Playlist
		fields = ('user', 'title', 'id')
	