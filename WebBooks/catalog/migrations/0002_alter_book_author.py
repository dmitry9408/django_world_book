# Generated by Django 4.2.1 on 2023-06-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выбеите автора книги', to='catalog.author', verbose_name='Автор книги'),
        ),
    ]
