from test_api.helpers import create_user, get_user_by_username, update_first_name, update_user_by_username, \
    delete_user_by_username, check_user_is_not_found


class TestUserClass:
    def test_post_user(self, user_info):
        create_user(user_info)
        username = user_info['username']
        response = get_user_by_username(username)

        json_data = response.json()
        expected_first_name = user_info['firstName']
        expected_last_name = user_info['lastName']
        actual_first_name = json_data['firstName']
        actual_last_name = json_data['lastName']
        assert actual_first_name == expected_first_name, f'Actual first name is {actual_first_name}'
        assert actual_last_name == expected_last_name, f'Actual last name is {actual_last_name}'

    def test_get_user(self, user_info):
        create_user(user_info)

        username = user_info['username']
        response = get_user_by_username(username)

        expected_keys = list(user_info)
        actual_keys = list(response.json())
        assert actual_keys == expected_keys, f'Actual keys is {actual_keys}'

    def test_put_user(self, user_info):
        create_user(user_info)

        username = user_info['username']
        response = get_user_by_username(username)

        json_data = response.json()

        update_first_name(json_data)

        update_user_by_username(username, json_data)

        response_2 = get_user_by_username(username)
        json_data_2 = response_2.json()
        assert json_data == json_data_2, 'User is not updated'

    def test_delete_user(self, user_info):
        create_user(user_info)

        username = user_info['username']

        delete_user_by_username(username)

        check_user_is_not_found(username)
