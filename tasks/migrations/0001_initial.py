# Generated by Django 4.2.15 on 2025-01-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Project Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name='End Date')),
                ('assigned_employees', models.ManyToManyField(related_name='projects', to='accounts.employee')),
            ],
        ),
    ]
