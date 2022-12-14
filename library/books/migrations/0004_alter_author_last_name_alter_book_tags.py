# Generated by Django 4.1.1 on 2022-10-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_tag_alter_book_options_book_author_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='book', to='books.tag'),
        ),
    ]
