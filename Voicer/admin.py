from django.contrib import admin
from .models import Anime, Tournament, UserVotes

admin.site.register(Anime)
admin.site.register(Tournament)
admin.site.register(UserVotes)