# Generated by Django 3.0.3 on 2020-02-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_game_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('developer', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='game_type',
            old_name='type_id',
            new_name='game_type_id',
        ),
        migrations.CreateModel(
            name='User_games',
            fields=[
                ('user_game_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('purchased_date', models.DateTimeField()),
                ('serial', models.CharField(max_length=255)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.Game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.User')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('lmage_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=255)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.Game_type'),
        ),
    ]