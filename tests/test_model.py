from example.models import User,Band,Album
import factory_module
import pytest

	

# metoda autouse, tworzy factory w każdej metodzie testowej
pytestmark=pytest.mark.django_db
@pytest.fixture(autouse=True)
def create(request):
	factory_module.UserFactory()
	factory_module.BandFactory()
	factory_module.AlbumFactory()

class Testmodel(object):
	pytestmark=pytest.mark.django_db
	# def setup_method(self,methods): #metoda setup na początku
	# 	factory_module.UserFactory()
	# 	factory_module.BandFactory()
	# 	factory_module.AlbumFactory()  
	@pytest.fixture()
	def user(self):
		user=User.objects.get(username='admin')
		return user

	@pytest.fixture()
	def band(self):
		band=Band.objects.get(band='Band1')
		return band

	@pytest.fixture()
	def album(self):
		album=Album.objects.get(band__band='Band1')
		return album
	
	def test_simple(self,user):
		assert user.username=="admin"
	def test_model(self,user):
		assert user.username=="admin"
	def test_band_album(self,album):
		assert album.album=="Album1"