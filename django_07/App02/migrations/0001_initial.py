# Generated by Django 2.2.9 on 2020-02-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(db_column='password_hash', max_length=128)),
            ],
            options={
                'db_table': 'bbs_user',
            },
        ),
    ]