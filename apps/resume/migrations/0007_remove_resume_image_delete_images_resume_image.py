# Generated by Django 4.1.1 on 2022-12-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_images_resume_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='image',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='resume',
            name='image',
            field=models.ImageField(blank=True, max_length=10, upload_to='', verbose_name='Примеры работ (портфолио)'),
        ),
    ]
