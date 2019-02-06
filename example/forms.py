from django import forms
from .models import Album,Band,Song


# FORM WITH ADDITIONAL FIELD FOR BAND TO MASSIVE RECORDS
class BandForm(forms.ModelForm):
    extra_field = forms.BooleanField(label='Do you want to import albums and songs form folder?',required=False)
    def save(self, commit=True):
        extra_field = self.cleaned_data.get('extra_field', None)

        return super(BandForm, self).save(commit=commit)

    class Meta:
        model = Album
        fields = "__all__"


class SongForm(forms.ModelForm):
    extra_field = forms.BooleanField(label='Do you want to import songs from album folder?',required=False)
    file_field = forms.FileField(label='Upload files .mp3',required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Song
        fields='__all__'

class add_band(forms.Form):
	band_name=forms.CharField(max_length=100)

class add_song_playlist(forms.Form):
    playlist_id=forms.CharField(max_length=100)
    song_id=forms.CharField(max_length=100)

class add_playlist(forms.Form):
    playlist_name=forms.CharField(max_length=100)

class share_playlist(forms.Form):
    playlist_title_modal=forms.CharField(max_length=100)
    user_id_modal=forms.IntegerField()

class search_band(forms.Form):
    search_phrase=forms.CharField(label='Find band',max_length=100)