# Generated by Django 3.2.7 on 2021-09-21 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_tag_tag_belongs_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='children',
            name='belongs_to',
        ),
        migrations.RemoveField(
            model_name='family',
            name='home',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Room',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_belongs_to',
        ),
        migrations.DeleteModel(
            name='testing',
        ),
        migrations.DeleteModel(
            name='Children',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]