# Generated by Django 4.0.6 on 2022-07-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_book', '0015_book_time_create_book_time_update_alter_book_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.AddField(
            model_name='genres',
            name='book',
            field=models.ManyToManyField(blank=True, to='read_book.book'),
        ),
    ]
