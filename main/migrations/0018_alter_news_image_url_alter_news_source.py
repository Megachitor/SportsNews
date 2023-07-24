# Generated by Django 4.2.3 on 2023-07-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_news_content_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.CharField(default='static/images/img-01_002.jpg', max_length=300, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=300, verbose_name='Source'),
        ),
    ]