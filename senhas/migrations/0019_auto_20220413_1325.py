# Generated by Django 3.2.10 on 2022-04-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0018_alter_viagem_turismo_outros'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='cadastur_guia',
            field=models.CharField(max_length=18),
        ),
    ]
