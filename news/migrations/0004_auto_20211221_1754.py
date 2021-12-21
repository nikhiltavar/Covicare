# Generated by Django 3.2.7 on 2021-12-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.Tags'),
        ),
    ]