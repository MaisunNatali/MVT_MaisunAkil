# Generated by Django 4.1 on 2022-08-27 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentezco',
            name='miembro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Familia.familiar'),
        ),
    ]
