# Generated by Django 2.2.6 on 2019-10-14 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinosaurio',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinosaurios.Periodo', verbose_name='Periodo'),
        ),
    ]
