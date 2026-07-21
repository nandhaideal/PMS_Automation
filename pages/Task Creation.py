from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config

class TrackerType:
   
   
    def __init__(self, driver):
        self.driver = driver

   
    """---------------------------Creating TASK-----------------------------------------------""" 
          
          
    FILTER_BY_PROJECTS = (
        By.XPATH,
        "//mat-label[text()='Filter by Projects']"
            
        )
        
    DESELECT_ALL = (
         By.XPATH,
         "//mat-option[@id='mat-option-0']"   
        )
        
        
        
    OSS_CHECKBOX = (
        By.XPATH,
        "//mat-option[@id='mat-option-4']"
        
          )    
    
    
    
    
    
    
    

    def Task_creation(self):
        
        self.driver.find_element(*self.FILTER_BY_PROJECTS).click()
        
        self.driver.find_element(*self.DESELECT_ALL).click()
        
        self.driver.find_element(*self.OSS_CHECKBOX).click()
        
        time.sleep(Config.MEDIUM_WAIT)

        
        
        
        
        
        
        
        
        
        SCRUM_BOARD_TEAMS = [
        
        " GHMIS ",
        " OSS ",
        " PDS ",
        " UPEX PRODUCTION TEAM ",
        " UPEX PAYMENT TEAM " ,
        " UPEX DISTRIBUTION TEAM ", 
        " UPEX LICENSE TEAM "  ,
        " AI/ML Team "    ,
        ]  
    GT_TEAMS = [
    
    
       " Service-Desk ",
       " IT Support ",
       " IT Infra ",
       " UI/UX Design Project ",
       " R&D Software & Support "
       " R&D Product Design & Development "
    ]
    