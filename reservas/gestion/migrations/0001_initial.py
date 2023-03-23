# Generated by Django 4.1.7 on 2023-03-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
    ]
