# Generated by Django 4.1.3 on 2022-11-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_resume_work_experience'),
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobResponses',
            new_name='ResponsesModel',
        ),
    ]