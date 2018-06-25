# -*- coding: utf-8 -*-
import random
from chooser.models import Game, Play
from django.db.models import F


def _choose_random(candidates):
    game = random.choice(candidates)
    return game


def register_play(game_id):
    if not game_id:
        return False

    game = Game.objects.filter(pk=game_id).first()

    if not game:
        return False

    Play.objects.create(
        game=game,
        mode='PLAYED'
    )

    Game.objects.filter(pk=game_id).update(total_plays=F('total_plays') + 1)

    return True


def reject_play(game_id):
    if not game_id:
        return False

    game = Game.objects.filter(pk=game_id).first()

    if not game:
        return False

    Play.objects.create(
        game=game,
        mode='REJECTED'
    )

    Game.objects.filter(pk=game_id).update(total_plays=F('total_rejects') + 1)

    return True


def choose_new_game_to_play(params=None):
    is_real = bool(params.get('is_real'))
    is_digital = bool(params.get('is_digital'))

    data = Game.objects.filter(
        is_excluded=False,
        is_playable_two_players=True
    )
    games = []

    for g in data:
        igame = {
            'id': g.id,
            'title': g.title,
            'plays_count': g.total_plays,
            'rejects_count': g.total_rejects,
            'is_digital': g.is_digital,
            'is_real': g.is_real,
            'cover': g.cover.url if g.cover else False,
            'plays_and_rejects': g.total_plays + g.total_rejects
        }

        if not g.is_real and not g.is_digital:
            continue

        if is_real != is_digital:
            if is_real and not g.is_real:
                continue
            if is_digital and not g.is_digital:
                continue

        games.append(igame)

    games = sorted(games, key=lambda k: k['plays_and_rejects'])

    candidates = []
    counts_lim = 3
    prev_ct = -1

    for g in games:
        ct = g['plays_and_rejects']
        candidates.append(g)
        if ct != prev_ct:
            counts_lim -= 1
            if counts_lim + 1 < 1:
                break
            prev_ct = ct
    game = _choose_random(candidates[0:-1])
    return game


