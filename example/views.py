from django.shortcuts import render,redirect,get_object_or_404
from .models import Album,Song,User,Band,BandFavourite,Playlist,Playlist_song,Notification
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import add_band,add_song_playlist,add_playlist,share_playlist,search_band
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test

# Create your views here.
#AJAX --------------------------
@login_required(login_url='/example/login')
def ajaxcreateplaylist(request):

	playlist_name=request.GET.get('playlist_name')
	if(Playlist.objects.filter(title=playlist_name).count() > 0):
		message={"class":'bg-success','text':"Playlist already exists."}
		return JsonResponse(message)
	else:
		Playlist.objects.create(title=playlist_name,user_id=request.user.id)
		message={"class":'bg-success','text':"Playlist created."}
		return JsonResponse(message)

# @login_required(login_url='/example/login')
# def ajaxbands(request):
# 	form_search=search_band(request.GET)
# 	bands=Band.objects.all()
# 	return render(request,"example/ajax/bands.html",{'bands':bands,'form_search':form_search})

# @login_required(login_url='/example/login')
# def ajaxalbums(request,band):
# 	albums=Album.objects.filter(band__band=band)
# 	band=Band.objects.get(band=band)
# 	# html = render_to_string("example/albums.html",{'albums':albums, 'band':band})
# 	return render(request,"example/ajax/albums.html",{'albums':albums, 'band':band})

# @login_required(login_url='/example/login')
# def ajaxsongs(request,band,album): #add song to playlist
# 	album=Album.objects.get(album=album)	
# 	songs=Song.objects.filter(album_id=album.id)
# 	# album=Album.objects.filter(id=id)[0]
# 	playlists=Playlist.objects.filter(user_id=request.user.id)
# 	return render(request,"ajax/songs.html",{'songs':songs,'band':band,'album':album.album,'playlists':playlists})

@login_required(login_url='/example/login')
def ajax_add_song_playlist(request):
	song_id=request.GET.get('song_id')
	playlist_id=request.GET.get('playlist_id')

	try:
		song_exists=Playlist_song.objects.get(playlist_id=playlist_id,song_id=song_id)

		message={"class":'bg-warning','text':"Song already exist."}
		return JsonResponse(message)
	except Playlist_song.DoesNotExist:
		song_exists = None
		Playlist_song.objects.create(song_id=song_id, playlist_id=playlist_id )
		message={"class":'bg-success','text':"Song added."}
		return JsonResponse(message)

@login_required(login_url='/example/login')
def ajax_add_favourites(request):
	band_name=request.POST.get('band_name')

	if not BandFavourite.objects.filter(user__id=request.user.id, band_id=band_name):
		user_id=User.objects.get(id=request.user.id)
		b=BandFavourite.objects.create(band_id=band_name,user_id=request.user.id )
		message={"class":'bg-success','text':"Band added to your favourites!."}
		return JsonResponse(message)
	else:
		message={"class":'bg-warning','text':"Band is already in your favourites."}
		return JsonResponse(message)

@login_required(login_url='/example/login')
def ajax_share_playlist(request):
	playlist_title_modal=request.POST.get('playlist_title_modal')
	user_id_modal=request.POST.get('user_id_modal')
	print(playlist_title_modal)
	print(playlist_title_modal)
	try:
		Playlist.objects.get(title=playlist_title_modal,user_id=user_id_modal,active=1)
		message={"class":'bg-warning','text':"Band is already in your favourites."}
		return JsonResponse(message)
	except Playlist.DoesNotExist:
		r=Playlist.objects.create(title=playlist_title_modal,user_id=user_id_modal,active=1)
		songs=Playlist_song.objects.filter(playlist__title=playlist_title_modal)
		for song in songs:
			Playlist_song.objects.create(playlist_id=r.id,song_id=song.song.id)
		message={"class":'bg-success','text':"Band added to your favourites!."}
		return JsonResponse(message)

def role_check(user):
	return user.is_staff==1
#  AJAX END--------------------------- 

# @user_passes_test(role_check,login_url='/example/') #if false redirect to /example
@login_required(login_url='/example/login')
def index(request):
	return render(request,"index.html",{'bands':bands})

@login_required(login_url='/example/login')
def bands(request):
	form_search=search_band(request.GET)
	if request.method=='POST':
		form=add_band(request.POST)
		if form.is_valid():
			band_name=form.cleaned_data['band_name']
			if not BandFavourite.objects.filter(user__id=request.user.id, band_id=band_name):
				user_id=User.objects.get(id=request.user.id)
				b=BandFavourite.objects.create(band_id=band_name,user_id=request.user.id )
				messages.add_message(request, messages.SUCCESS, 'Band was added to your favourites.')
				return redirect('/example/bands')
			else:
				messages.add_message(request, messages.WARNING, 'Band is already exists.')
				return redirect('/example/bands')
	if request.method=='GET':
		if form_search.is_valid():
			search_phrase=form_search.cleaned_data['search_phrase']
			bands=Band.objects.filter(band__contains=search_phrase)
			return render(request,"example/bands.html",{'bands':bands,'form_search':form_search})
	bands=Band.objects.all()

	return render(request,"example/bands.html",{'bands':bands,'form_search':form_search})

@login_required(login_url='/example/login')
def albums(request,band):
	albums=Album.objects.filter(band__band=band)
	band=Band.objects.get(band=band)
	# html = render_to_string("example/albums.html",{'albums':albums, 'band':band})
	return render(request,"example/albums.html",{'albums':albums, 'band':band})


	
@login_required(login_url='/example/login')
def songs(request,band,album): #add song to playlist

	album=Album.objects.get(album=album)	
	songs=Song.objects.filter(album_id=album.id)
	# album=Album.objects.filter(id=id)[0]
	playlists=Playlist.objects.filter(user_id=request.user.id)

	return render(request,"songs.html",{'songs':songs,'band':band,'album':album.album,'playlists':playlists})

@login_required(login_url='/example/login')
def all_songs(request,band):
	all_songs=Song.objects.filter(band__band=band)
	playlists=Playlist.objects.filter(user_id=request.user.id)
	return render(request,"songs.html",{'songs':all_songs,'band':band,'playlists':playlists})

@login_required(login_url='/example/login')
def my_favourite(request):
	if request.user.id!=None:
		bands=Band.objects.filter(bandfavourite__user_id=request.user.id)
		return render(request,"bands.html",{'bands':bands})
	else:
		return render(request,"bands.html",{'bands':None})

@login_required(login_url='/example/login')
def my_playlist(request):
	if request.method=="POST":
		form=share_playlist(request.POST)
		if form.is_valid():
			playlist_title=form.cleaned_data['playlist_title_modal']
			user_id_modal=form.cleaned_data['user_id_modal']	
			# try:
			# 	Notification.objects.create(text="",type='sharing') # jeśli jeszcze nie ma
			# 	#create powiadomienia
			try:
				Playlist.objects.get(title=playlist_title,user_id=user_id_modal,active=1)
				messages.error(request, 'Playlist already exists!.')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			except Playlist.DoesNotExist:
				r=Playlist.objects.create(title=playlist_title,user_id=user_id_modal,active=1)
				songs=Playlist_song.objects.filter(playlist__title=playlist_title)
				for song in songs:
					Playlist_song.objects.create(playlist_id=r.id,song_id=song.song.id)
				messages.success(request, 'Playlist shared!.')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	if request.method=="GET":
		form=add_playlist(request.GET)
		if form.is_valid():
			playlist_name=form.cleaned_data['playlist_name']
			if(Playlist.objects.filter(title=playlist_name).count() > 0):
				messages.error(request, 'Playlist already exists!.')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			else:
				Playlist.objects.create(title=playlist_name,user_id=request.user.id)
				messages.success(request, 'Playlist added!.')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	playlists=Playlist.objects.filter(user_id=request.user.id)
	users=User.objects.all()
	return render(request,"my_playlist.html",{'playlists':playlists,'users':users})

@login_required(login_url='/example/login')
def playlist_songs(request,playlist):
	playlist=Playlist.objects.get(title=playlist,user_id=request.user.id)
	songs=Song.objects.filter(playlist_song__playlist_id=playlist.id)
	return render(request,"songs.html",{'songs':songs, 'playlist':playlist.title})



def logging(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		user=authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect('/example')
		else:
			messages.error(request, 'Wrong login or password.')
			return redirect('/example/login')
	else:
		return render(request,"login.html")

def register(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password_reg"]
		try:
			user=User.objects.create_user(username=str(username),password=str(password))
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('/example')
			print(user)
		except:
			messages.warning(request, 'Username already exists')
			return redirect('/example/login')


def logout_view(request):
	logout(request)
	return redirect('/')

