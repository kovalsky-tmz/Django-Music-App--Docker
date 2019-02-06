from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='example'
urlpatterns = [
    path('', views.index, name='index'),
    path('bands', views.bands, name='bands'),
    path('bands', views.index, name='add_band'),
    path('album/<str:band>', views.albums, name='albums'),
    path('album/<str:band>/all', views.all_songs, name='all_songs'),
    path('album/<str:band>/save_playlist', views.all_songs, name='save_playlist'),
    # path('song/<int:id>', views.songs, name='songs'),  #add song to playlist
    path('album/<str:band>/<str:album>', views.songs, name='songs'),
    path('my_favourite', views.my_favourite, name='my_favourite'),
    path('my_playlist', views.my_playlist, name='my_playlist'),
    path('my_playlist/<str:playlist>', views.playlist_songs, name='playlist_song'),
    path('login', views.logging, name='login'),
	path('register', views.register, name='register'),
    path('logout',views.logout_view,name='logout'),


    path('ajax_song_to_playlist',views.ajax_add_song_playlist,name='ajax-song-playlist'),
    # path('ajaxbands', views.ajaxbands, name='ajaxbands'),
    path('ajaxaddfavouritesband', views.ajax_add_favourites, name='ajaxfavourites'),
	path('ajaxshareplaylist', views.ajax_share_playlist, name='ajaxshare'),
    # path('ajaxalbum/<str:band>', views.ajaxalbums, name='ajaxalbums'),
    # path('ajaxalbum/<str:band>/<str:album>', views.ajaxsongs, name='ajaxsongs'),
    path('ajaxcreateplaylist', views.ajaxcreateplaylist, name='ajaxcreateplaylist'),
]