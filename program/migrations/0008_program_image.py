# Generated by Django 4.1.4 on 2023-01-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_businessunit_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image',
            field=models.ImageField(default='default_program.png', upload_to='images/program_images'),
        ),
    ]
