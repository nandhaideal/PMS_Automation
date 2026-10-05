from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#####-----------Locators------------------###############
LISTS_BTN = (By.XPATH,"//span[text()='Lists']")

Tracker_Create_BTN = (By.XPATH,"//span[text()=' add ']")

Status_change_btn = (By.XPATH,"(//button[text()=' Change Status '])[1]")
InProgress_Status_btn = (By.XPATH,"//button[text()=' In Progress ']")
Design_to_do_btn = (By.XPATH,"//button[text()=' Design To-Do ']")
Design_in_progress_btn = (By.XPATH,"//button[text()=' Design In Progress ']")

Lists_Bug_Btn = (By.XPATH,"//button[text()=' Bug ']")
back_btn = (By.XPATH,"//span[text()='Back']")

subtask_link = (By.XPATH,"//span[text()=' GHMIS-7026 ']")
Summary_Textbox = (By.XPATH,"(//input[@type='text'])[1]")
Defect_Description_Textbox = (By.XPATH,"//div[@data-placeholder='Improve description']")
Assignee_Dropdown = (By.XPATH,"(//button[@class='assignee-btn'])[1]")
Priority_Dropdown = (By.XPATH,"//select[@formcontrolname = 'priority']")
Ghmis_agent = (By.XPATH,"//span[normalize-space()='ghmis agent']")
project_dropdown = (By.XPATH,"//select[@formcontrolname='project']")
Sprint_Dropdown = (By.XPATH,"//select[@formcontrolname='sprint']")
phase_dropdown = (By.XPATH,"//select[@formcontrolname='Phase']")
subphase_dropdown = (By.XPATH,"//select[@formcontrolname='Subphase']")
severity_of_defect_dropdown = (By.XPATH,"//select[@formcontrolname='Severity']")
origin_dropdown = (By.XPATH,"//select[@formcontrolname='Origin']")
defect_type_dropdown =(By.XPATH,"//select[@formcontrolname='Defecttype']")
defect_environment_dropdown = (By.XPATH,"//select[@formcontrolname='Defectenvironment']")
build_versions_dropdown = (By.XPATH,"//select[@formcontrolname='buildVersions']")
test_scenario_id_dropdown = (By.XPATH,"//select[@formcontrolname='TestScenarioID']")
db_changes_required_dropdown = (By.XPATH,"//select[@formcontrolname='DBChangesRequired']")
components_dropdown = (By.XPATH,"//select[@formcontrolname='components']")
linked_issue_dropdown = (By.XPATH,"//span[text()='Select linked issue']")
client_ticket_id = (By.XPATH,"//input[@formcontrolname='clientticketID']")
platform_dropdown = (By.XPATH,"//select[@formcontrolname='Platform']")
os_type_dropdown = (By.XPATH,"//select[@formcontrolname='ostype']")
bug_raised_team_dropdown = (By.XPATH,"//select[@formcontrolname='BugRaisedTeam']")
bug_raised_on_datepicker = (By.XPATH,"//input[@formcontrolname='BugRaisedOn']")
fixed_by_dropdown = (By.XPATH,"//input[@formcontrolname='FixedBy']")
create_button = (By.XPATH,"//button[@class='btn btn-primary']")
open_backlog_btn = (By.XPATH,"//button[text()=' Open/ Backlog ']")
Linked_issue_subtask = (By.XPATH,"//span[text()=' SUBTASK-7026 - Test_09090 ']")
Subtask_design_to_do_btn = (By.XPATH,"//button[text()=' Design To-Do ']")
Design_in_progress_btn = (By.XPATH,"//button[text()=' Design In Progress ']")
design_to_do_status_btn = (By.XPATH,"(//button[@type='button'])[16]")
design_to_button =(By.XPATH,"//button[@class='btn btn-sm dropdown-toggle btn-primary']")
attachment_upload_button = (By.XPATH,"//input[@type='file']")


#20260929_175344 20260929_163246


class BugCreationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.LONG_WAIT)

    def Create_Bug(self):


     self.driver.find_element(*LISTS_BTN).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*subtask_link).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*open_backlog_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     
     self.driver.find_element(*Design_to_do_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Status_change_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*design_to_button).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Design_in_progress_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Status_change_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*back_btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Tracker_Create_BTN).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Lists_Bug_Btn).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     task_name = "Test Task " + datetime.now().strftime("%Y%m%d_%H%M%S")
     
     self.wait.until(
                 EC.element_to_be_clickable(Summary_Textbox)
             ).send_keys(task_name)
     
     self.driver.find_element(*Defect_Description_Textbox).send_keys(
                 "This is a test task created for testing purposes."
             )
     time.sleep(Config.SHORT_WAIT)
     
     project_dropdown_element = Select(self.driver.find_element(*project_dropdown))
     project_dropdown_element.select_by_index(3)
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

     severity_of_defect_dropdown_element = Select(self.driver.find_element(*severity_of_defect_dropdown))
     severity_of_defect_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     Origin_dropdown_element = Select(self.driver.find_element(*origin_dropdown))
     Origin_dropdown_element.select_by_index(1)
     time.sleep(Config.MEDIUM_WAIT)
     
     Defect_Type_element = Select(self.driver.find_element(*defect_type_dropdown))
     Defect_Type_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     defect_environment_dropdown_element = Select(self.driver.find_element(*defect_environment_dropdown))
     defect_environment_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     build_versions_dropdown_element = Select(self.driver.find_element(*build_versions_dropdown))
     build_versions_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     test_scenario_id_dropdown_element = Select(self.driver.find_element(*test_scenario_id_dropdown))
     test_scenario_id_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     db_changes_required_dropdown_element = Select(self.driver.find_element(*db_changes_required_dropdown))
     db_changes_required_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     components_dropdown_element = Select(self.driver.find_element(*components_dropdown))
     components_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*linked_issue_dropdown).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*Linked_issue_subtask).click()
     time.sleep(Config.MEDIUM_WAIT)
     
     self.driver.find_element(*client_ticket_id).send_keys("testing")
     time.sleep(Config.MEDIUM_WAIT)
     
     platform_dropdown_element = Select(self.driver.find_element(*platform_dropdown))

     platform_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     os_type_dropdown_element = Select(self.driver.find_element(*os_type_dropdown))
     os_type_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)                                        
     
     
     bug_raised_team_dropdown_element = Select(self.driver.find_element(*bug_raised_team_dropdown))
     bug_raised_team_dropdown_element.select_by_index(2)
     time.sleep(Config.MEDIUM_WAIT)
     
     bug_raised_on_datepicker_element = self.driver.find_element(*bug_raised_on_datepicker)
     bug_raised_on_datepicker_element.send_keys("09-10-2026")
     
     fixed_by_dropdown_element = self.driver.find_element(*fixed_by_dropdown)
     fixed_by_dropdown_element.send_keys("test")
     time.sleep(Config.MEDIUM_WAIT)
     
     attachment_upload_button_element = self.driver.find_element(*attachment_upload_button)
     attachment_upload_button_element.send_keys("C:\\Users\\Nandha\\Downloads\\test_automation.png")   
             
     
     CREATE_BTN = self.wait.until(
            EC.element_to_be_clickable(create_button)
           )
             
     time.sleep(Config.LONG_WAIT)
             
     CREATE_BTN.click()
             
     
     
     
     
     
             

