# Generated by Django 5.1.4 on 2024-12-29 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2024, 12, 29, 11, 48, 9, 387949)),
        ),
    ]