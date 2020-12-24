# Generated by Django 3.1.3 on 2020-12-15 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20201215_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='password',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/api/images/person.jpg', null=True, upload_to='media/api/images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]