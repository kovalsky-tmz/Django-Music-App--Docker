import factory
from example.models import User,Band,Album
class UserFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = User
		django_get_or_create = ('username','password',)
	username = 'admin'
	password='testy123'
	
	
class BandFactory(factory.django.DjangoModelFactory):
	class Meta:
		model=Band
		django_get_or_create=('band','year',)
	band="Band1"
	year=1999

class AlbumFactory(factory.django.DjangoModelFactory):
	class Meta:
		model=Album
		django_get_or_create=('album','year',)
	album="Album1"
	year=1999
	band=factory.SubFactory(BandFactory)
