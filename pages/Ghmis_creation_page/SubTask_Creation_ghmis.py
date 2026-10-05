from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config
from datetime import datetime
from selenium.common.exceptions import TimeoutException

from pages.Ghmis_creation_page.Task_Creation import Ghmis_agent, Sprint_Dropdown
from pages.Ghmis_creation_page.Task_Creation import components_dropdown, Hmis_Module_dropdown, Hmis_Submodule_dropdown, project_dropdown, client_ticket_id
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config
from datetime import datetime

from pages.Ghmis_creation_page.Task_Creation import Ghmis_agent, Sprint_Dropdown
from pages.Ghmis_creation_page.Task_Creation import components_dropdown, Hmis_Module_dropdown, Hmis_Submodule_dropdown, project_dropdown, client_ticket_id
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


####----------Locators--------------------------------------

LISTS_BTN = (By.XPATH,"//span[text()='Lists']")
change_status_btn = (By.XPATH,"(//button[text()=' Change Status '])[1]")
Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")
Status_change_btn = (By.XPATH,"(//button[@type='button'])[16]")
InProgress_Status_btn = (By.XPATH,"//button[text()=' In Progress ']")
SubTask_Btn = (By.XPATH,"//button[text()=' + Sub-task ']")
open_backlog_btn = (By.XPATH,"//button[text()=' Open/ Backlog ']")
Story_link = (By.XPATH,"//span[text()=' GHMIS-6862 ']")
Summary_Textbox = (By.XPATH,"//input[@formcontrolname='summary']")
Description_Textbox = (By.XPATH,"//textarea[@formcontrolname='description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
project_dropdown = (By.XPATH,"//select[@formcontrolname='project']")
client_ticket_id = (By.XPATH,"//input[@formcontrolname='clientticketID']")
phase_dropdown = (By.XPATH,"//select[@formcontrolname='phase']")
subphase_dropdown = (By.XPATH,"//select[@formcontrolname='subphase']")
components_dropdown = (By.XPATH,"//select[@formcontrolname = 'components']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")
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
create_btn = (By.XPATH,"//button[@class='btn btn-primary shadow']")


class SubTask_Creation_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)
      
      
    def _is_present(self, locator, timeout=5):
        
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False  
        
    def Create_SubTask(self):
      
        self.driver.find_element(*LISTS_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
      
        story = self.wait.until(EC.element_to_be_clickable(Story_link))
        ActionChains(self.driver).move_to_element(story).click().perform()

# Change status only if the story is still in Open Backlog
        if self._is_present(open_backlog_btn):
          print("Story is in Open Backlog. Changing status to In Progress.")

          backlog_btn = self.wait.until(
           EC.element_to_be_clickable(open_backlog_btn),
           message="open_backlog_btn not clickable"
            )
          ActionChains(self.driver).move_to_element(backlog_btn).click().perform()

          in_progress = self.wait.until(
          EC.element_to_be_clickable(InProgress_Status_btn),
           message="InProgress_Status_btn not clickable"
            )
          ActionChains(self.driver).move_to_element(in_progress).click().perform()

          change_btn = self.wait.until(
          EC.element_to_be_clickable(change_status_btn),
          message="change_status_btn not clickable"
          )
          ActionChains(self.driver).move_to_element(change_btn).click().perform()

    # Wait until the status has actually changed (backlog button gone)
          self.wait.until(
        EC.invisibility_of_element_located(open_backlog_btn),
        message="Status did not change from Open Backlog"
        )

        else:
         print("Story is already In Progress. Skipping status change.")

         subtask_btn = self.wait.until(
         EC.element_to_be_clickable(SubTask_Btn),
          message="SubTask_Btn not clickable"
              )
        ActionChains(self.driver).move_to_element(subtask_btn).click().perform()
       
        task_name = "Test Task " + datetime.now().strftime("%Y%m%d_%H%M%S")
              
        self.wait.until(
                          EC.element_to_be_clickable(Summary_Textbox)
                      ).send_keys(task_name)
              
        self.driver.find_element(*Description_Textbox).send_keys(
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
         
        project_dropdown_element = Select(self.driver.find_element(*project_dropdown))
        project_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
         
         
         
         
        Client_ticket_id = self.driver.find_element(*client_ticket_id)
        Client_ticket_id.send_keys("12345")
        time.sleep(Config.SHORT_WAIT)
                      
        phase_dropdown_element = Select(self.driver.find_element(*phase_dropdown))
        phase_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        subphase_dropdown_element = Select(self.driver.find_element(*subphase_dropdown))
        subphase_dropdown_element.select_by_index(2)
        time.sleep(Config.MEDIUM_WAIT)
        
        components_dropdown_element = Select(self.driver.find_element(*components_dropdown))
        components_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        
        ui_changes_dropdown = Select(self.driver.find_element(*UI_Changes_dropdown))
        ui_changes_dropdown.select_by_visible_text("yes")
        time.sleep(Config.SHORT_WAIT)
        
        db_changes_dropdown = Select(self.driver.find_element(*DB_Changes_dropdown))
        db_changes_dropdown.select_by_visible_text("yes")
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
        
        planned_start_date_field = self.driver.find_element(*planned_start_date)
        planned_start_date_field.send_keys("15-09-2026")
        
        planned_end_date_field = self.driver.find_element(*planned_end_date)
        planned_end_date_field.send_keys("30-09-2026")
        time.sleep(Config.SHORT_WAIT)
        
        original_estimate = self.driver.find_element(*Original_estimate)
        original_estimate.send_keys("5d")
        time.sleep(Config.SHORT_WAIT)
        
        
        CREATE_BTN = self.wait.until(
               EC.element_to_be_clickable(create_btn)
              )
                
        time.sleep(Config.LONG_WAIT)
                
        CREATE_BTN.click()
                
        
              
      
      
      