import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@pytest.mark.smoke
def test_sai():
    assert 1 + 1 == 3

@pytest.mark.smoke
def test_sham():
    assert 1 - 1 != 1

@pytest.mark.reg
def test_aana():
    assert 1 + 1 == 2

@pytest.mark.skip(reason = "not req")
def test_kha():
    assert 2 - 1 == 1
