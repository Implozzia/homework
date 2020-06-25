from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = driver.find_element_by_id("book")
    button.click()

    driver.execute_script("window.scrollBy(0, 300);")

    time.sleep(1)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    find_value = driver.find_element_by_id("input_value")
    x = find_value.text
    y = calc(x)

    input = driver.find_element_by_id("answer")
    input.send_keys(y)

    submit = driver.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(20)
    driver.quit()
