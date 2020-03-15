# Generated by Django 3.0.4 on 2020-03-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
