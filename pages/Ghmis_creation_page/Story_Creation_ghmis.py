from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config
from datetime import datetime

from pages.Ghmis_creation_page.Task_Creation import Ghmis_agent, Sprint_Dropdown
from pages.Ghmis_creation_page.Task_Creation import components_dropdown, Hmis_Module_dropdown, Hmis_Submodule_dropdown, project_dropdown, client_ticket_id
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

###### LOCATORS#######  

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")

Story_BTN = (By.XPATH,"//button[text()=' Story ']")
Summary_Textbox = (By.XPATH,"//input[@formcontrolname='summary']")
Description_Textbox = (By.XPATH,"//textarea[@formcontrolname='description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
Hmis_Module_dropdown = (By.XPATH,"//input[@formcontrolname = 'module']")
Hmis_Submodule_dropdown = (By.XPATH,"//input[@formcontrolname = 'submodule']")
Sprint_Dropdown = (By.XPATH,"//select[@formcontrolname='sprint']")
client_ticket_id = (By.XPATH,"//input[@formcontrolname='clientticketID']")
complexity_dropdown = (By.XPATH,"//select[@formcontrolname='complexity']")
optimistic_value_field = (By.XPATH,"//input[@formcontrolname='optimistic']")
pessimistic_value_field = (By.XPATH,"//input[@formcontrolname='pessimistic']")
most_likely_value_field = (By.XPATH,"//input[@formcontrolname='mostLikely']")
srs_reference_text_field = (By.XPATH,"//input[@formcontrolname='srsReference']")
linked_issue_dropdown = (By.XPATH,"//span[text()='Select linked issue']")
components_dropdown = (By.XPATH,"//select[@formcontrolname='components']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")
planned_start_date = (By.XPATH,"//input[@formcontrolname = 'plannedStart']")
planned_end_date = (By.XPATH,"//input[@formcontrolname = 'plannedEnd']")
create_button = (By.XPATH,"//button[@class='btn btn-primary']")


class StoryCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)


    def Create_STORY(self):
        
        self.driver.find_element(*LISTS_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*Tracker_Create_BTN).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*Story_BTN).click()
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
         
        priority_dropdown = Select(self.driver.find_element(*Priority_Dropdown))
        priority_dropdown.select_by_visible_text("High")
        time.sleep(Config.SHORT_WAIT)
        
        hmis_module_dropdown = self.driver.find_element(*Hmis_Module_dropdown)
        hmis_module_dropdown.click()
        time.sleep(Config.SHORT_WAIT)
        hmis_module_dropdown.send_keys("System Login")
                        
        hmis_submodule_dropdown = self.driver.find_element(*Hmis_Submodule_dropdown)
        hmis_submodule_dropdown.click()
        hmis_submodule_dropdown.send_keys("Application Header")
        time.sleep(Config.SHORT_WAIT)
        
        sprint_dropdown = Select(self.driver.find_element(*Sprint_Dropdown))
        sprint_dropdown.select_by_index(1)
        time.sleep(Config.SHORT_WAIT)
        
        Client_ticket_id = self.driver.find_element(*client_ticket_id)
        Client_ticket_id.send_keys("12345")
        time.sleep(Config.SHORT_WAIT)
        
        complexity_dropdown_element = Select(self.driver.find_element(*complexity_dropdown))
        complexity_dropdown_element.select_by_index(1)  
        
        optimistic_value_field_element = self.driver.find_element(*optimistic_value_field)
        optimistic_value_field_element.send_keys("4")
        
        mostlikely_value_field_element  = self.driver.find_element(*most_likely_value_field)
        mostlikely_value_field_element.send_keys("9")
        
        pessimistic_value_field_element = self.driver.find_element(*pessimistic_value_field)
        pessimistic_value_field_element.send_keys("16")
        
        srs_reference_text_field_element = self.driver.find_element(*srs_reference_text_field)
        srs_reference_text_field_element.send_keys("SRS.12345")
        
        linked_issue = self.driver.find_element(By.XPATH, "//span[normalize-space()='Select linked issue']")
        ActionChains(self.driver).move_to_element(linked_issue).click().perform()

        option = self.driver.find_element(By.XPATH, "//mat-option[contains(.,'CR-6697 - test_6')]")
        ActionChains(self.driver).move_to_element(option).click().perform()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        components_dropdown_element = Select(self.driver.find_element(*components_dropdown))
        components_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        attachment_upload_button_element = self.driver.find_element(*attachment_upload_button)
        attachment_upload_button_element.send_keys("C:\\Users\\Nandha\\Downloads\\test_automation.png")   
           
        planned_start_date_field = self.driver.find_element(*planned_start_date)
        planned_start_date_field.send_keys("15-09-2026")
        
        planned_end_date_field = self.driver.find_element(*planned_end_date)
        planned_end_date_field.send_keys("30-09-2026")
        time.sleep(Config.SHORT_WAIT)
        
        
        
        CREATE_BTN = self.wait.until(
               EC.element_to_be_clickable(create_button)
              )
                
        time.sleep(Config.LONG_WAIT)
                
        CREATE_BTN.click()
                
                
        
        
                
