# Generated by Django 5.1.4 on 2024-12-29 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0003_alter_aluno_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2024, 12, 29, 11, 51, 45, 756312)),
        ),
    ]
