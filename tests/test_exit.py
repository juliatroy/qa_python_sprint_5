from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestExit:

    def test_exit_from_personal_area_successful(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Constants.PROFILE_FORM_URL

        driver.find_element(*Locators.BUTTON_EXIT_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Constants.LOGIN_FORM_URL

        driver.quit()
