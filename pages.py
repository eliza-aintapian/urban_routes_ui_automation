from selenium.webdriver.common.by import By
import time

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedan")]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[3]/div[1]/div')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')

    def __init__(self, driver):
        self.driver = driver

    def select_locations(self, from_address, to_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)
        time.sleep(2)

    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    def get_selected_plan_name(self):
        active_plan = self.driver.find_element(By.CSS_SELECTOR, '.tcard.active .tcard-title')
        return active_plan.text




    """def select_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()
        time.sleep(2)

    def select_drive_icon(self):
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()
        time.sleep(2)

    def book_ride(self):
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()
        time.sleep(2)

    def choose_camping(self):
        self.driver.find_element(*self.CAMPING_LOCATOR).click()
        time.sleep(2)
        car_name = self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text
        return car_name

    def add_driver_license(self):
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()
        time.sleep(2)

    def fill_driver_info(self):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys("John")
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys("Doe")
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys("01/01/1990")
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys("PHONE_NUMBER")
        time.sleep(2)

    def submit_driver_info(self):
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()
        time.sleep(2)

    def click_on_the_overlay(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]').click()

    def accept_license_info(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/button[2]').click()

    def enter_payment_method(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[3]/div[2]/div[1]').click()

    def add_card(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]').click()

    def fill_card_info(self):
        self.driver.find_element(By.ID, 'number').send_keys(CARD_NUMBER)
        self.driver.find_element(By.ID, 'code').send_keys(CARD_CODE)
        time.sleep(1)

    def link_card(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]').click()

    def click_close(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button').click()
        time.sleep(1)

    def book_a_car(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]').click()

    def get_verification_text(self):
        return self.driver.find_element(By.CLASS_NAME, "sms-verification__title").text"""
