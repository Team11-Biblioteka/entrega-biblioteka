# Generated by Django 4.1.7 on 2023-03-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_start_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('is_returned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('copy_booked', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
