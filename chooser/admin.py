# -*- coding: utf-8 -*-
from django.db.models import F
from django.contrib import admin

from chooser.models import Game, Play


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_plays', 'total_rejects', 'is_digital', 'is_real', 'is_playable_two_players']
    search_fields = ['title']
    list_filter = ['is_real', 'is_digital', 'is_playable_two_players', 'is_excluded']


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mode', 'played_at']
    list_filter = ['mode']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            f = 'total_rejects' if obj.mode == 'REJECTED' else 'total_plays'
            data = {f: F(f) + 1}
            Game.objects.filter(pk=obj.game_id).update(**data)
        return super(PlayAdmin, self).save_model(request, obj, form, change)
