# Generated by Django 4.2.3 on 2023-07-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_player_age_alter_player_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Away', to='main.club')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Home', to='main.club')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matchs',
            },
        ),
    ]
