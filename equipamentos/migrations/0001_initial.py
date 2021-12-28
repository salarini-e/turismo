# Generated by Django 3.1.7 on 2021-03-21 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, unique=True)),
                ('descricao', models.CharField(max_length=3000)),
                ('foto', models.CharField(max_length=250)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Descrição',
                'verbose_name_plural': 'Descrições',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=32, unique=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipamentos.equipamento')),
            ],
            options={
                'ordering': ['dt_inclusao'],
            },
        ),
        migrations.AddField(
            model_name='equipamento',
            name='tipo_equipamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipamentos.tipo_equipamento'),
        ),
    ]
