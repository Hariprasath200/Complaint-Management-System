# Generated by Django 3.2.24 on 2024-02-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0004_auto_20240229_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('complaint', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accepted'), ('reject', 'Rejected')], default='pending', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='demp',
        ),
    ]
