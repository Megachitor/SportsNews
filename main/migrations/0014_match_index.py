# Generated by Django 4.2.3 on 2023-07-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='index',
            field=models.IntegerField(default=0, verbose_name='Index'),
            preserve_default=False,
        ),
    ]
