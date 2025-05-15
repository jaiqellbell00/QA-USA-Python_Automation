import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert urban_routes_page.verify_from_address() == data.ADDRESS_FROM
        assert urban_routes_page.verify_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_taxi_icon()
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        actual_value = urban_routes_page.get_supportive_text()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}' but got '{actual_value}'"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_taxi_icon()
        time.sleep(1)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        assert urban_routes_page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_icon()
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.link_new_card(data.CARD_NUMBER, data.CARD_CODE)
        assert urban_routes_page.get_card_number() == data.CARD_NUMBER
        assert urban_routes_page.get_card_code() == data.CARD_CODE


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_icon()
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.link_new_card(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        assert urban_routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_taxi_icon()
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.link_new_card(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.add_blanket_and_handkerchiefs()
        assert urban_routes_page.check_blanket_and_handkerchief()
        urban_routes_page.finalize_order()
        time.sleep(5)


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_taxi_icon()
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.link_new_card(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.add_ice_cream()
        time.sleep(2)
        urban_routes_page.finalize_order()
        time.sleep(5)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_taxi_icon()
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')))
        element.click()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        urban_routes_page.enter_sms_code(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.link_new_card(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.finalize_order()
        time.sleep(5)
        urban_routes_page.verify_car_search_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
