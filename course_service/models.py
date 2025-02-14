from django.db import models


class Course(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=50)
	course_no = models.CharField(max_length=50)
	credit = models.PositiveSmallIntegerField()
	school_id = models.PositiveSmallIntegerField()
	type = models.PositiveSmallIntegerField()
	review_count = models.PositiveIntegerField(default=0)
	recommend_score = models.FloatField(default=0)
	exam_score = models.FloatField(default=0)
	work_score = models.FloatField(default=0)
	content_score = models.FloatField(default=0)
	last_review = models.PositiveBigIntegerField()
	create_time = models.PositiveBigIntegerField()

	class Meta:
		db_table = 'course_tab'
		indexes = [
			models.Index(fields=['name'], name='course_name_idx'),
			models.Index(fields=['course_no'], name='course_no_idx'),
			models.Index(fields=['school_id'], name='school_id_idx'),
			models.Index(fields=['type'], name='course_type_idx'),
		]


class Class(models.Model):
	id = models.BigAutoField(primary_key=True)
	course_id = models.PositiveBigIntegerField()
	teacher_id = models.PositiveBigIntegerField()
	semester = models.CharField(max_length=10)
	review_count = models.PositiveSmallIntegerField(default=0)
	recommend_score = models.FloatField(default=0)
	exam_score = models.FloatField(default=0)
	work_score = models.FloatField(default=0)
	content_score = models.FloatField(default=0)
	create_time = models.PositiveBigIntegerField()

	class Meta:
		db_table = 'class_tab'
		indexes = [
			models.Index(fields=['course_id'], name='course_id_idx'),
		]


