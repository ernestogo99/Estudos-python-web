# Generated by Django 5.1.4 on 2024-12-29 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0002_alter_aluno_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2024, 12, 29, 14, 49, 14, 238569, tzinfo=datetime.timezone.utc)),
        ),
    ]
