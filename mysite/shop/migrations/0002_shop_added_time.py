# Generated by Django 4.2.7 on 2023-12-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
