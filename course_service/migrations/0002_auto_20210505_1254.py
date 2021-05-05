# Generated by Django 3.2 on 2021-05-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='content_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='class',
            name='exam_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='class',
            name='recommend_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='class',
            name='work_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='content_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='exam_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='recommend_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='work_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='content_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='exam_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='recommend_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='work_score',
            field=models.FloatField(default=0),
        ),
    ]
