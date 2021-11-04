# Generated by Django 3.2.7 on 2021-11-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0002_auto_20211019_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameScoreboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat1', models.IntegerField(default=0)),
                ('stat2', models.IntegerField(default=0)),
                ('stat3', models.IntegerField(default=0)),
                ('stat4', models.IntegerField(default=0)),
                ('totalPoints', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Scoreboard',
            new_name='UserStats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='scoreboard',
        ),
        migrations.RemoveField(
            model_name='team',
            name='scoreboard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ManyToManyField(related_name='winnerTeam', to='endpoint.Team'),
        ),
        migrations.AddField(
            model_name='user',
            name='userStats',
            field=models.ManyToManyField(to='endpoint.UserStats'),
        ),
        migrations.AddField(
            model_name='team',
            name='team1Scoreboard',
            field=models.ManyToManyField(related_name='team1Scoreboard', to='endpoint.GameScoreboard'),
        ),
    ]
