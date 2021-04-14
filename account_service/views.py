from common.utils import parse_request
from common.consts import *
from account_service.schemas import *
from account_service.account_manager import *


@parse_request(method="POST", schema=REQUEST_AUTH_CODE_SCHEMA)
def request_auth_code(request, data):
	email = data["email"]

	if not is_pku_mail(email):
		return Result.ERROR_INVALID_EMAIL, None

	auth_code = generate_auth_code(email)
	if send_auth_code(email, auth_code):
		return Result.SUCCESS, None
	else:
		return Result.ERROR_SERVER, None


@parse_request(method="POST", schema=LOGIN_SCHEMA)
def login(request, data):
	email = data["email"]
	auth_code = data["auth_code"]
	if auth_code != get_auth_code_by_email(email):
		return Result.ERROR_AUTHORIZATION, None
	user = get_or_create_user_by_email(email)
	token = generate_token(user)
	return Result.SUCCESS, {
		"access_token": token
	}
