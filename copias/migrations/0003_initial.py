# Generated by Django 4.1.7 on 2023-03-13 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copias', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to=settings.AUTH_USER_MODEL),
        ),
    ]
