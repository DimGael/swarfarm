# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0003_auto_20170601_2202'),
        ('bestiary', '0001_squashed_0004_patchnotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CraftMaterial',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('herders.craftmaterial',),
        ),
        migrations.CreateModel(
            name='HomunculusSkill',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('herders.homunculusskill',),
        ),
        migrations.CreateModel(
            name='HomunculusSkillCraftCost',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('herders.homunculusskillcraftcost',),
        ),
        migrations.CreateModel(
            name='MonsterCraftCost',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('herders.monstercraftcost',),
        ),
    ]