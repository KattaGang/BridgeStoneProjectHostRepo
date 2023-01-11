# Generated by Django 4.1.4 on 2023-01-11 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_remove_program_business_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='business_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.businessunit'),
        ),
    ]
