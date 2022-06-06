# Generated by Django 4.0.5 on 2022-06-03 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_agenda',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da Criacao'),
        ),
    ]