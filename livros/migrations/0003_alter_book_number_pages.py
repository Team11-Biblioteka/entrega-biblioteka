# Generated by Django 4.1.7 on 2023-03-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_pages',
            field=models.PositiveIntegerField(),
        ),
    ]