# Generated by Django 4.0.6 on 2022-07-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_book', '0019_remove_genres_book_book_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='read_book.genres'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='genre',
            field=models.CharField(blank=True, choices=[('mystery', 'Mystery'), ('thriller', 'Thriller'), ('horror', 'Horror'), ('historical', 'Historical'), ('romance', 'Romance'), ('western', 'Western'), ('bildungsroman', 'Bildungsroman'), ('speculative fiction', 'Speculative Fiction'), ('science fiction', 'Science Fiction'), ('fantasy', 'Fantasy'), ('dystopian', 'Dystopian'), ('magical realism', 'Magical Realism'), ('realist literature', 'Realist Literature'), ('literary fiction', 'Literary Fiction')], max_length=50, null=True),
        ),
    ]
