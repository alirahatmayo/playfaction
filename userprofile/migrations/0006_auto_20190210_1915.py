# Generated by Django 2.1.5 on 2019-02-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20190210_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='player_games',
            field=models.ManyToManyField(blank=True, related_name='games', to='game.Game'),
        ),
    ]
