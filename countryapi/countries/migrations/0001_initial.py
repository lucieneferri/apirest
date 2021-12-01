# Generated by Django 3.2.9 on 2021-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('carea', models.IntegerField(help_text='(in square kilometers)')),
            ],
        ),
    ]
