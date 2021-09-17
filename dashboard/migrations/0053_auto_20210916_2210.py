# Generated by Django 3.2.7 on 2021-09-17 02:10

import dashboard.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0052_auto_20210916_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='code',
            field=models.CharField(max_length=96, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='24-char hex string', regex='[a-f0-9]{24}')]),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.TextField(help_text='Text shown beneath this achievement for students who obtain it.'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='diamonds',
            field=models.SmallIntegerField(default=1, help_text='Number of diamonds for this achievement'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(blank=True, help_text='Image for the obtained achievement, at most 1MB.', null=True, upload_to=dashboard.models.achievement_image_file_name, validators=[dashboard.models.validate_at_most_1mb]),
        ),
        migrations.AlterField(
            model_name='palaceentry',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional small photo that will appear next to your entry, no more than 1 megabyte', null=True, upload_to=dashboard.models.palace_image_file_name, validators=[dashboard.models.validate_at_most_1mb]),
        ),
        migrations.AlterField(
            model_name='palaceentry',
            name='message',
            field=models.TextField(blank=True, help_text='You can write a message here', max_length=1024),
        ),
    ]
