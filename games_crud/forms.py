from django import forms
from .models import VideoGame, Publisher


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = ['title', 'description', 'publisher']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', ]
