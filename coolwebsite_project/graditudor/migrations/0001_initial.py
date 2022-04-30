# Generated by Django 4.0.1 on 2022-01-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annoyance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annoyance_text', models.CharField(max_length=500, verbose_name='Annoyance')),
            ],
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation_text', models.CharField(max_length=500, verbose_name='Situation')),
            ],
        ),
    ]
