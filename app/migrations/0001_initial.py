# Generated by Django 4.2.4 on 2023-08-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Pronto', 'pronto'), ('Em Andamento', 'Em Andamento'), ('Pendente', 'Pendente')], max_length=12)),
            ],
        ),
    ]