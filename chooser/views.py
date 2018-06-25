# -*- coding: utf-8 -*-
import json
from django.views.generic import TemplateView
from chooser.common_views import JsonView
from chooser import helpers


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