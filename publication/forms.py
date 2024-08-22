from django import forms

from publication.models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['pub_title', 'pub_text', 'pub_image']