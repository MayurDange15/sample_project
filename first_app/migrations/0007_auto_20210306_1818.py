# Generated by Django 3.1.3 on 2021-03-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_delete_gccontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seq',
            name='sample_seq',
            field=models.TextField(max_length=200),
        ),
    ]
