from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages import UrbanRoutesPage

import data
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert pages.get_from() == data.ADDRESS_FROM
        assert pages.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()
        selected_plan = pages.get_selected_plan_name()
        assert selected_plan == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        self.driver.find_element(By.XPATH, "//div[text()='Phone number']").click()
        self.driver.find_element(By.ID, "phone").send_keys(data.PHONE_NUMBER)

        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'button full')]").click()

        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(By.ID, "code").send_keys(phone_code)

        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'button') and contains(@class, 'full') and text()='Confirm']").click()

        displayed_number = self.driver.find_element(By.CSS_SELECTOR, "div.np-text").text
        assert data.PHONE_NUMBER in displayed_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        self.driver.find_element(By.XPATH, "//div[@class='pp-text' and text()='Payment method']").click()
        self.driver.find_element(By.XPATH, "//div[@class='pp-title' and text()='Add card']").click()
        self.driver.find_element(By.ID, "number").send_keys(data.CARD_NUMBER)
        self.driver.find_element(By.ID, "code").send_keys(data.CARD_CODE)

        #clicking on another element to activate the "Link" button
        self.driver.find_element(By.XPATH, "//div[@class='head' and text()='Adding a card']").click()

#Ensure the "Link" button becomes clickable. not sure how to ensure that
        self.driver.find_element(By.XPATH,"//button[@type='submit' and contains(@class, 'button full') and text()='Link']").click()

        #closing the little popup window after adding the card
        self.driver.find_element(By.CSS_SELECTOR, "button.close-button.section-close").click()

        displayed_payment_method = self.driver.find_element(By.CSS_SELECTOR, "div.pp-value-text").text
        assert displayed_payment_method == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        self.driver.find_element(By.ID, "comment").send_keys(data.MESSAGE_FOR_DRIVER)

        comment_to_driver = self.driver.find_element(By.ID, "comment").get_attribute("value")
        assert comment_to_driver == 'Stop at the juice bar, please'

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        slider_checkbox = self.driver.find_element(By.CLASS_NAME, 'switch')
        slider_checkbox.click()

        is_checked = slider_checkbox.get_property("checked")
        assert is_checked is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        for _ in range(2):
            plus_button = self.driver.find_element(By.CSS_SELECTOR, ".counter-plus")
            plus_button.click()

        counter_value = self.driver.find_element(By.CSS_SELECTOR, ".counter-value").text
        assert counter_value == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
#the code repeats itself. can we reduce it?
        self.driver.find_element(By.XPATH, "//button[text()='Call a taxi']").click()
        self.driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']").click()

        self.driver.find_element(By.XPATH, "//div[text()='Phone number']").click()
        self.driver.find_element(By.ID, "phone").send_keys(data.PHONE_NUMBER)

        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'button full')]").click()

        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(By.ID, "code").send_keys(phone_code)

        displayed_number = self.driver.find_element(By.CSS_SELECTOR, "div.np-text").text
        assert data.PHONE_NUMBER in displayed_number
#same here. I literally copy-pasted it
        self.driver.find_element(By.ID, "comment").send_keys(data.MESSAGE_FOR_DRIVER)

        comment_to_driver = self.driver.find_element(By.ID, "comment").get_attribute("value")
        assert comment_to_driver == 'Stop at the juice bar, please'

        self.driver.find_element(By.XPATH, "//span[@class='smart-button-main' and text()='Order']").click()

        car_search_modal = self.driver.find_element(By.XPATH, "//div[@class='order-header-title' and text()='Car search']")
        assert car_search_modal.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()