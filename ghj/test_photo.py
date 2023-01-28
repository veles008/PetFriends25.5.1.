import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ficsture import login

def test_photo_availability(login):


    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    statistic = pytest.driver.find_elements(By.CSS_SELECTOR,".\\.col-sm-4.left")


    images = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover img')


    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])


    half = number // 2


    number_a_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_a_photos += 1


    assert number_a_photos >= half
    print(f'количество фото: {number_a_photos}')
