from django.contrib import admin
from .models import Game_type, Game, User_games, Image

# Register your models here.


class Useradmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'password', 'first_name', 'last_name', 'email'
    ]


admin.site.register(Game_type)
admin.site.register(Game)
admin.site.register(User_games)
admin.site.register(Image)
