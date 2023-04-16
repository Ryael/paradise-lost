# Generated by Django 4.2 on 2023-04-16 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('army_builder', '0015_roster'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roster',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
