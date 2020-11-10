# Generated by Django 3.1.1 on 2020-09-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDesc', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
