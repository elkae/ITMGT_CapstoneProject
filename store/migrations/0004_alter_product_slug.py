# Generated by Django 4.2.2 on 2023-07-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='Bond Paper (500 Sheets)'),
        ),
    ]
