# Generated by Django 3.2.9 on 2021-12-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_usuario_cadastur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=60),
        ),
    ]
