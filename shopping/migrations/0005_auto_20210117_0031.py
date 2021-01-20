# Generated by Django 3.1.5 on 2021-01-17 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('shopping', '0004_tobuy_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tobuy',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='tobuy',
            name='text',
        ),
        migrations.AddField(
            model_name='tobuy',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='tobuy',
            name='quantity',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='tobuy',
            name='unit',
            field=models.TextField(null=True),
        ),
    ]
