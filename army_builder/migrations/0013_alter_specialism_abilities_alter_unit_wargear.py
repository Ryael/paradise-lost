# Generated by Django 4.2 on 2023-04-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_builder', '0012_remove_wargear_weapon_profiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialism',
            name='abilities',
            field=models.ManyToManyField(to='army_builder.option'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='wargear',
            field=models.ManyToManyField(to='army_builder.option'),
        ),
    ]