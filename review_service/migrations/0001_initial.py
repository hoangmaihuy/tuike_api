# Generated by Django 3.2 on 2021-05-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('course_id', models.PositiveBigIntegerField()),
                ('class_id', models.PositiveBigIntegerField()),
                ('teacher_id', models.PositiveBigIntegerField()),
                ('recommend_score', models.FloatField(default=0)),
                ('exam_score', models.FloatField(default=0)),
                ('work_score', models.FloatField(default=0)),
                ('content_score', models.FloatField(default=0)),
                ('user_grade', models.PositiveSmallIntegerField(default=0)),
                ('create_by', models.PositiveBigIntegerField()),
                ('create_time', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'review_tab',
            },
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['course_id'], name='review_course_id_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['class_id'], name='review_class_id_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['teacher_id'], name='review_teacher_id_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['create_time'], name='review_create_time'),
        ),
    ]