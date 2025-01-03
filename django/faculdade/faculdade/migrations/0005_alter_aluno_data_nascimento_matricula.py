# Generated by Django 5.1.4 on 2024-12-29 15:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0004_alter_aluno_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2024, 12, 29, 12, 48, 5, 81848)),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculdade.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculdade.curso')),
            ],
        ),
    ]
