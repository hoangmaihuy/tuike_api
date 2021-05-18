from tuike_api.settings import HOST

REVIEW_SERVICE_API = HOST + "/review"

GET_LATEST_REVIEWS_CACHE_PREFIX = "GET_LATEST_REVIEWS"

GET_LATEST_REVIEWS_CACHE_TIMEOUT = 60 * 2


class ReviewServiceApi:
	ADD_REVIEW = REVIEW_SERVICE_API + "/add_review"
	GET_LATEST_REVIEWS = REVIEW_SERVICE_API + "/get_latest_reviews"
	GET_COURSE_REVIEWS = REVIEW_SERVICE_API + "/get_course_reviews"


TEST_COURSE_ID = 1824
TEST_TEACHER_ID = 3241
TEST_SEMESTER = "20-21-2"