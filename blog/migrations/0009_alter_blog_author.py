# Generated by Django 4.0 on 2022-02-08 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_categary_category_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
