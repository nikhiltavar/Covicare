# Generated by Django 4.0 on 2022-01-03 18:02

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, max_length=100, null=True, populate_from='title', unique=True),
        ),
    ]