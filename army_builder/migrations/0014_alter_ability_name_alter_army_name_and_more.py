# Generated by Django 4.2 on 2023-04-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_builder', '0013_alter_specialism_abilities_alter_unit_wargear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='army',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ruleset',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='specialism',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wargear',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='weaponprofile',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
