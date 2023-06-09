# Generated by Django 4.2 on 2023-04-13 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_builder', '0014_alter_ability_name_alter_army_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('points_max', models.SmallIntegerField(default='0')),
                ('serialised_roster', models.TextField()),
                ('army', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='army_builder.army')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='army_builder.ruleset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
