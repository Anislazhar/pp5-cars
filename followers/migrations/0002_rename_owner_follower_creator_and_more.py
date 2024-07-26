# Generated by Django 5.0.7 on 2024-07-26 19:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='owner',
            new_name='creator',
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('creator', 'followed')},
        ),
    ]
