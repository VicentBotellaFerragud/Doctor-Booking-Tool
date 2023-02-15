# Generated by Django 4.1.6 on 2023-02-15 10:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Dr.', 'Dr.'), ('Prof. Dr.', 'Prof. Dr.'), ('Dr. rer. nat.', 'Dr. rer. nat.')], default='Dr.', max_length=13)),
                ('name', models.CharField(max_length=30)),
                ('specialty', models.CharField(choices=[('Family medicine', 'Family medicine'), ('Pediatrics', 'Pediatrics'), ('Urology', 'Urology'), ('Dermatology', 'Dermatology'), ('Emergency medicine', 'Emergency medicine')], default='Family medicine', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
