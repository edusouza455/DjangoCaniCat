# Generated by Django 5.0 on 2024-10-21 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testeCursos', '0004_lista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='lista',
            name='descripiton',
        ),
        migrations.RemoveField(
            model_name='lista',
            name='status',
        ),
        migrations.RemoveField(
            model_name='lista',
            name='title',
        ),
    ]
