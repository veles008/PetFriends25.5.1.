import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ficsture import login

def test_all_pets_are_present(login):
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))


    statistic = pytest.driver.find_elements(By.CSS_SELECTOR,".\\.col-sm-4.left")

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))


    pets = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')


    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # количество карточек питомцев
    number_of_pets = len(pets)

    #  количество питомцев из статистики == количеством карточек питомцев
    assert number == number_of_pets

