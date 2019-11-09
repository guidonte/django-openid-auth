# Generated by Django 2.2.6 on 2019-11-09 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_url', models.TextField(max_length=2047)),
                ('handle', models.CharField(max_length=255)),
                ('secret', models.TextField(max_length=255)),
                ('issued', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('assoc_type', models.TextField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Nonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_url', models.CharField(max_length=2047)),
                ('timestamp', models.IntegerField()),
                ('salt', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpenID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimed_id', models.CharField(max_length=255, unique=True)),
                ('display_id', models.TextField(max_length=2047)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
