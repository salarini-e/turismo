# Generated by Django 3.1.7 on 2021-03-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0004_equipamento_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='uuid',
            field=models.CharField(max_length=32),
        ),
    ]
