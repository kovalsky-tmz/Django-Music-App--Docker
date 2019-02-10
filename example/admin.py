from django.contrib import admin
from .models import Album,Song,Band,BandFavourite,Playlist
import os
from .forms import BandForm,SongForm
from django.contrib import messages
from django.urls import path
import csv
from django.http import HttpResponseRedirect


# Register your models here.
# admin.site.register(Band)

# KLASA POTRZEBNA DO UTWORZENIA ELEMENTOW W CHANGELIST VIEW PAGE
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"



# MULTIPLE ALBUM TO BAND
class AlbumInline(admin.TabularInline):
	model=Album
	show_change_link = True

class BandAdmin(admin.ModelAdmin,ExportCsvMixin):

	inlines=[AlbumInline]
	form = BandForm

	fieldsets = (
    	(None, {
        	'fields': ('band','year','team','image','extra_field'),
		}),
	)
	# rozszerzenie change_list admina. dodaje element
	change_list_template = "admin/update_band.html"

	# url z forma update_band
	def get_urls(self):
	    urls = super().get_urls()
	    my_urls = [
	        path('update_band/', self.update_band),
	    ]
	    return my_urls + urls


	def update_band(self, request):
		form = BandForm
		path=("media/")
		dirs = os.listdir(path)
		for file in dirs:
			if os.path.isdir(os.path.join('media/',file)):
				if not Band.objects.filter(band=file):
					Band.objects.create(band=file, year='2137')
					messages.add_message(request, messages.INFO, 'Album added :'+file)
					
				else:
					messages.add_message(request, messages.INFO, 'Already exists: '+file)
		return HttpResponseRedirect("../")
	    
	    
	def save_model(self, request, obj, form, change):
		if form.cleaned_data.get('extra_field'):
			obj.save()
			path=("media/"+form.cleaned_data.get('band'))
			dirs = os.listdir(path)
			for file in dirs:
				path_song=("media/"+form.cleaned_data.get('band')+"/"+file)
				dirs_song = os.listdir(path_song)
				if not obj.albums.filter(album=file):
					for song in dirs_song:
						if(song.endswith('.jpg')):
							imagee=os.path.join(path_song,song)
							break
						else:
							imagee="default.jpg"
							
							
					n=obj.albums.create(album=file, year='2137',image=imagee)
					for song in dirs_song:
						if 'mp3' in song:
							obj.song_set.create(album_id=Album.objects.get(album=file).id,song=song,mp3=str(obj.band)+"/"+file+"/"+song+".mp3")
					messages.add_message(request, messages.INFO, 'Album with songs added :'+file)
				else:
					messages.add_message(request, messages.INFO, 'Already exists: '+file)
		else:
			obj.save()



class SongInline(admin.TabularInline):
	model=Song
	

class AlbumAdmin(admin.ModelAdmin):
	inlines=[SongInline]
	form = SongForm

	fieldsets = (
    	(None, {
        	'fields': ('band','year','album','image','extra_field','file_field'),
		}),
	)

	def save_model(self, request, obj, form, change):
		obj.save()
		for afile in request.FILES.getlist('file_field'):
			obj.song_set.create(band=obj.band,song=afile,mp3=afile)
		if form.cleaned_data.get('extra_field'):
			obj.save()
			print(obj.band)
			path=("C:/Users/Tomasz/djangopro/media/"+str(obj.band)+"/"+form.cleaned_data.get('album'))
			dirs = os.listdir(path)
			for file in dirs:
				print (file)
				if not obj.song_set.filter(song=file):
					obj.song_set.create(band=obj.band,song=file,mp3=str(obj.band)+"/"+form.cleaned_data.get('album')+"/"+file+".mp3")
					messages.add_message(request, messages.INFO, 'Album added :'+file)
				else:
					messages.add_message(request, messages.INFO, 'Already exists: '+file)




admin.site.register(Band,BandAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)
# do konkretnego usera trzeba kiedys zrobic
admin.site.register(BandFavourite)
admin.site.register(Playlist)