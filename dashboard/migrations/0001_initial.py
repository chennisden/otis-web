# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 22:03

from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_unit_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roster', '0009_auto_20170808_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('HMWK', 'Homework'), ('TRNS', 'Transcript'), ('NOTE', 'Notes / Comments'), ('MISC', 'Miscellaneous')], help_text='What kind of file this is', max_length=10)),
                ('content', models.FileField(help_text='The file itself')),
                ('description', models.CharField(blank=True, help_text='A description of the file (defaults to filename if blank)', max_length=160)),
                ('benefactor', models.ForeignKey(help_text='The student for which this file is meant', on_delete=django.db.models.deletion.CASCADE, to='roster.Student')),
                ('owner', models.ForeignKey(help_text='The user who uploaded the file', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(blank=True, help_text='The unit for which this file is associated', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Unit')),
            ],
        ),
    ]
