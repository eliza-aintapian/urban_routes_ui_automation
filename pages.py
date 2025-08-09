from selenium.webdriver.common.by import By
import time

import data
import helpers

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_LOCATOR = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")
    ACTIVE_PLAN_LOCATOR = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    PHONE_NUMBER_LOCATOR = (By.XPATH, "//div[text()='Phone number']")
    PHONE_INPUT_LOCATOR = (By.ID, "phone")
    PHONE_SUBMIT_LOCATOR = (By.XPATH, "//button[@type='submit' and contains(@class, 'button full')]")
    PHONE_CODE_LOCATOR = (By.ID, "code")
    PHONE_CODE_SUBMIT_LOCATOR = (By.XPATH, "//button[@type='submit' and contains(@class, 'button') and contains(@class, 'full') and text()='Confirm']")
    PHONE_NUMBER_DISPLAYED_LOCATOR = (By.CSS_SELECTOR, "div.np-text")
    CARD_LOCATOR = (By.XPATH, "//div[@class='pp-text' and text()='Payment method']")
    CARD_ADD_LOCATOR = (By.XPATH, "//div[@class='pp-title' and text()='Add card']")
    CARD_NUMBER_LOCATOR = (By.ID, "number")
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, "#code.card-input")
    TITLE_ADD_A_CARD_LOCATOR = (By.XPATH, "//div[@class='head' and text()='Adding a card']")
    CARD_LINK_LOCATOR = (By.XPATH,"//button[@type='submit' and contains(@class, 'button full') and text()='Link']")
    CARD_OPTION_DISPLAYED_LOCATOR = (By.CSS_SELECTOR, "div.pp-value-text")
    MESSAGE_TO_DRIVER_LOCATOR = (By.ID, "comment")
    BLANKET_SLIDER_LOCATOR = (By.CSS_SELECTOR, '.slider.round')
    CHECKBOX_LOCATOR = (By.CSS_SELECTOR, '[type=checkbox].switch-input')
    PLUS_BUTTON_LOCATOR = (By.CLASS_NAME, "counter-plus")
    COUNTER_VALUE_LOCATOR = (By.CSS_SELECTOR, ".counter-value")
    ORDER_BUTTON_LOCATOR = (By.CLASS_NAME, "smart-button-wrapper")
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, "//div[@class='order-header-title' and text()='Car search']")

    def __init__(self, driver):
        self.driver = driver

    def select_locations(self, from_address, to_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)
        time.sleep(1)
        self.driver.find_element(*self.CALL_A_TAXI_LOCATOR).click()

    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    def select_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()

    def get_selected_plan_name(self):
        active_plan = self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR)
        return active_plan.text

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).send_keys(phone)
        self.driver.find_element(*self.PHONE_SUBMIT_LOCATOR).click()

        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(phone_code)

        self.driver.find_element(*self.PHONE_CODE_SUBMIT_LOCATOR).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_DISPLAYED_LOCATOR).text

    def fill_card(self, card, code):
        self.driver.find_element(*self.CARD_LOCATOR).click()
        self.driver.find_element(*self.CARD_ADD_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(code)

        self.driver.find_element(*self.TITLE_ADD_A_CARD_LOCATOR).click()

        self.driver.find_element(*self.CARD_LINK_LOCATOR).click()

    def get_card(self):
        return self.driver.find_element(*self.CARD_OPTION_DISPLAYED_LOCATOR).text

    def comment_for_driver(self, message):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER_LOCATOR).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_TO_DRIVER_LOCATOR).get_property("value")

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def check_slider(self):
        is_checked = self.driver.find_element(*self.CHECKBOX_LOCATOR).get_property("checked")
        assert is_checked is True

    def add_ice_cream(self):
        self.driver.find_element(*self.PLUS_BUTTON_LOCATOR).click()

    def get_counter_value(self):
        return self.driver.find_element(*self.COUNTER_VALUE_LOCATOR).text

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def get_car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL_LOCATOR)