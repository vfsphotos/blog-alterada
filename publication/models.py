from django.db import models
from author.models import Author
from tinymce.models import HTMLField

# Create your models here.
class Publication(models.Model):
    date_pub = models.DateTimeField(
        'publication date',
        auto_now_add=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    pub_text = HTMLField('publications')
    pub_title = models.CharField(
        'publication title',
        max_length=100
    )
    pub_image = models.ImageField(
        'publication image',
        upload_to='publications/',
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'publications'