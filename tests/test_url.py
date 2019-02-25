# from example.views import my_view
import pytest 
import factory_module
from example.models import User
import example


pytestmark=pytest.mark.django_db
@pytest.fixture(autouse=True)
def create_admin(client):
	User.objects.create_user(username='admin',password='testy123',is_active=1,is_superuser=1,is_staff=1)
	client.post('/example/login',{'username':'admin', 'password':'testy123'})

class TestUrl:
	pytestmark=pytest.mark.django_db
	def test_home(self,client):
		# request = rf.get('/customer/details')
		# response = my_view(request)
		response = client.get('/')
		assert response.status_code == 200
		assert "Click and Listen Music" in str(response.content)
		
	
	def test_login(self,client,create_admin):
		response=client.get('/example/')
		assert response.status_code==200

	def test_band(self,client):
		response = client.get('/example/bands')
		assert response.status_code == 200

	def test_album(self,client):
		factory_module.BandFactory()
		response = client.get('/example/album/Band1')
		assert response.status_code == 200

	def test_admin(self,client):
		response = client.get('/admin/')
		assert response.status_code == 200

	#  path('bands', views.bands, name='bands'),
	#     path('bands', views.index, name='add_band'),
	#     path('album/<str:band>', views.albums, name='albums'),
	#     path('album/<str:band>/all', views.all_songs, name='all_songs'),
	#     path('album/<str:band>/save_playlist', views.all_songs, name='save_playlist'),
	#     # path('song/<int:id>', views.songs, name='songs'),  #add song to playlist
	#     path('album/<str:band>/<str:album>', views.songs, name='songs'),
	#     path('my_favourite', views.my_favourite, name='my_favourite'),
	#     path('my_playlist', views.my_playlist, name='my_playlist'),
	#     path('my_playlist/<str:playlist>', views.playlist_songs, name='playlist_song'),
	#     path('login', views.logging, name='login'),
	# 	path('register', views.register, name='register'),
	#     path('logout',views.logout_view,name='logout'),