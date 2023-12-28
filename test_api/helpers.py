import requests

OUR_USERNAME = 'TMS_IB_{}'
OUR_FIRST_NAME = 'Igor_{}'
OUR_LAST_NAME = 'Bolduk_{}'


class UserStore:
    HOST = "https://petstore.swagger.io/v2"
    USER = "/user"
    USER_USERNAME = "/user/{username}"


def check_response(response):
    assert response.ok, f"{response.status_code = }"


def create_user(user_info):
    url = f"{UserStore.HOST}{UserStore.USER}"
    response = requests.post(url, json=user_info)
    check_response(response)


def get_user_by_username(username):
    url = f"{UserStore.HOST}{UserStore.USER_USERNAME.format(username=username)}"
    response = requests.get(url)
    check_response(response)
    return response


def update_user_by_username(username, json_data):
    url = f"{UserStore.HOST}{UserStore.USER_USERNAME.format(username=username)}"
    response = requests.put(url, json=json_data)
    check_response(response)


def delete_user_by_username(username):
    url = f"{UserStore.HOST}{UserStore.USER_USERNAME.format(username=username)}"
    response = requests.delete(url)
    check_response(response)


def check_user_is_not_found(username):
    url = f"{UserStore.HOST}{UserStore.USER_USERNAME.format(username=username)}"
    response_get = requests.get(url)
    assert response_get.status_code == 404, 'User was not deleted'


def update_first_name(json_data):
    actual_first_name = json_data['firstName']
    new_first_name = actual_first_name.replace('Igor', 'Ivan')
    json_data['firstName'] = new_first_name
