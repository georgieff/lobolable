# Generated by Django 2.0.3 on 2018-03-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='url_name',
            field=models.URLField(max_length=300, unique=True),
        ),
    ]
