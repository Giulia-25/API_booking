import json

import requests
from assertpy import assert_that


def test_delete_booking():
    CREDENTIALS = json.dumps({
        "username": "admin",
        "password": "password123"
    })

    HEADERS_TOKEN = {
        'Content-Type': 'application/json'
    }
    response_token = requests.post("https://restful-booker.herokuapp.com/auth", headers=HEADERS_TOKEN, data=CREDENTIALS)
    assert_that(response_token.status_code).is_equal_to(200)
    token = response_token.json()["token"]
    print(token)
    token = "token" + response_token.json()["token"]
    HEADERS_TOKEN["Cookie"] = token
    response_delete = requests.delete("https://restful-booker.herokuapp.com/booking/6048", headers=HEADERS_TOKEN)
    assert_that(response_token.status_code).is_equal_to(200)
    response = requests.get("https://restful-booker.herokuapp.com/booking/6048")
    assert_that(response.status_code).is_equal_to(404)
    