# Generated by Django 5.1.3 on 2024-11-14 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0004_alter_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_interest_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]