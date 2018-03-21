# Generated by Django 2.0.3 on 2018-03-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20180321_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, upload_to='pizzas'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='pizza',
            name='preparation',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]
