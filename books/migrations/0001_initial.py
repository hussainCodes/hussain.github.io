# Generated by Django 4.0 on 2021-12-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('auther', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=500)),
                ('page', models.IntegerField()),
            ],
        ),
    ]