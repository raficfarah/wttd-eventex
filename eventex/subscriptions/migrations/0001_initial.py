# Generated by Django 3.1.7 on 2021-11-11 18:00

from django.db import migrations, models
import eventex.subscriptions.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, validators=[eventex.subscriptions.validators.validate_cpf])),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de registro')),
                ('hashid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
                'ordering': ('-created_at',),
            },
        ),
    ]
