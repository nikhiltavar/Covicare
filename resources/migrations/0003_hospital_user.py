# Generated by Django 4.0 on 2022-04-24 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('resources', '0002_auto_20220424_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]