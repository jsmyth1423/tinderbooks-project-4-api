# Generated by Django 4.0.4 on 2022-04-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]