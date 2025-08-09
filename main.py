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

        pages.select_supportive()
        selected_plan = pages.get_selected_plan_name()
        assert selected_plan == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        pages.fill_phone_number(data.PHONE_NUMBER)

        assert pages.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        pages.fill_card(data.CARD_NUMBER, data.CARD_CODE)

        assert pages.get_card() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        pages.comment_for_driver(data.MESSAGE_FOR_DRIVER)

        assert pages.get_message_for_driver() == 'Stop at the juice bar, please'

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        pages.order_blanket_and_handkerchiefs()

        pages.check_slider()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.select_supportive()

        for _ in range(2):
            pages.add_ice_cream()

        assert pages.get_counter_value() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)
        pages.select_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        pages.select_supportive()

        pages.fill_phone_number(data.PHONE_NUMBER)

        pages.comment_for_driver(data.MESSAGE_FOR_DRIVER)

        pages.order_taxi()

        assert pages.get_car_search_modal().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()