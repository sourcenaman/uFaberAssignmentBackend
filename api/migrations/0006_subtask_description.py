# Generated by Django 3.1.6 on 2021-02-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210215_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
