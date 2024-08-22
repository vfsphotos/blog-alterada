from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    class Meta:
        db_table = 'authors'