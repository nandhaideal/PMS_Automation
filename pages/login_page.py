from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME = (By.XPATH, "//input[@placeholder='Username ']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Home page element after successful login
    HOME_PAGE_TITLE = (
        By.XPATH,
        "//*[contains(text(),'Scrum Board')]"
    )



    def login(self):

        self.driver.find_element(*self.USERNAME).send_keys(
            Config.USERNAME
        )

        time.sleep(Config.SHORT_WAIT)

        self.driver.find_element(*self.PASSWORD).send_keys(
            Config.PASSWORD
        )

        time.sleep(Config.SHORT_WAIT)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

        # Fixed: replaced time.sleep + assert with WebDriverWait
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.HOME_PAGE_TITLE)
            )
        except Exception:
            raise AssertionError("Login Failed: 'Scrum Board' not visible after 20 seconds")

try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.HOME_PAGE_TITLE)
            )
        except Exception:
            raise AssertionError("Login Failed: 'Scrum Board' not visible after 20 seconds")      