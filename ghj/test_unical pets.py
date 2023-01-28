import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ficsture import login

def test_no_duplicate_pets(login):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))


    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')


    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)


    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '


    list_line = line.split(' ')


    set_list_line = set(list_line)


    a = len(list_line)
    b = len(set_list_line)


    result = a - b

    # Если количество элементов == 0 значит все питомцы уникальны
    assert result == 0

