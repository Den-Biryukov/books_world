# Generated by Django 4.0.6 on 2022-07-26 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('read_book', '0014_alter_genres_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 26, 13, 14, 46, 978065, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, to='read_book.genres'),
        ),
    ]