from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Band(models.Model):
	band=models.CharField(max_length=60)
	year=models.IntegerField()
	team=models.CharField(max_length=120)
	image=models.ImageField(default='default.png',blank=True)

	def __str__(self):
		return str(self.band)

class Album(models.Model):
    band=models.ForeignKey(Band, related_name='albums', on_delete=models.CASCADE)
    album=models.CharField(max_length=60)
    year=models.IntegerField()
    image=models.ImageField(default='default.jpg',blank=True)

    def __str__(self):
        return str(self.album)

# FUNKCJA ZMiANY FOLDERU DO UPLOADU
def update_filename(instance, filename):
	band = instance.band
	album = instance.album
	song = instance.song
	path = "{}/{}".format(str(band),str(album))
	return os.path.join(path,str(song))

class Song(models.Model):
	album=models.ForeignKey(Album, on_delete=models.CASCADE)
	band=models.ForeignKey(Band, on_delete=models.CASCADE)
	song=models.CharField(max_length=60)
	mp3=models.FileField(upload_to=update_filename) #Funkcja zmiany folderu do uploadu
	def __str__(self):
		return str(self.song)

class BandFavourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	band=models.ForeignKey(Band, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.band)


class Playlist(models.Model):
	user=models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	active=models.IntegerField(default=1)
	def __str__(self):
		return str(self.title)

class Playlist_song(models.Model):
	song=models.ForeignKey(Song, on_delete=models.CASCADE)
	playlist=models.ForeignKey(Playlist, on_delete=models.CASCADE)
	def __str__(self):
		return self.song_id

class Notification(models.Model):
	text=models.CharField(max_length=100)
	type=models.CharField(max_length=100,default='')

# kazdy typ do innej tabeli powiadomien
class Notifications_share(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	notification=models.ForeignKey(Notification, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	active=models.IntegerField(default=1)

