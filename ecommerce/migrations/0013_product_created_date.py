# Generated by Django 4.0 on 2022-05-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_remove_product_highlights'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
