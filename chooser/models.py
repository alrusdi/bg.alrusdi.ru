# -*- coding: utf-8 -*-
from django.db import models


class Game(models.Model):
    title = models.CharField(
        max_length=500
    )
    desc = models.TextField(
        null=True, blank=True
    )
    cover = models.ImageField(
        null=True, blank=True
    )
    is_excluded = models.BooleanField(
        default=False
    )
    is_digital = models.BooleanField(
        default=False
    )
    is_real = models.BooleanField(
        default=True
    )
    is_playable_two_players = models.BooleanField(
        default=True
    )
    total_plays = models.IntegerField(
        default=0
    )
    total_rejects = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.title


class Play(models.Model):
    game = models.ForeignKey(
        'chooser.Game',
        on_delete=models.CASCADE
    )
    mode = models.CharField(
        max_length=50,
        default='PLAYED',
        choices=(
            ('PLAYED', 'Сыграно'),
            ('REJECTED', 'Отказ'),
        )
    )
    played_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return 'Play id=%s of «%s»' % (self.pk, self.game.title)
