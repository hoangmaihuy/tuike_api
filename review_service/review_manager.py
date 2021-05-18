from django.db import IntegrityError, transaction
from common.utils import TimeUtils
from common.cache import cache_func
from review_service.models import *
from review_service.consts import *
from course_service import course_manager, class_manager
from teacher_service import teacher_manager


@transaction.atomic()
def create_review(course_id, teacher_id, class_id, title, content, score, create_by):
	try:
		with transaction.atomic():
			review = Review.objects.create(
				course_id=course_id,
				class_id=class_id,
				teacher_id=teacher_id,
				title=title,
				content=content,
				**score,
				create_by=create_by,
				create_time=TimeUtils.now_ts()
			)
			if not review:
				return False
			if not course_manager.update_course_score(course_id, score):
				raise IntegrityError
			if not class_manager.update_class_score(class_id, score):
				raise IntegrityError
			if not teacher_manager.update_teacher_score(teacher_id, score):
				raise IntegrityError
			return True
	except IntegrityError as e:
		print(e)
		return False


@cache_func(prefix=GET_LATEST_REVIEWS_CACHE_PREFIX, timeout=GET_LATEST_REVIEWS_CACHE_TIMEOUT)
def get_latest_reviews(offset, size):
	qs = Review.objects.all().order_by("-create_time")[offset:offset+size]
	reviews = list(qs.values(
		"id", "title", "content", "course_id", "class_id", "teacher_id",
		"recommend_score", "work_score", "content_score", "exam_score", "create_time"
	))

	reviews = add_review_extra_infos(reviews)
	return reviews


def add_review_extra_infos(reviews):
	course_ids = [review["course_id"] for review in reviews]
	course_infos = course_manager.get_course_infos_by_ids(course_ids)
	course_infos_dict = {
		course_info["id"]: course_info for course_info in course_infos
	}

	class_ids = [review["class_id"] for review in reviews]
	class_infos = class_manager.get_class_infos_by_ids(class_ids)
	class_infos_dict = {
		class_info["id"]: class_info for class_info in class_infos
	}

	teacher_ids = [review["teacher_id"] for review in reviews]
	teacher_infos = teacher_manager.get_teacher_infos_by_ids(teacher_ids)
	teacher_infos_dict = {
		teacher_info["id"]: teacher_info for teacher_info in teacher_infos
	}

	review_ids = [review["id"] for review in reviews]
	interact_infos_dict = get_review_interacts(review_ids)

	for review in reviews:
		review["teacher_name"] = teacher_infos_dict[review["teacher_id"]]["name"]
		review["course_name"] = course_infos_dict[review["course_id"]]["name"]
		review["semester"] = class_infos_dict[review["class_id"]]["semester"]
		review["likes"] = interact_infos_dict[review["id"]]["likes"]
		review["dislikes"] = interact_infos_dict[review["id"]]["dislikes"]

	return reviews


def get_review_interacts(review_ids):
	interacts = list(ReviewInteract.objects.filter(review_id__in=review_ids).values())
	interact_dict = {}
	for review_id in review_ids:
		interact_dict[review_id] = {
			"likes": [],
			"dislikes": [],
		}
	for item in interacts:
		if item["action"] == ReviewInteraction.LIKE:
			interact_dict[item["review_id"]]["likes"].append(item["create_by"])
		else:
			interact_dict[item["review_id"]]["dislikes"].append(item["create_by"])

	return interact_dict


def get_course_reviews(course_id, offset, limit, sorted_by, teacher_id=None, class_ids=None, user_id=None):
	qs = Review.objects.filter(course_id=course_id)
	if teacher_id:
		qs = qs.filter(teacher_id=teacher_id)
	if class_ids:
		qs = qs.filter(class_id__in=class_ids)
	if sorted_by:
		qs = qs.order_by(sorted_by)
	total = qs.count()
	qs = qs[offset:offset+limit]
	reviews = list(qs.values(
		"id", "title", "content", "course_id", "teacher_id", "class_id",
		"recommend_score", "content_score", "work_score", "exam_score", "create_time"
	))

	reviews = add_review_extra_infos(reviews)
	return total, reviews


def interact_review(review_id, action, user_id):
	ReviewInteract.objects.get_or_create(
		review_id=review_id,
		action=action,
		create_by=user_id,
		create_time=TimeUtils.now_ts(),
	)

	ReviewInteract.objects.filter(review_id=review_id, action=1-action, create_by=user_id).delete()