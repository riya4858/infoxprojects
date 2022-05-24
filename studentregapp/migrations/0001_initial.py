# Generated by Django 3.2.13 on 2022-05-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('joiningdate', models.DateField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
            ],
        ),
    ]