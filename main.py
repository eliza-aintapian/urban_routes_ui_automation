from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages import UrbanRoutesPage

driver = webdriver.Chrome()
driver.get("https://cnt-bd24763a-2901-4257-9efa-3df7e1133158.containerhub.tripleten-services.com")
driver.maximize_window()
time.sleep(2)

page = UrbanRoutesPage(driver)

page.select_locations()
page.select_custom_option()
page.select_drive_icon()
page.book_ride()
car_name = page.choose_camping()
print("Car name:", car_name)

page.add_driver_license()
page.fill_driver_info()
page.driver.find_element(By.CSS_SELECTOR, '.modal-container').click()
#page.click_on_the_overlay()
page.submit_driver_info()
page.accept_license_info()
page.enter_payment_method()
page.add_card()
page.fill_card_info()
page.link_card()
page.click_close()
page.book_a_car()

verification_text = page.get_verification_text()
print("Verification text:", verification_text)

time.sleep(2)
driver.quit()