# Generated by Django 2.2.10 on 2020-02-22 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='empty', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='notes.Notes_Model'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='notes.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='empty'),
        ),
    ]
