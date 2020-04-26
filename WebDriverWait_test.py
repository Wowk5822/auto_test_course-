import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    #чекаємо поки ціна буде 100
    price = WebDriverWait(driver,13).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))

    #коли ціна буде 100 то шукаємо кнопку і натискаємо
    button = driver.find_element_by_css_selector("#book")
    button.click()

    #шукаємо значення х для розрахунку формули
    x = driver.find_element_by_id("input_value").text
    y = int(x)
    print(y)

    answer = math.log(math.fabs(math.sin(y) * 12))
    z = str(answer)
    print(z)

    write_answer = driver.find_element_by_id("answer")
    write_answer.send_keys(z)

    submit2 = driver.find_element_by_css_selector("#solve")
    submit2.click()

    #переключаємось на вікно повідомлення де показується результат
    rezultat = driver.switch_to.alert
    rezultat_text = rezultat.text
    rezultat.accept()
    print(rezultat_text.split(': ')[-1])  #друкуємо результат 





finally:
    time.sleep(15)
    driver.quit()