# Generated by Django 3.2.7 on 2021-09-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_description',
            field=models.TextField(),
        ),
    ]
