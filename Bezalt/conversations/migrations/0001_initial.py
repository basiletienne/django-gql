# Generated by Django 4.0.1 on 2022-01-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sender', models.TextField()),
                ('receiver', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
