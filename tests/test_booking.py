import requests
from assertpy import assert_that


def test_get_all_bookings():
    # response = requests.get("https://restful-booker.herokuapp.com/booking")
    # ori asa
    response = requests.request("GET", "https://restful-booker.herokuapp.com/booking")

    assert_that(response.status_code).is_equal_to(200)
    print(response.status_code)
    # raspunsul sub forma de json
    print(response.json())
    assert_that(response.json()).extracting("bookingid").is_not_none()


def test_one_booking_negative():
    response = requests.get("https://restful-booker.herokuapp.com/booking/6161612225")
    assert_that(response.status_code).is_equal_to(404)


def test_one_booking():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1861")
    assert_that(response.status_code).is_equal_to(200)
    print(response.json())
    assert_that(response.json()['firstname']).is_equal_to("Josimar")
    assert_that(response.json()['lastname']).is_equal_to("Leon")
    assert_that(response.json()['bookingdates']["checkin"]).is_equal_to("2018-01-01")