# Generated by Django 4.1.1 on 2022-10-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_author_last_name_alter_book_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='on_shelf',
            field=models.BooleanField(db_column='Czy na półce', default=True),
            preserve_default=False,
        ),
    ]