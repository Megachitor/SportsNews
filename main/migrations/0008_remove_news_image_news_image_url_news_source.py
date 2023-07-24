# Generated by Django 4.2.3 on 2023-07-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_club_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(default='', max_length=200, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(default='', max_length=200, verbose_name='Image'),
            preserve_default=False,
        ),
    ]
