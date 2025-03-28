# Generated by Django 5.1.5 on 2025-02-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_life_product_mfg_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='life',
            field=models.CharField(blank=True, default='100 days', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_count',
            field=models.CharField(blank=True, default='10', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, default='Organic', max_length=100, null=True),
        ),
    ]
