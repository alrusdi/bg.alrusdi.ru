# -*- coding: utf-8 -*-
import json
from django.views.generic import TemplateView
from chooser.common_views import JsonView
from chooser import helpers
from chooser.models import Game


class Index(TemplateView):
    template_name = "index.html"


class ChooseGame(JsonView):
    def get_context_data(self):

        return {
            'game': helpers.choose_new_game_to_play(self.request.POST)
        }


class RegisterPlay(JsonView):
    def get_context_data(self, **kwargs):
        return {
            'result': helpers.register_play(self.json_post.get('game_id'))
        }


class RejectPlay(JsonView):
    def get_context_data(self, **kwargs):
        return {
            'result': helpers.reject_play(self.json_post.get('game_id'))
        }


class GamesList(TemplateView):
    template_name = "games_list.html"

    def get_context_data(self):
        ctx = {
            "games": Game.objects.all()
        }
        return ctx
