# Generated by Django 4.2.15 on 2025-01-12 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_department_num_and_more'),
        ('accounts', '0003_employee_company_alter_employee_workflow_and_more'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_tasks', to='company.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='assigned_employees',
            field=models.ManyToManyField(related_name='project_employees', to='accounts.employee'),
        ),
    ]
