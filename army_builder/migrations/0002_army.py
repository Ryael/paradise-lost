# Generated by Django 4.2 on 2023-04-10 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='army_builder.ruleset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
