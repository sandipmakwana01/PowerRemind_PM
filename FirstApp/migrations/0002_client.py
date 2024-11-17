# Generated by Django 5.1.3 on 2024-11-14 09:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('given_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('process', 'Process'), ('complete', 'Complete')], default='process', max_length=10)),
                ('add_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('remove_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('daily_interest_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
