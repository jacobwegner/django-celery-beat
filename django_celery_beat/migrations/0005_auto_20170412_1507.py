# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0004_auto_20170221_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarschedule',
            name='event',
            field=models.CharField(choices=[('dawn_astronomical', 'dawn_astronomical'), ('dawn_civil', 'dawn_civil'), ('dawn_nautical', 'dawn_nautical'), ('dusk_astronomical', 'dusk_astronomical'), ('dusk_civil', 'dusk_civil'), ('dusk_nautical', 'dusk_nautical'), ('solar_noon', 'solar_noon'), ('sunrise', 'sunrise'), ('sunset', 'sunset')], max_length=24, verbose_name='event'),
        ),
    ]
