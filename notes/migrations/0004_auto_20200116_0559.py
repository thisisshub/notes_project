# Generated by Django 2.2.1 on 2020-01-16 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20200115_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes_model',
            old_name='title',
            new_name='subject',
        ),
    ]
