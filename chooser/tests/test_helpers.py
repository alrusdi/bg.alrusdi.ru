# -*- coding: utf-8 -*-
import fudge
from django.test import TestCase
from chooser import helpers


class BaseTestCase(TestCase):
    pass


class ChooseNewGameToPlayTest(BaseTestCase):

    @fudge.patch('chooser.helpers._choose_random')
    def test_chooses_random_game_from_lowest_by_play(self, choose_random_stub):
        stored_cands = []

        def choose_random_repl(cands):
            stored_cands = [g["id"] for g in cands]

        choose_random_stub.expects_call().calls(choose_random_repl)

        game = helpers.choose_new_game_to_play(
            {
                'is_real': True,
                'is_digital': False
            }
        )

        self.assertIn(stored_cands, game['id'])


