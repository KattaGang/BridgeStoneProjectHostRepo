# Generated by Django 4.1.4 on 2023-01-08 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idea', '0011_alter_idea_bu_delete_businessunit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='BU',
            new_name='business_unit',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='images',
        ),
        migrations.AddField(
            model_name='idea',
            name='image',
            field=models.ImageField(null=True, upload_to='idea_images'),
        ),
        migrations.CreateModel(
            name='Ideator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('domain', models.CharField(max_length=200, null=True)),
                ('current_industry', models.CharField(max_length=500, null=True)),
                ('year_of_experience', models.DurationField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
