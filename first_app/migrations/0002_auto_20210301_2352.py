# Generated by Django 3.1.7 on 2021-03-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gccontent',
            name='gcper',
        ),
        migrations.AddField(
            model_name='gccontent',
            name='GCPer',
            field=models.SmallIntegerField(default=12, max_length=3),
            preserve_default=False,
        ),
    ]