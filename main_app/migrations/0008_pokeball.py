# Generated by Django 4.0.2 on 2022-04-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_training_date_alter_training_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokeball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=40)),
            ],
        ),
    ]
