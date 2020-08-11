# Generated by Django 3.1 on 2020-08-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_bot', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textuser',
            fields=[
                ('text_user', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('timestamp', models.FloatField(blank=True, null=True)),
                ('entity', models.CharField(blank=True, max_length=10000, null=True)),
                ('intent', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'TextUser',
                'managed': False,
            },
        ),
    ]
