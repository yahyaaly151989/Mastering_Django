from django import forms
from .models import Image
from django.utils.text import slugify
import requests
from django.core.files.base import ContentFile

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'desciption']
        widgets = {
            'url': forms.HiddenInput
        }
        
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', '.jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        
        if extension not in valid_extensions:
            raise forms.ValidationError("The given URL doesnot match a valid image extension.")
        
        return url
        
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f"{name}.{extension}"
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        
        if commit:
            image.save()
        return image
        
        
        
