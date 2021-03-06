# Generated by Django 4.0.4 on 2022-05-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Сообщение')),
                ('email', models.EmailField(max_length=255, verbose_name='Email почта')),
                ('adress', models.TextField(verbose_name='Сообщение')),
                ('messages', models.TextField(verbose_name='Сообщение')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
