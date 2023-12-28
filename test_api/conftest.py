from datetime import datetime

import pytest

from test_api.helpers import OUR_USERNAME, OUR_FIRST_NAME, OUR_LAST_NAME


@pytest.fixture
def user_info():
    current_timestamp = int(datetime.now().timestamp())
    data = {
        "id": 0,
        "username": OUR_USERNAME.format(current_timestamp),
        "firstName": OUR_FIRST_NAME.format(current_timestamp),
        "lastName": OUR_LAST_NAME.format(current_timestamp),
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    return data
