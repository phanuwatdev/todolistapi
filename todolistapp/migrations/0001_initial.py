# Generated by Django 4.0.4 on 2022-05-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('task', models.CharField(max_length=200)),
                ('checked', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
