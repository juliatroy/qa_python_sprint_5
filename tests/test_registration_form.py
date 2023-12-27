import random
import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from constants import Urls
from locators import Locators

faker = Faker()


class TestRegistration:
    def test_registration_with_valid_credentials_successful(self, driver):
        name = faker.first_name()
        email = 'yulia_troy_QA4_' + str(random.randint(100, 999)) + '@mesto.ru'

        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

    @pytest.mark.parametrize('user_password',
                             [
                                 ["1"],
                                 ["12"],
                                 ["123"],
                                 ["1234"],
                                 ["12345"]
                             ])
    def test_registration_with_too_short_password_failed(self, driver, user_password):

        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))

        user_name = faker.first_name()
        email = faker.email()

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(user_name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(user_password)

        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()

        error_text = driver.find_element(*Locators.INPUT_ERROR).text
        assert error_text == 'Некорректный пароль'

