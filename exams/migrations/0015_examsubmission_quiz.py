# Generated by Django 3.2.5 on 2021-08-04 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0061_alter_registrationcontainer_allowed_tracks'),
        ('exams', '0014_auto_20180531_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.IntegerField(default=0, help_text='Answer to p1')),
                ('answer2', models.IntegerField(default=0, help_text='Answer to p2')),
                ('answer3', models.IntegerField(default=0, help_text='Answer to p3')),
                ('answer4', models.IntegerField(default=0, help_text='Answer to p4')),
                ('answer5', models.IntegerField(default=0, help_text='Answer to p5')),
                ('exam', models.OneToOneField(help_text='The associated exam for this answer key', on_delete=django.db.models.deletion.CASCADE, to='exams.practiceexam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess1', models.IntegerField(default=0, help_text='Guess for p1')),
                ('guess2', models.IntegerField(default=0, help_text='Guess for p2')),
                ('guess3', models.IntegerField(default=0, help_text='Guess for p3')),
                ('guess4', models.IntegerField(default=0, help_text='Guess for p4')),
                ('guess5', models.IntegerField(default=0, help_text='Guess for p5')),
                ('submitted', models.DateTimeField(auto_now_add=True, help_text='When the quiz was submitted')),
                ('quiz', models.ForeignKey(help_text='The quiz being submitted for', on_delete=django.db.models.deletion.CASCADE, to='exams.quiz')),
                ('student', models.ForeignKey(help_text='The student taking the exam', on_delete=django.db.models.deletion.CASCADE, to='roster.student')),
            ],
            options={
                'unique_together': {('quiz', 'student')},
            },
        ),
    ]
