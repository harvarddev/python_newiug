# Generated by Django 4.0.4 on 2022-08-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('manzil', models.CharField(max_length=50)),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
    ]
