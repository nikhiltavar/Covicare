# Generated by Django 4.0 on 2022-02-09 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
    ]