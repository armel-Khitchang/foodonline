# Generated by Django 5.1.5 on 2025-02-06 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_vendor_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='life',
            field=models.CharField(default='100 days', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='mfg',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_count',
            field=models.CharField(default='10', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='Organic', max_length=100),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='core.product'),
        ),
    ]
