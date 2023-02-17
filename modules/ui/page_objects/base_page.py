from selenium import webdriver

class BasePage:
    PATH = r"/home/yivha/"
    DRIVER_NAME = "geckodriver"

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=BasePage.PATH + BasePage.DRIVER_NAME
        )

    def close(self):
        self.driver.close()