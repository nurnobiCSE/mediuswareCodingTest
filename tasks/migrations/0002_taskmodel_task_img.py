# Generated by Django 4.2.6 on 2023-10-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='task_img',
            field=models.ImageField(default='', upload_to='task_img'),
            preserve_default=False,
        ),
    ]