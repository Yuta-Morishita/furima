# Generated by Django 2.2.2 on 2020-04-19 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('ability', models.TextField()),
                ('status', models.CharField(choices=[('1', '新品未使用'), ('2', '未使用に近い'), ('3', '目立った傷や汚れなし'), ('4', '全体的に状態が悪い')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
