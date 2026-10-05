from datetime import datetime

from pages.Ghmis_creation_page.Task_Creation import Ghmis_agent, Sprint_Dropdown
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

###### LOCATORS#######  

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")

CR_BTN = (By.XPATH,"//button[text()=' CR ']")
Summary_Textbox = (By.XPATH,"//input[@formcontrolname='summary']")
Description_Textbox = (By.XPATH,"//textarea[@formcontrolname='description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
CR_NUMBER = (By.XPATH,"//input[@formcontrolname='crnumber']")
Hmis_Module_dropdown = (By.XPATH,"//input[@formcontrolname = 'module']")
Hmis_Submodule_dropdown = (By.XPATH,"//input[@formcontrolname = 'submodule']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")

Change_requestedby_dropdown = (By.XPATH,"//select[@formcontrolname='changerequestedby']")
Change_approvedby_dropdown = (By.XPATH,"//select[@formcontrolname='changeapprovedby']")
Change_Type_dropdown = (By.XPATH,"//select[@formcontrolname='changetype']")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
planned_start_date = (By.XPATH,"//input[@formcontrolname = 'plannedStart']")
planned_end_date = (By.XPATH,"//input[@formcontrolname = 'plannedEnd']")
Original_estimate = (By.XPATH,"//input[@formcontrolname = 'estimate']")
Sprint_Dropdown = (By.XPATH,"//select[@formcontrolname='sprint']")
create_button = (By.XPATH,"//button[@class='btn btn-primary']")


class CRCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)


    def Create_CR(self):
        
        self.driver.find_element(*LISTS_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*Tracker_Create_BTN).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*CR_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        task_name = "Test Task " + datetime.now().strftime("%Y%m%d_%H%M%S")
                
        self.wait.until(EC.element_to_be_clickable(Summary_Textbox)
                        ).send_keys(task_name)
                
        self.driver.find_element(*Description_Textbox).send_keys(
                            "This is a test task created for testing purposes.")
        time.sleep(Config.SHORT_WAIT)
                
        self.driver.find_element(*Assignee_Dropdown).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*Ghmis_agent).click()
        time.sleep(Config.SHORT_WAIT)
        
        self.driver.find_element(*CR_NUMBER).send_keys("CR-12345")
        
        time.sleep(Config.SHORT_WAIT)
        
        hmis_module_dropdown = self.driver.find_element(*Hmis_Module_dropdown)
        hmis_module_dropdown.click()
        time.sleep(Config.SHORT_WAIT)
        hmis_module_dropdown.send_keys("System Login")
                
        hmis_submodule_dropdown = self.driver.find_element(*Hmis_Submodule_dropdown)
        hmis_submodule_dropdown.click()
        hmis_submodule_dropdown.send_keys("Application Header")
        time.sleep(Config.SHORT_WAIT)
         
        change_requestedby_dropdown = Select(self.driver.find_element(*Change_requestedby_dropdown))
        change_requestedby_dropdown.select_by_index(1)
        time.sleep(Config.SHORT_WAIT)
        
        change_approvedby_dropdown = Select(self.driver.find_element(*Change_approvedby_dropdown))
        change_approvedby_dropdown.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        change_type_dropdown = Select(self.driver.find_element(*Change_Type_dropdown))
        change_type_dropdown.select_by_index(2)
        time.sleep(Config.SHORT_WAIT)
        
        priority_dropdown = Select(self.driver.find_element(*Priority_Dropdown))
        priority_dropdown.select_by_visible_text("High")
        time.sleep(Config.SHORT_WAIT)
        
        planned_start_date_field = self.driver.find_element(*planned_start_date)
        planned_start_date_field.send_keys("15-09-2026")
                
        planned_end_date_field = self.driver.find_element(*planned_end_date)
        planned_end_date_field.send_keys("30-09-2026")
        time.sleep(Config.SHORT_WAIT)
                
        original_estimate = self.driver.find_element(*Original_estimate)
        original_estimate.send_keys("5d")
        time.sleep(Config.SHORT_WAIT)
        
        sprint_dropdown = Select(self.driver.find_element(*Sprint_Dropdown))
        sprint_dropdown.select_by_index(1)
        time.sleep(Config.SHORT_WAIT)
        
        attachment_upload_button_element = self.driver.find_element(*attachment_upload_button)
        attachment_upload_button_element.send_keys("C:\\Users\\Nandha\\Downloads\\test_automation.png")   
                   
        
        CREATE_BTN = self.wait.until(
        EC.element_to_be_clickable(create_button)
                       )
        CREATE_BTN.click()
        
                
                            
                        