# Generated by Django 5.1.6 on 2025-03-08 14:48

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
