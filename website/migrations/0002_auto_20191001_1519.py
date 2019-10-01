# Generated by Django 2.2.5 on 2019-10-01 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conclusao',
            name='desafio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Desafio'),
        ),
        migrations.AlterField(
            model_name='desafio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Usuario'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Usuario'),
        ),
    ]