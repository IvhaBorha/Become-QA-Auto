import pytest

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкта для керування браузером
    # driver = webdriver.Chrome(
    #     service=Service(r"/home/yivha/" + "chromedriver")
    # )

    driver = webdriver.Firefox(
        executable_path="/home/yivha/geckodriver"
    )

    #Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім'я користувача, або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильне ім'я користувача, або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakemail.com")
    

    #Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
   

    #Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    #Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    #Перевіряємо, що назва сторінки відповідає очікуваній назві
    assert driver.title =="Sign in to GitHub · GitHub"

    #Закриваємо браузер
    driver.close()


