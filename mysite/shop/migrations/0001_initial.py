# Generated by Django 4.2.7 on 2023-12-11 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('subject', models.CharField(max_length=12)),
                ('body', models.CharField(max_length=17)),
                ('price', models.CharField(max_length=17)),
                ('shoes', models.BooleanField(default=False)),
                ('bag', models.BooleanField(default=False)),
                ('scarf', models.BooleanField(default=False)),
            ],
        ),
    ]
