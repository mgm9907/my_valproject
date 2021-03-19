# Generated by Django 3.0.7 on 2020-06-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_email', models.EmailField(blank=True, max_length=70)),
            ],
            options={
                'db_table': 'subscribe_user_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('message', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]