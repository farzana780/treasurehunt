# Generated by Django 3.0.7 on 2020-06-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasuregram',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
