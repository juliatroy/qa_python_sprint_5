from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestPersonalAreaNavigation:

    def test_navigation_main_page_to_personal_area_successful(self, driver):
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
        driver.quit()

    def test_navigation_personal_area_to_constructor_by_link_successful(self, driver):
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
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Constants.PROFILE_FORM_URL

        driver.find_element(*Locators.MENU_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == Constants.HOME_PAGE_URL

    def test_navigation_personal_area_to_constructor_by_logo_successful(self, driver):
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
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Constants.PROFILE_FORM_URL

        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == Constants.HOME_PAGE_URL


class TestConstructorNavigation:
    def test_navigation_constructor_to_buns(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()

        driver.find_element(*Locators.BUTTON_BUNS).click()
        assert driver.find_element(*Locators.HEADER_BUNS).is_displayed()
        driver.quit()

    def test_navigation_constructor_to_sauces(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.HEADER_SAUCES).is_displayed()

        driver.quit()

    def test_navigation_constructor_to_fillings(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()
        driver.quit()
