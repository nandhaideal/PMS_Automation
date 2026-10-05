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

EPIC_BTN = (By.XPATH," //button[text()=' Epic ']")
Summary_Textbox = (By.XPATH,"//input[@formcontrolname='summary']")
Description_Textbox = (By.XPATH,"//textarea[@formcontrolname='description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
Epic_Name_Textbox = (By.XPATH,"//input[@formcontrolname='epicname']")
client_ticket_id = (By.XPATH,"//input[@formcontrolname='clientticketID']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")

Hmis_Module_dropdown = (By.XPATH,"//input[@formcontrolname = 'module']")
Hmis_Submodule_dropdown = (By.XPATH,"//input[@formcontrolname = 'submodule']")
project_dropdown = (By.XPATH,"//select[@formcontrolname='project']")
File_name = (By.XPATH,"//input[@formcontrolname = 'FileName']")
components_dropdown = (By.XPATH,"//select[@formcontrolname = 'components']")
planned_start_date = (By.XPATH,"//input[@formcontrolname = 'plannedStart']")
planned_end_date = (By.XPATH,"//input[@formcontrolname = 'plannedEnd']")
Original_estimate = (By.XPATH,"//input[@formcontrolname = 'estimate']")
srs_reference = (By.XPATH,"//input[@placeholder='SRS Reference']")
create_button = (By.XPATH,"//button[@class='btn btn-primary']")
ROUTER_BOX = (By.XPATH, "//div[@class='router-box']")

class EpicCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)


    def Create_Epic(self):
        
        self.driver.find_element(*LISTS_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*Tracker_Create_BTN).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*EPIC_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        task_name = "Test Task " + datetime.now().strftime("%Y%m%d_%H%M%S")
        
        self.wait.until(
                    EC.element_to_be_clickable(Summary_Textbox)
                ).send_keys(task_name)
        
        self.driver.find_element(*Description_Textbox).send_keys(
                    "This is a test task created for testing purposes."
                )
        time.sleep(Config.SHORT_WAIT)
        
        self.driver.find_element(*Epic_Name_Textbox).send_keys(
                    "Test Epic " + datetime.now().strftime("%Y%m%d_%H%M%S")
                )   
        priority_dropdown = Select(self.driver.find_element(*Priority_Dropdown))
        priority_dropdown.select_by_visible_text("High")
        time.sleep(Config.SHORT_WAIT)
        
        Client_ticket_id = self.driver.find_element(*client_ticket_id)
        Client_ticket_id.send_keys("12345")
        time.sleep(Config.SHORT_WAIT)
        
        self.driver.find_element(*Assignee_Dropdown).click()
        time.sleep(Config.SHORT_WAIT)
        self.driver.find_element(*Ghmis_agent).click()
        time.sleep(Config.SHORT_WAIT)
        
        sprint_dropdown = Select(self.driver.find_element(*Sprint_Dropdown))
        sprint_dropdown.select_by_index(1)
        time.sleep(Config.SHORT_WAIT)
        
        hmis_module_dropdown = self.driver.find_element(*Hmis_Module_dropdown)
        hmis_module_dropdown.click()
        time.sleep(Config.SHORT_WAIT)
        hmis_module_dropdown.send_keys("System Login")
        
        hmis_submodule_dropdown = self.driver.find_element(*Hmis_Submodule_dropdown)
        hmis_submodule_dropdown.click()
        hmis_submodule_dropdown.send_keys("Application Header")
        time.sleep(Config.SHORT_WAIT)
        
        
        project_dropdown_element = Select(self.driver.find_element(*project_dropdown))
        project_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        
        self.driver.find_element(*File_name).send_keys("test_file.txt")
        time.sleep(Config.SHORT_WAIT)
        
        components_dropdown_element = Select(self.driver.find_element(*components_dropdown))
        components_dropdown_element.select_by_index(3)
        time.sleep(Config.SHORT_WAIT)
        
        SRS_REFERENCE = self.driver.find_element(*srs_reference)
        SRS_REFERENCE.send_keys("SRS.12345")
        
        
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
        
        
        
        router_box = self.wait.until(
               EC.visibility_of_element_located(ROUTER_BOX)
                )
        
        ActionChains(self.driver).move_to_element(router_box).perform()         
        
        
        
        CREATE_BTN = self.wait.until(
               EC.element_to_be_clickable(create_button)
              )

        # --- DEBUG ---
        print("Button disabled attr:", CREATE_BTN.get_attribute("disabled"))
        print("Button class:", CREATE_BTN.get_attribute("class"))

        invalid_fields = self.driver.find_elements(By.XPATH, "//*[contains(@class,'ng-invalid')]")
        print(f"Found {len(invalid_fields)} ng-invalid elements")
        for f in invalid_fields:
            print(" -", f.tag_name, "| formcontrolname:",
                  f.get_attribute("formcontrolname"), "| class:", f.get_attribute("class"))

        self.driver.save_screenshot("before_click.png")
        # --- END DEBUG ---

        time.sleep(Config.LONG_WAIT)
        CREATE_BTN.click()

        # capture state immediately after click, before the wait
        self.driver.save_screenshot("after_click.png")

        # confirm the dialog closed (i.e. submission was accepted)
        self.wait.until(EC.invisibility_of_element_located(create_button))
        return task_name
                
        
        
        
        
        