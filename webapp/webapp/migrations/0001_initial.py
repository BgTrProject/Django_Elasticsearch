# Generated by Django 3.2 on 2022-07-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElasticDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('date', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
