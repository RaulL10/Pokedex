# Generated by Django 4.0.2 on 2022-04-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_training_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='time',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='Morning', max_length=1),
        ),
    ]
