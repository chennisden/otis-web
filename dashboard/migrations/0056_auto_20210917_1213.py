# Generated by Django 3.2.7 on 2021-09-17 16:13

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0055_rename_palaceentry_palacecarving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palacecarving',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional small photo that will appear next to your carving, no more than 1 megabyte', null=True, upload_to=dashboard.models.palace_image_file_name, validators=[dashboard.models.validate_at_most_1mb]),
        ),
        migrations.AlterField(
            model_name='palacecarving',
            name='visible',
            field=models.BooleanField(default=True, help_text='Uncheck to hide your carving altogether (can change your mind later)'),
        ),
    ]
