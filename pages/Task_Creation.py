from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

from selenium.webdriver.support.ui import Select


###LOCATORS#######

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")

TASK_BTN = (By.XPATH,"//button[text()=' Task ']")

Summary_Textbox = (By.XPATH,"(//input[@type='text'])[1]")
Description_Textbox = (By.XPATH,"//textarea[@formcontrolname='description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
Ghmis_agent = (By.XPATH,"//span[normalize-space()='ghmis agent']")
Sprint_Dropdown = (By.XPATH,"//select[@formcontrolname='sprint']")
phase_dropdown = (By.XPATH,"//select[@formcontrolname='phase']")
subphase_dropdown = (By.XPATH,"//select[@formcontrolname='subphase']")
components_dropdown = (By.XPATH,"//select[@formcontrolname = 'components']")
Hmis_Module_dropdown = (By.XPATH,"//input[@formcontrolname = 'module']")
Hmis_Submodule_dropdown = (By.XPATH,"//input[@formcontrolname = 'submodule']")
project_dropdown = (By.XPATH,"//select[@formcontrolname='project']")
client_ticket_id = (By.XPATH,"//input[@formcontrolname='clientticketID']")
UI_Changes_dropdown = (By.XPATH,"//select[@formcontrolname = 'UIChangesRequired']")
DB_Changes_dropdown = (By.XPATH,"//select[@formcontrolname = 'DBChangesRequired']")
Api_changes_dropdown = (By.XPATH,"//select[@formcontrolname = 'APIChangesRequired']")
DB_changes_description = (By.XPATH,"//textarea[@formcontrolname = 'DBChangesDesc']")
File_name = (By.XPATH,"//input[@formcontrolname = 'FileName']")
Fixed_UI_Branchname =(By.XPATH,"//input[@formcontrolname = 'FixedUIBranchName']")
Fixed_Api_Branchname = (By.XPATH,"//input[@formcontrolname = 'FixedAPIBranchName']")
planned_start_date = (By.XPATH,"//input[@formcontrolname = 'plannedStart']")
planned_end_date = (By.XPATH,"//input[@formcontrolname = 'plannedEnd']")
Original_estimate = (By.XPATH,"//input[@formcontrolname = 'estimate']")
create_btn = (By.XPATH,"//button[text()=' Create ']")
cancel_btn = (By.XPATH,"//button[text()=' Cancel ']")
TASK_CREATED_SUCCESS_MESSAGE = (
    By.XPATH,
    "//*[contains(normalize-space(), 'Task Created Successfully')]"
)
#---------------------------------------------------------------------------------------#


class TaskCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def Create_Task(self):
        
       self.driver.find_element(*LISTS_BTN).click()
       time.sleep(Config.SHORT_WAIT)      
       self.driver.find_element(*Tracker_Create_BTN).click()
       time.sleep(Config.SHORT_WAIT)
       self.driver.find_element(*TASK_BTN).click()
       time.sleep(Config.SHORT_WAIT)
       self.driver.find_element(* Summary_Textbox).send_keys("Test Task")
       time.sleep(Config.SHORT_WAIT)
       self.driver.find_element(*Description_Textbox).send_keys("This is a test task created for testing purposes.")
       time.sleep(Config.SHORT_WAIT)   
       self.driver.find_element(*Assignee_Dropdown).click()
       time.sleep(Config.SHORT_WAIT)
       self.driver.find_element(*Ghmis_agent).click() 
       time.sleep(Config.SHORT_WAIT)
       priority_dropdown = Select(self.driver.find_element(*Priority_Dropdown))
       priority_dropdown.select_by_visible_text("High")  
       time.sleep(Config.SHORT_WAIT)  
       sprint_dropdown = Select(self.driver.find_element(*Sprint_Dropdown))
       sprint_dropdown.select_by_index(1)
       time.sleep(Config.SHORT_WAIT)
      
       Phase_dropdown = Select(self.driver.find_element(*phase_dropdown))
       Phase_dropdown.select_by_index(3)
       time.sleep(Config.SHORT_WAIT)    
       Subphase_dropdown = Select(self.driver.find_element(*subphase_dropdown))
       Subphase_dropdown.select_by_index(2)
       time.sleep(Config.MEDIUM_WAIT)
       Components_dropdown = Select(self.driver.find_element(*components_dropdown))
       Components_dropdown.select_by_index(3)
       time.sleep(Config.SHORT_WAIT)
        
       hmis_module_dropdown = self.driver.find_element(*Hmis_Module_dropdown)
       hmis_module_dropdown.click()
       time.sleep(Config.SHORT_WAIT)
       hmis_module_dropdown.send_keys(" IP Management ") 
       
       hmis_submodule_dropdown = self.driver.find_element(*Hmis_Submodule_dropdown)
       hmis_submodule_dropdown.click()
       hmis_submodule_dropdown.send_keys(" Ward Master ")
       
       time.sleep(Config.SHORT_WAIT)
       
       Project_dropdown = Select(self.driver.find_element(*project_dropdown))
       Project_dropdown.select_by_index(3)
       time.sleep(Config.SHORT_WAIT)
       
       
       self.driver.find_element(*client_ticket_id).send_keys("test_12345")
       
       ui_Changes_dropdown = Select(self.driver.find_element(*UI_Changes_dropdown))
       ui_Changes_dropdown.select_by_visible_text("yes")
       
       time.sleep(Config.SHORT_WAIT)
       
       db_Changes_dropdown = Select(self.driver.find_element(*DB_Changes_dropdown))
       db_Changes_dropdown.select_by_visible_text("yes")
       
       time.sleep(Config.SHORT_WAIT)
       
       api_changes_dropdown = Select(self.driver.find_element(*Api_changes_dropdown))
       api_changes_dropdown.select_by_visible_text("yes")
       
       time.sleep(Config.SHORT_WAIT)
       
       db_changes_description = self.driver.find_element(*DB_changes_description)
       db_changes_description.send_keys("This is a test description for database changes.")
       
       time.sleep(Config.SHORT_WAIT)
       self.driver.find_element(*File_name).send_keys("test_file.txt")

       time.sleep(Config.SHORT_WAIT)
       
       fixed_ui_branchname = self.driver.find_element(*Fixed_UI_Branchname)
       fixed_ui_branchname.send_keys("test_ui_branch")  
       
       time.sleep(Config.SHORT_WAIT)
       fixed_api_branchname = self.driver.find_element(*Fixed_Api_Branchname)  
       fixed_api_branchname.send_keys("test_api_branch")
       
       time.sleep(Config.SHORT_WAIT)
       Planned_start_date = self.driver.find_element(*planned_start_date)
       Planned_start_date.send_keys("15-09-2026")
       
       Planned_end_date = self.driver.find_element(*planned_end_date)
       Planned_end_date.send_keys("30-09-2026")
       time.sleep(Config.SHORT_WAIT)
       original_estimate = self.driver.find_element(*Original_estimate)
       original_estimate.send_keys("5d")
       
       time.sleep(Config.SHORT_WAIT)
            
       Create_btn = self.wait.until(
         EC.element_to_be_clickable(create_btn)
         )

       print("Create button is enabled:", Create_btn.is_enabled())

       Create_btn.click()

        # Verify task creation success message
       
       success_message = self.wait.until(
          EC.visibility_of_element_located(TASK_CREATED_SUCCESS_MESSAGE)
)

       print("✅ Task Created Successfully")