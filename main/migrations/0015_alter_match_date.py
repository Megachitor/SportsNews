# Generated by Django 4.2.3 on 2023-07-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_match_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]