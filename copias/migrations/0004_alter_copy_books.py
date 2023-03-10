# Generated by Django 4.1.7 on 2023-03-10 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("livros", "0002_initial"),
        ("copias", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="copy",
            name="books",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="copy",
                to="livros.book",
            ),
        ),
    ]
