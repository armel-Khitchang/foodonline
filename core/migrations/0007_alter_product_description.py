# Generated by Django 5.1.5 on 2025-02-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_life_alter_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='This is the product', max_length=1000),
        ),
    ]
