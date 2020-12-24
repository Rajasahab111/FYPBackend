# Generated by Django 3.1.3 on 2020-12-15 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='Time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
    ]
