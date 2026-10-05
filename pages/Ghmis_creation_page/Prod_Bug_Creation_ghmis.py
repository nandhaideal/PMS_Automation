from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")

Status_change_btn = (By.XPATH,"(//button[text()=' Change Status '])[1]")
InProgress_Status_btn = (By.XPATH,"//button[text()=' In Progress ']")
