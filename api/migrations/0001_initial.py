# Generated by Django 2.2.5 on 2021-02-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('caption', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=250)),
            ],
        ),
    ]
