from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")
linked_issue_dropdown = (By.XPATH,"//span[text()='Select linked issue']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")
Summary_Textbox = (By.XPATH,"(//input[@type='text'])[1]")
Status_change_btn = (By.XPATH,"(//button[text()=' Change Status '])[1]")
InProgress_Status_btn = (By.XPATH,"//button[text()=' In Progress ']")
Prod_bug_btn = (By.XPATH,"//button[text()=' Prod Bug ']")
Defect_Description_Textbox = (By.XPATH,"//div[@data-placeholder='Improve description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
Ghmis_agent = (By.XPATH,"//span[normalize-space()='ghmis agent']")
phase_dropdown = (By.XPATH,"//select[@formcontrolname='Phase']")
subphase_dropdown = (By.XPATH,"//select[@formcontrolname='Subphase']")
Sprint_Dropdown = (By.XPATH,"//select[@formcontrolname='sprint']")
cause_of_defect_dropdown = (By.XPATH,"//select[@formcontrolname='causeofdefect']")
severity_dropdown = (By.XPATH,"//select[@formcontrolname='Severity']")
origin_dropdown = (By.XPATH,"//select[@formcontrolname='Origin']")
defect_type_dropdown =(By.XPATH,"//select[@formcontrolname='Defecttype']")
defect_environment_dropdown = (By.XPATH,"//select[@formcontrolname='Defectenvironment']")
Hmis_Module_dropdown = (By.XPATH,"//input[@formcontrolname = 'module']")
Hmis_Submodule_dropdown = (By.XPATH,"//input[@formcontrolname = 'submodule']")
Linked_issue_subtask = (By.XPATH,"//span[text()=' SUBTASK-7026 - Test_09090 ']")
planned_start_date = (By.XPATH,"//input[@formcontrolname = 'plannedStart']")
planned_end_date = (By.XPATH,"//input[@formcontrolname = 'plannedEnd']")
Original_estimate = (By.XPATH,"//input[@formcontrolname = 'estimate']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")
create_button = (By.XPATH,"//button[@class='btn btn-primary']")


class ProdBugCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)

    def Create_ProdBug(self):

        self.driver.find_element(*LISTS_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*Tracker_Create_BTN).click()
        time.sleep(Config.SHORT_WAIT)
        
        
        self.driver.find_element(*Prod_bug_btn).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        
        task_name = "Test Task " + datetime.now().strftime("%Y%m%d_%H%M%S")
        
        self.wait.until(
                    EC.element_to_be_clickable(Summary_Textbox)
                ).send_keys(task_name)
        
         
        self.driver.find_element(*Defect_Description_Textbox).send_keys(
                         "This is a test task created for testing purposes."
                     )
        time.sleep(Config.SHORT_WAIT)
        
        self.driver.find_element(*Assignee_Dropdown).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*Ghmis_agent).click()
        time.sleep(Config.SHORT_WAIT)
        
        priority_dropdown = Select(self.driver.find_element(*Priority_Dropdown))
        priority_dropdown.select_by_visible_text("High")
        time.sleep(Config.SHORT_WAIT)
        
        phase_dropdown_element = Select(self.driver.find_element(*phase_dropdown))
        phase_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        subphase_dropdown_element = Select(self.driver.find_element(*subphase_dropdown))
        subphase_dropdown_element.select_by_index(2)
        time.sleep(Config.MEDIUM_WAIT)
        
        sprint_dropdown = Select(self.driver.find_element(*Sprint_Dropdown))
        sprint_dropdown.select_by_index(1)
        time.sleep(Config.SHORT_WAIT)
        
        cause_of_defect_dropdown_element = Select(self.driver.find_element(*cause_of_defect_dropdown))
        cause_of_defect_dropdown_element.select_by_index(2)
        time.sleep(Config.MEDIUM_WAIT)  
        
        severity_dropdown_element = Select(self.driver.find_element(*severity_dropdown))
        severity_dropdown_element.select_by_index(2)    
        
        origin_dropdown_element = Select(self.driver.find_element(*origin_dropdown))
        origin_dropdown_element.select_by_index(1)  
        time.sleep(Config.MEDIUM_WAIT)
        
        defect_type_dropdown_element = Select(self.driver.find_element(*defect_type_dropdown))
        defect_type_dropdown_element.select_by_index(2)
        time.sleep(Config.MEDIUM_WAIT)
        
        defect_environment_dropdown_element = Select(self.driver.find_element(*defect_environment_dropdown))
        defect_environment_dropdown_element.select_by_index(2)
        time.sleep(Config.MEDIUM_WAIT)
        
       
        hmis_module_dropdown = self.driver.find_element(*Hmis_Module_dropdown)
        hmis_module_dropdown.click()
        time.sleep(Config.SHORT_WAIT)
        hmis_module_dropdown.send_keys("System Login")

        hmis_submodule_dropdown = self.driver.find_element(*Hmis_Submodule_dropdown)
        hmis_submodule_dropdown.click()
        hmis_submodule_dropdown.send_keys("Application Header")
        time.sleep(Config.SHORT_WAIT)

        
        self.driver.find_element(*linked_issue_dropdown).click()
        time.sleep(Config.MEDIUM_WAIT)
           
        self.driver.find_element(*Linked_issue_subtask).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        planned_start_date_field = self.driver.find_element(*planned_start_date)
        planned_start_date_field.send_keys("15-09-2026")
        
        planned_end_date_field = self.driver.find_element(*planned_end_date)
        planned_end_date_field.send_keys("30-09-2026")
        time.sleep(Config.SHORT_WAIT)
        
        original_estimate = self.driver.find_element(*Original_estimate)
        original_estimate.send_keys("5d")
        time.sleep(Config.SHORT_WAIT)
              
        attachment_upload_button_element = self.driver.find_element(*attachment_upload_button)
        attachment_upload_button_element.send_keys("C:\\Users\\Nandha\\Downloads\\test_automation.png") 
        
        
        CREATE_BTN = self.wait.until(
                    EC.element_to_be_clickable(create_button)
                   )
                     
        time.sleep(Config.LONG_WAIT)
                     
        CREATE_BTN.click()    
             