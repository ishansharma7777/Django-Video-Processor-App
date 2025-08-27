from django import forms
from .models import VideoUpload

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields =  ['video','title']
