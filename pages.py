from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By. XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-icon"]//img[@alt="Supportive"]')
    SUPPORTIVE_TEXT_LOCATOR = (By.XPATH, '(//div[@class="tcard-title"])[5]')
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '//div[@class="np-button"]//div[text()="Phone number"]')
    PHONE_NUMBER_LOCATOR = (By.ID, "phone")
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    SMS_CODE_LOCATOR = (By.XPATH, '//input[@placeholder="xxxx"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//div[@class="buttons"]//button[text()="Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_BUTTON_LOCATOR = (By.XPATH, '//img[@class="pp-plus"]')
    CARD_NUMBER_LOCATOR = (By.XPATH, '//input[@id="number"]')
    CVV_CODE_LOCATOR = (By.XPATH, '//input[@placeholder="12"]')
    ADDING_A_CARD_TITLE_LOCATOR = (By.XPATH, '//div[text()="Adding a card"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//div[@class="pp-buttons"]//button[text()="Link"]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    MESSAGE_TO_THE_DRIVER_LOCATOR = (By.XPATH, '//input[@placeholder="Get some whiskey"]')
    ORDER_REQUIREMENTS_LOCATOR = (By.XPATH, '//div[@class="reqs-head"]')
    BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR = (By.CLASS_NAME, 'switch')
    CHECK_BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR = (By. CLASS_NAME, 'switch-input')
    ICE_CREAM_ADD_BUTTON_LOCATOR = (By.CLASS_NAME, "counter-plus")
    ORDER_BUTTON_LOCATOR = (By.CLASS_NAME, "smart-button")
    CAR_SEARCH_MODAL_LOCATOR = (By.CLASS_NAME, "order-header-title" )

    def __init__ (self, driver):
        self.driver = driver

        # Enter "From" location
    def enter_from_address(self, from_text,):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

        # Enter "To" address
    def enter_to_address(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

        # Step created for entering "From" and "To" locations
    def enter_locations(self, from_text, to_text):
        self.enter_from_address(from_text)
        self.enter_to_address(to_text)

        # Verify "From" address is correct
    def verify_from_address(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value')

        # Verify "To" address is correct
    def verify_to_address(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

        # Click the "Custom" option
    def click_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

        # Click the taxi icon
    def click_taxi_icon(self):
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

        # Click the "Call a taxi" button
    def click_call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

        # Select Supportive Tariff plan
    def click_supportive_tariff(self):
        self.driver.find_element(*self.SUPPORTIVE_TARIFF_LOCATOR).click()

        # Verify "Supportive" text
    def get_supportive_text(self):
        return self.driver.find_element(*self.SUPPORTIVE_TEXT_LOCATOR).text

        # Click phone number field
    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).click()

        # Enter a phone number
    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(phone_number)

        # Verify phone number
    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).get_property('value')

        # Click "Next" button to advance
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

        # Enter SMS code
    def enter_sms_code(self, sms_code):
        self.driver.find_element(*self.SMS_CODE_LOCATOR).send_keys(sms_code)

        # Click "Confirm"
    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

        # Step for entering a phone number
    def enter_phone_number_and_sms_code(self, phone_number, sms_code):
        self.click_phone_number_field()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        self.enter_sms_code(sms_code)
        self.click_confirm_button()

        # Click "Payment Method"
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

        # Click "Add card"
    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON_LOCATOR).click()

        # Enter a card number
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

        # Enter a CVV code
    def enter_cvv_code(self, cvv_code):
        self.driver.find_element(*self.CVV_CODE_LOCATOR).send_keys(cvv_code)

        # Click title so input fields are out of focus
    def click_title(self):
        self.driver.find_element(*self.ADDING_A_CARD_TITLE_LOCATOR).click()

        # Click "Link" button
    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

        # Close the card info window
    def close_card_info_window(self):
        self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR).click()

        # Step created for entering card information, linking a new card, and closing the card info window
    def link_new_card(self, card_number, cvv_code):
        self.click_add_card_button()
        self.enter_card_number(card_number)
        self.enter_cvv_code(cvv_code)
        self.click_title()
        self.click_link_button()
        self.close_card_info_window()

        # Verify "Card number" is correct
    def get_card_number(self):
        return self.driver.find_element(*self.CARD_NUMBER_LOCATOR).get_property('value')

        # Verify "Card code" is correct
    def get_card_code(self):
        return self.driver.find_element(*self.CVV_CODE_LOCATOR).get_property('value')

        # Enter a message for the driver
    def enter_driver_message(self, driver_message):
        self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).send_keys(driver_message)

        # Verify driver message is correct
    def get_driver_message(self):
        return self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).get_property('value')

        # Expand order requirements drop down list
    def click_order_requirements(self):
        self.driver.find_element(*self.ORDER_REQUIREMENTS_LOCATOR).click()

        # Toggle on Blanket and Handkerchief option
    def add_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR).click()

        # Verify blanket and handkerchief were added
    def check_blanket_and_handkerchief(self):
        return self.driver.find_element(*self.CHECK_BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR).get_property('checked')

        # Add an ice cream to order
    def add_ice_cream(self):
        # Begin loop - will run twice
        for i in range(2):
            ice_cream_button = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ICE_CREAM_ADD_BUTTON_LOCATOR))
            ice_cream_button.click()

        # Finalize order
    def finalize_order(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

        # Verify "Car search" modal appears after ordering
    def verify_car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL_LOCATOR).text

