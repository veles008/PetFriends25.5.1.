import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def login():

    pytest.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://petfriends.skillfactory.ru/login') #логинимся
    pytest.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('fortestlesson@gmail.com')
    pytest.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('qwerty')
    pytest.driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()

