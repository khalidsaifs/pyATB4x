import pytest
import allure
import requests
@allure.title("Restful Booker # Project1")
@allure.description("Get the Booking id 1 for TC1 ")
@allure.tag("regression", "P0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Khalid")
@allure.testcase("#Tc1(P)")

@pytest.mark.smoke
def test_get_single_booking_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200

@allure.title("Restful Booker # Project1")
@allure.description("Get the Booking id -1 (negative TC) for TC2 ")
@allure.testcase("#Tc2(N)")
@pytest.mark.smoke
def test_get_single_booking_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data)
    assert response_data.status_code != 404

@allure.title("Restful Booker # Project1")
@allure.description("Get the Booking id 123456789 (negative TC) for TC3 ")
@allure.testcase("#Tc3(N)")
@pytest.mark.smoke
def test_get_single_booking_by_id_negative_2():
    url = "https://restful-booker.herokuapp.com/booking/123456789"
    response_data = requests.get(url)
    print(response_data)
    print(response_data.text)
    assert response_data.status_code != 404

@allure.title("Restful Booker # Project1")
@allure.description("Get the Booking id 34.67 (negative TC) for TC4 ")
@allure.testcase("#Tc4(N)")
@pytest.mark.smoke
def test_get_single_booking_by_id_negative_3():
    url = "https://restful-booker.herokuapp.com/booking/34.67"
    response_data = requests.get(url)
    print(response_data)
    print(response_data.text)
    assert response_data.status_code != 404