# Generated by Django 4.2.2 on 2023-07-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='potangina mo'),
        ),
    ]