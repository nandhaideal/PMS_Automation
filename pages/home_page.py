from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.config import Config
import pytest
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    BOARD_TITLE = (
        By.XPATH,
        "//*[contains(text(),'Scrum Board')]"
    )

    GT_BOARD = (
        By.XPATH,
        "//*[contains(text(),'GT Board')]"
    )

    BUGS_BOARD = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card board-item-card'])[3]"
    )

    HOME_BUTTON = (
        By.XPATH,
        "//button[@class='glass-btn glow']"
    )
    FILTER_BY_PROJECTS = (
        By.XPATH,
        "//mat-label[text()='Filter by Projects']"
            
        )
    
    """ALL_PROJECT_OPTIONS = (
    By.XPATH,
         "//span[normalize-space()='GHMIS'] | "
         "//span[normalize-space()='IT Infra'] | "
         "//span[normalize-space()='IT Support'] | "
         "//span[normalize-space()='OSS'] | "
         "//span[normalize-space()='PDS'] | "
         "//span[normalize-space()='R&D Product Design & Development'] | "
         "//span[normalize-space()='R&D Software & Support'] | "
         "//span[normalize-space()='DISTRIBUTION TEAM'] | "
         "//span[normalize-space()='AI/ML']"
         
        )"""

        
    DESELECT_ALL = (
         By.XPATH,
         "//mat-option[@id='mat-option-0']"   
        )
        
        
        
    OSS_CHECKBOX = (
        By.XPATH,
        "//mat-option[@id='mat-option-4']"
        
    )   
    
    CLICK_ON_HOMEPAGE = (
        By.XPATH,
        "//body[@class='mat-typography']"
    )
        
    CLICK_ON_SUMMARY_PAGE = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
    USER_PROFILE_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger user-avatar-btn']"
    )
    
    USER_PROFILE_NAME = (
        By.XPATH,
        "//div[@class='profile-header']"
    )
    
    VIEW_PROFILE_BTN = (
        By.XPATH,
        "(//button[@class='mat-mdc-menu-item mat-focus-indicator'])[1]"
        
    )
    THEME_BLUE_DOT_BTN = (
        By.XPATH,
        "//button[@class='theme-dot blue']"
    )
    THEME_DOT_DARK = (
        
        By.XPATH,
        "//button[@class='theme-dot dark']"
    )
    
    THEME_DOT_GREEN = (
        
        By.XPATH,
        "//button[@class='theme-dot green']"
    )
    CHANGE_PASSWORD_BTN = (
        
        By.XPATH,
        "(//button[@class='mat-mdc-menu-item mat-focus-indicator'])[2]"
    )
    
    LOG_OUT_BTN = (
        By.XPATH,
        "//*[contains(text(),'Logout')]"
    )
    
#       ------------Create Button------------------

    CREATE_BTN = (
        By.XPATH,
        "//span[text()='Create']"
    )

    TASK_BTN = (
        By.XPATH,
        "//button[text()=' Task ']"
    )

    BUG_BTN = (
        By.XPATH,
        "//button[@class='btn bug-btn']"
    )

    PROD_BUG = (
        By.XPATH,
        "//button[@class='btn prod-btn']"
    )

    CR_BTN = (
        By.XPATH,
        "//button[@class='btn cr-btn']"
    )

    STORY_BTN = (
        By.XPATH,
        "//button[@class='btn story-btn']"
    )

    EPIC_BTN = (
        By.XPATH,
        "//button[@class='btn epic-btn']"
    )

    CLOSE_ICON = (
        By.XPATH,
        "//button[@class='close-btn']"
    )

####-------------------SCRUM BOARD---------------------------------

    SCRUM_BOARD = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card board-item-card'][1])"
    )

####----------Active sprint page------------------------------
   
    TRACKER_TYPE = (
        By.XPATH,
        "//div[@class='mat-mdc-form-field-flex']"
    )

    COMPLETE_SPRINT = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )

    SPRINT_DETAILS_BTN = (
        By.XPATH,
        "//button[@class='info-btn mdc-fab mat-mdc-fab-base mdc-fab--mini mat-mdc-mini-fab mat-accent mat-mdc-button-base']"
    )
    
    SPRINT_DETAILS_CHIP = (
        By.XPATH,
        "//div[contains(@class,'sprint-chip')]"
    )
    
    TO_DO = (
        By.XPATH,
        "(//div[contains(@class,'cdk-drop-list') and contains(@class,'column')])[1]"
    )
    IN_PROGRESS = (
        By.ID, "inProgressList"
    )
    DONE = (
        By.ID, "doneList"
    )
    SPRINT_DETAILS_DETACH_RADIO_BUTTON = (
        By.XPATH,
        "//*[normalize-space()='Detach']"
    )
    SPRINT_DETAILS_MOVETOSPRINT_RADIO_BUTTON = (
        By.XPATH,
        "//*[normalize-space()='Move to next sprint']"
    )
    SPRINT_DETAILS_ITEMS_PER_PAGE_DROPDOWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    SPRINT_DETAILS_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'close-btn')]"
    )
    SPRINT_DETAILS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[contains(@class,'mat-mdc-icon-button')])[4]"
    )
    SPRINT_DETAILS_FULL_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[contains(@class,'mat-mdc-icon-button')])[7]"
    )
    SPRINT_DETAILS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[contains(@class,'mat-mdc-icon-button')])[5]"
    )
    SPRINT_DETAILS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[contains(@class,'mat-mdc-icon-button')])[6]"
    )
    SPRINT_DETAILS_CANCEL_BUTTON = (
        By.XPATH,
        "(//button[@class='mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base'])[7]"
    )

###---------------SUMMARY Page--------------------------------------

    SUMMARY = (
        By.XPATH,
        "//span[normalize-space()='Summary']"
    )

    TOTAL_ISSUES = (
        By.XPATH,
        "//mat-card[contains(@class,'kpi-card') and contains(@class,'total')]"
    )

    OPEN_ISSUES = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card open']"
    )

    CLOSED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card closed']"
    )

    UPDATED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card overdue']"
    )

    DATE_FILTER = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger export-btn mdc-button mdc-button--raised mat-mdc-raised-button mat-unthemed mat-mdc-button-base']"
    )
    ISSUE_STATUS = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[1]"
    )
    PRIORITY_BREAKDOWN = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[2]"
    )
    PRIORITY_SPLIT = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[3]"
    )
    ISSUE_TREND = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[4]"
    )
    COMPLETION_RATE = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[5]"
    )
    TEAM_WORKLOAD = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[6]"
    )
    
    CYCLE_TIME_DISTRIBUTION = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[7]"
    )
    
    ASSIGNE_VS_TRACKER = (
        By.XPATH,
        "//mat-card[contains(@class,'table-card')]"
    )
    
    DATE_FILTER_RADIO_BTN = (
        By.XPATH,
        "(//input[@type='radio'])[1]"
    )
    
    UPDATE_BTN = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    
    EXPORT_BTN = (
      
        By.XPATH,
         "//button[contains(@class,'export-btn')]"
    )
    EXPORT_AS_CSV_BTN = (
        By.XPATH,
        "//button[contains(@class,'mat-mdc-menu-item') and .//span[contains(text(),'Export as CSV')]]"
    )
    
    EXPORT_AS_HTML_BTN = (
        By.XPATH,
        "//button[contains(@class,'mat-mdc-menu-item') and .//span[contains(text(),'Export as HTML')]]"
    )
   
###---------------BackLog Page------------------------

    BACKLOG = (
        By.XPATH,
        "//span[normalize-space()='Backlog']"
    )

    BACKLOG_OPEN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )

    BACKLOG_CLOSED = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )

    BACKLOG_COMPLETE_SPRINT = (
        By.XPATH,
        "//span[text()=' Complete Sprint ']"
    )
    BACKLOG_DETACH_RADIO_BTN = (
        By.XPATH,
        "(//div[@class='mdc-radio'])[1]"
        
     )
    BACKLOG_MOVETOSPRINT_RADIO_BTN = (
        By.XPATH,
        "(//div[@class='mdc-radio'])[2]"
        
    )
    BACKLOG_PAGINATOR_DRPDWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
        
    )
    BACKLOG_FULL_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[11]"
    )
    BACKLOG_FULL_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[14]"
    )
    
    BACKLOG_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[12]"
    )
    
    BACKLOG_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[13]"
    )
    
    BACKLOG_SPRINT_DETAILS_ICON = (
        By.XPATH,
        "//div[@class='position-relative']"
    )
    BACKLOG_SPRINT_NAME = (
        By.XPATH,
        "//input[@placeholder='Enter sprint name']"
        
    )
    BACKLOG_SPRINT_DESCRIPTION = (
        By.XPATH,
        "//textarea[@placeholder='Enter description']"
    )
    BACKLOG_SHARING = (
        By.XPATH,
        "//select[@formcontrolname='sharing']"
        
    )
    BACKLOG_ADD_SPRINT = (
        By.XPATH,
        "//span[text()=' Add Sprint ']"
    )
    BACKLOG_SPRINT_DURATION = (
        By.XPATH,
        "//select[@formcontrolname='duration']"
        
    )
    
    BACKLOG_SPRINT_STARTDATE = (
        By.XPATH,
        "//input[@formcontrolname='startDate']"
        
    )
    BACKLOG_SPRINT_ENDDATE = (
        By.XPATH,
        "//input[@formcontrolname='dueDate']"
        
    )
    
    BACKLOG_CREATE_SPRINT_BTN = (
        By.XPATH,
        "//button[text()=' Create Sprint ']"
        
    )
    BACKLOG_CREATE_SPRINT_BACK_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    BACKLOG_CANCEL_BTN = (
        By.XPATH,
        "(//button[@class='mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base'])[7]"
        
    )
    BACKLOG_TABLE = (
        By.XPATH,
        "//table[contains(@class,'mat-mdc-table')]"
    )
    BACKLOG_ARROW_BUTTON = (
         By.XPATH,
         "//span[@class='arrow-icon']"
     )
    #-----------------REPORTS---------------------------------
    
    REPORTS = (
        By.XPATH,
        "//span[normalize-space()='Reports']"
    )

    REPORTS_SEARCH_BTN = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )
    REPORTS_FROM_DATE = (
        By.XPATH,
        "(//div[@class='mat-mdc-text-field-wrapper mdc-text-field mdc-text-field--outlined'])[1]"
    )
    REPORTS_END_DATE = (
        By.XPATH,
        "(//div[@class='mat-mdc-text-field-wrapper mdc-text-field mdc-text-field--outlined'])[2]"
    )
    REPORTS_EXPORT_BUTTON = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger btn btn-success px-3 py-2']"
    )
    REPORTS_CHECK_BOX = (
        By.XPATH,
        "//div[contains(@class,'mdc-checkbox')]"
    )
    REPORTS_PAGINATOR_DROPDOWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    REPORTS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//span[@class='mat-mdc-button-touch-target'])[12]"
    )
    REPORTS_RIGHT_FULL_NAVIGATE_BTN = (
        By.XPATH,
        "(//span[@class='mat-mdc-button-touch-target'])[15]"
    )
    REPORTS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//span[@class='mat-mdc-button-touch-target'])[13]"
    )
    REPORTS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//span[@class='mat-mdc-button-touch-target'])[14]"
    )

    #-----------------------LISTS-----------------------------------------
    
    LISTS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Lists']"
    )
    LISTS_SEARCH_ISSUES = (
        By.XPATH,
        "//input[@placeholder='Search Issues']"
    )
    
    LIST_CHECKBOX_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']"
    )
    
    LISTS_CREATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-success create-btn']"
    )
    LISTS_TASK_BTN = (
        By.XPATH,
        "//button[@class='btn task-btn']"
    )

    LISTS_BUG_BTN = (
        By.XPATH,
        "//button[contains(@class,'bug-btn')]"
    )

    LISTS_PROD_BUG = (
        By.XPATH,
        "//button[@class='btn prod-btn']"
    )

    LISTS_CR_BTN = (
        By.XPATH,
        "//button[@class='btn cr-btn']"
    )

    LISTS_STORY_BTN = (
        By.XPATH,
        "//button[@class='btn story-btn']"
    )

    LISTS_EPIC_BTN = (
        By.XPATH,
        "//button[@class='btn epic-btn']"
    )

    LISTS_CLOSE_ICON = (
        By.XPATH,
        "//button[@class='close-btn']"
    )
    
    LISTS_EXPORT_BTN = (
        By.XPATH,
        "//span[text()=' Export ']"
    )
    LISTS_EXPORT_CSV_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[1]"
        
    )
    
    LISTS_EXPORT_HTML_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[2]"
    )
    
    LISTS_EXPORT_CSV_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[3]"
        
    )
    LISTS_EXPORT_HTML_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[4]"
        
    )
    LISTS_EXPORT_CLOSE_CLICK   =(
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
    
    LISTS_ITEMS_PER_PAGE = (
        By.XPATH,
        "//mat-form-field[contains(@class,'mat-mdc-paginator-page-size-select')]"
    )
    
    LISTS_FULL_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    LISTS_FULL_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    
    LISTS_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    
    LISTS_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    
    #------------------------TIMESHEETS-----------------------------------------------

    TIMESHEETS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Timesheets']"
    )
    
    TIMESHEETS_EXPORT_BTN = (
        By.XPATH,
        "//button[text()=' Export ']"
    )
    TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL = (
        By.XPATH,
        "//span[text()=' Download as Excel ']"
        
    )
    TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML = (
        By.XPATH,
        "//span[text()=' Download as HTML ']"
        
    )
    TIMESHEETS_EXPORT_CLOSE_CLICK  = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
    TIMESHEETS_PROJECT_LEFT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[1]"
    )

    TIMESHEETS_PROJECT_RIGHT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[2]"
    )

    TIMESHEETS_APPROVAL = (
        By.XPATH,
        "//span[text()='Approvals']"
    )
    TIMESHEETS_READY_TO_SUBMIT = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[1]"
        
    )
    TIMESHEETS_WAITING_FOR_APPROVAL = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[2]"
        
    )
    TIMESHEETS_APPROVED = (
        By.XPATH,
        "//div[@class='approval-box']"
    )
    TIMESHEETS_PROJECT_ISSUE = (
        By.XPATH,
        "//div[@class='card border']"
    )
    TIMESHEETS_TIMESHEET_CARD = (
        By.XPATH,
        "//div[@class='timesheet-card']"
    )
    TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm me-2']"
    )
    TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm ms-2']"
    )    
    #--------------------Users-------------------------------------

    USERS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Users']"
    )

    USERS_SEARCH_FIELD = (
        By.XPATH,
        "//input[@placeholder='Search ']"
    )
    USERS_ADD_USER_BTN = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    
    USERS_CREATE_NEWUSER_USRNAME = (
        By.XPATH,
        "(//input[@type='text'])[1]"
    )
    USERS_CREATE_NEWUSER_PWD = (
        By.XPATH,
        "//input[@type='password']"
    )

    USERS_EMP_USERNAME = (
        By.XPATH,
        "(//input[@type='text'])[2]"
    )
    
    USERS_EMP_EMAIL = (
        By.XPATH,
        "//input[@type='email']"
    )
    
    USERS_EMP_TEL_NO = (
        By.XPATH,
        "//input[@type='tel']"
    )

    USERS_ASSGN_PROJECT_DROPDWN = (
        By.XPATH,
        "(//mat-select)[1]"
    )
    
    USERS_ASSGN_PROJ_ROLE = (
        By.XPATH,
        "(//mat-select)[2]"
    )
    
    USERS_CREATE_USER_BTN = (
        By.XPATH,
        "//button[@class='btn-submit']"
    )
    USERS_CANCEL_BTN = (
        By.XPATH,
        "//button[@class='btn-cancel']"
    )
    
    USERS_BACK_BTN = (
        By.XPATH,
        "//button[@class='back-btn']"
    )
    USERS_PAGINATOR_DRPDWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    
    USERS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    USERS_FULL_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    USERS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    USERS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
      #------------------------ALLWORKS------------------------------------

    ALLWORKS_BTN = (
        By.XPATH,
        "//button[contains(@class,'active-link')]"
    )




####---------------------------GT BOARD----------------------------------------

    GT_BOARD = (
        By.XPATH,
        "(//mat-card[contains(@class,'board-item-card')])[2]"
    )

###------------KANBAN MODULE--------------------

    KANBAN_SELECT_BOARD_DRPDWN = (
        By.XPATH,
        "//mat-label[text()='Select Board']"
    )
    KANBAN_DROPDWN_GT_BOARD = (
        By.XPATH,
        " //span[text()=' GT Board ']"
        
    )
    KANBAN_DROPDWN_BUGS_BOARD = (
        By.XPATH,
        " //span[text()=' Bugs Board ']"
        
    )
    KANBAN_SELECT_DRPDWN_CLICK_BTN = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
    
    KANBAN_GENERAL_TRACKER_BILLABLE = (
        By.XPATH,
        "//div[@id='billableList']"
    )
    KANBAN_GENERAL_TRACKER_NONBILLABLE = (
        By.XPATH,
        "//div[@id='nonBillableList']"
    )
    
    ###-----------------GT_SUMMARY MODULE
    ###---------------GT_SUMMARY Page--------------------------------------

    GT_SUMMARY = (
        By.XPATH,
        "//span[normalize-space()='Summary']"
    )

    GT_TOTAL_ISSUES = (
        By.XPATH,
        "//mat-card[contains(@class,'kpi-card') and contains(@class,'total')]"
    )

    GT_OPEN_ISSUES = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card open']"
    )

    GT_CLOSED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card closed']"
    )

    GT_UPDATED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card overdue']"
    )

    GT_DATE_FILTER = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    GT_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger export-btn mdc-button mdc-button--raised mat-mdc-raised-button mat-unthemed mat-mdc-button-base']"
    )
    GT_ISSUE_STATUS = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[1]"
    )
    GT_PRIORITY_BREAKDOWN = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[2]"
    )
    GT_PRIORITY_SPLIT = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[3]"
    )
    GT_ISSUE_TREND = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[4]"
    )
    GT_COMPLETION_RATE = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[5]"
    )
    GT_TEAM_WORKLOAD = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[6]"
    )
    
    GT_CYCLE_TIME_DISTRIBUTION = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[7]"
    )
    
    GT_ASSIGNE_VS_TRACKER = (
        By.XPATH,
        "//mat-card[contains(@class,'table-card')]"
    )

    GT_DATE_FILTER_RADIO_BTN = (
        By.XPATH,
        "(//input[@type='radio'])[1]"
    )
    
    GT_UPDATE_BTN = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    
    GT_DATE_FILTER_CLOSE_CLICK = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
    GT_EXPORT_BTN = (
        
        By.XPATH,
         "//button[contains(@class,'export-btn')]"
    )
    GT_EXPORT_CLOSE_CLICK = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']")
        
    GT_EXPORT_AS_CSV_BTN = (
        By.XPATH,
        "//button[contains(@class,'mat-mdc-menu-item') and .//span[contains(text(),'Export as CSV')]]"
    )
    GT_EXPORT_AS_HTML_BTN = (
        By.XPATH,
        "//button[contains(@class,'mat-mdc-menu-item') and .//span[contains(text(),'Export as HTML')]]"
    )
    
    #-----------------GT_REPORTS---------------------------------
    
    GT_REPORTS = (
        By.XPATH,
        "//span[normalize-space()='Reports']"
    )

    GT_REPORTS_SEARCH_BTN = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )
    GT_REPORTS_FROM_DATE = (
        By.XPATH,
        "//input[@formcontrolname='fromDate']"
    )
    GT_REPORTS_END_DATE = (
        By.XPATH,
        "//input[@formcontrolname='toDate']"
    )
    GT_REPORTS_EXPORT_BUTTON = (
        By.XPATH,
        "//button[text()=' Export ']"
    )
    GT_REPORTS_CHECK_BOX = (
        By.XPATH,
        "//div[contains(@class,'mdc-checkbox')]"
    )
    GT_REPORTS_PAGINATOR_DROPDOWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    GT_REPORTS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    GT_REPORTS_RIGHT_FULL_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[7]"
    )
    GT_REPORTS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    GT_REPORTS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[6]"
    )
    GT_REPORTS_EXPORT_EXCEL_BTN = (
        By.XPATH,
        "//span[text()=' Download as Excel ']"
    )
    
    GT_REPORTS_EXPORT_AS_HTML_BTN = (
        By.XPATH,
        "//span[text()=' Download as HTML ']"
    )
    GT_REPORTS_EXPORT_CLOSE_CLICK =(
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
    #----------------------GT ALLWORKS BUTTON-------------------------------
    
    GT_ALLWORKS_BTN = (
        By.XPATH,
        "//button[contains(@class,'active-link')]"
    )
    
    
        
    #-----------------------GT_LISTS-----------------------------------------
    
    GT_LISTS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Lists']"
    )
    GT_LISTS_SEARCH_ISSUES = (
        By.XPATH,
        "//input[@placeholder='Search Issues']"
    )
    
    GT_LIST_CHECKBOX_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']"
    )
    
    GT_LISTS_CREATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-success create-btn']"
    )
    GT_LISTS_TASK_BTN = (
        By.XPATH,
        "//button[@class='btn task-btn']"
    )

    GT_LISTS_BUG_BTN = (
        By.XPATH,
        "//button[contains(@class,'bug-btn')]"
    )

    GT_LISTS_PROD_BUG = (
        By.XPATH,
        "//button[@class='btn prod-btn']"
    )

    GT_LISTS_CR_BTN = (
        By.XPATH,
        "//button[@class='btn cr-btn']"
    )

    GT_LISTS_STORY_BTN = (
        By.XPATH,
        "//button[@class='btn story-btn']"
    )

    GT_LISTS_EPIC_BTN = (
        By.XPATH,
        "//button[@class='btn epic-btn']"
    )

    GT_LISTS_CLOSE_ICON = (
        By.XPATH,
        "//button[@class='close-btn']"
    )
    
    GT_LISTS_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-primary mat-mdc-button-base']"
    )
    GT_LISTS_ITEMS_PER_PAGE = (
        By.XPATH,
        "//mat-form-field[contains(@class,'mat-mdc-paginator-page-size-select')]"
    )
    
    GT_LISTS_FULL_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    GT_LISTS_FULL_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    
    GT_LISTS_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    
    GT_LISTS_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    GT_LISTS_EXPORT_CSV_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[1]"
        
    )
    
    GT_LISTS_EXPORT_HTML_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[2]"
    )
    
    GT_LISTS_EXPORT_CSV_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[3]"
        
    )
    GT_LISTS_EXPORT_HTML_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[4]"
        
    )
    GT_LISTS_EXPORT_CLOSE_CLICK   =(
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
    
    #------------------------GT_TIMESHEETS-----------------------------------------------

    GT_TIMESHEETS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Timesheets']"
    )
    
    GT_TIMESHEETS_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger btn btn-success px-3 py-2']"
    )
    GT_TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL = (
        By.XPATH,
        "//span[text()=' Download as Excel ']"
        
    )
    GT_TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML = (
        By.XPATH,
        "//span[text()=' Download as HTML ']"
        
    )
    GT_TIMESHEETS_EXPORT_CLOSE_CLICK  = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
   
    GT_TIMESHEETS_PROJECT_LEFT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[1]"
    )

    GT_TIMESHEETS_PROJECT_RIGHT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[2]"
    )
    GT_TIMESHEETS_APPROVAL = (
        By.XPATH,
        "//span[text()='Approvals']"
    )
    GT_TIMESHEETS_READY_TO_SUBMIT = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[1]"
        
    )
    GT_TIMESHEETS_WAITING_FOR_APPROVAL = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[2]"
        
    )
    GT_TIMESHEETS_APPROVED = (
        By.XPATH,
        "//div[@class='approval-box']"
    )
    GT_TIMESHEETS_PROJECT_ISSUE = (
        By.XPATH,
        "//div[@class='card border']"
    )
    GT_TIMESHEETS_TIMESHEET_CARD = (
        By.XPATH,
        "//div[@class='timesheet-card']"
    )
    GT_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm me-2']"
    )
    GT_TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm ms-2']"
    )    
   
   
    #--------------------Users-------------------------------------

    GT_USERS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Users']"
    )

    GT_USERS_SEARCH_FIELD = (
        By.XPATH,
        "//input[@placeholder='Search ']"
    )
    GT_USERS_ADD_USER_BTN = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    
    GT_USERS_CREATE_NEWUSER_USRNAME = (
        By.XPATH,
        "(//input[@type='text'])[1]"
    )
    GT_USERS_CREATE_NEWUSER_PWD = (
        By.XPATH,
        "//input[@type='password']"
    )

    GT_USERS_EMP_USERNAME = (
        By.XPATH,
        "(//input[@type='text'])[2]"
    )
    
    GT_USERS_EMP_EMAIL = (
        By.XPATH,
        "//input[@type='email']"
    )
    
    GT_USERS_EMP_TEL_NO = (
        By.XPATH,
        "//input[@type='tel']"
    )

    GT_USERS_ASSGN_PROJECT_DROPDWN = (
        By.XPATH,
        "(//mat-select)[1]"
    )
    
    GT_USERS_ASSGN_PROJ_ROLE = (
        By.XPATH,
        "(//mat-select)[2]"
    )
    
    GT_USERS_CREATE_USER_BTN = (
        By.XPATH,
        "//button[@class='btn-submit']"
    )
    GT_USERS_CANCEL_BTN = (
        By.XPATH,
        "//button[@class='btn-cancel']"
    )
    
    GT_USERS_BACK_BTN = (
        By.XPATH,
        "//button[@class='back-btn']"
    )
    GT_USERS_PAGINATOR_DRPDWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    
    GT_USERS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    GT_USERS_FULL_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    GT_USERS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    GT_USERS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    
    
    #--------------------------------Bugs Board-------------------------------------------
    
    BUGS_KANBAN_SELECT_BOARD = (
    By.XPATH,
    "//div[contains(@class,'mdc-notched-outline')]"
    )
    
    BUGS_OPEN_BACKLOG = (
        By.XPATH,
        "//div[@id='openBacklogList']"
    )
    BUGS_INPROGRESS = (
        By.XPATH,
        "//div[@id='inProgressList']"
    )
    
    BUGS_CLARIFICATION_LIST = (
        By.XPATH,
        "//div[@id='clarificationList']"
    )
    BUGS_RELEASE_QA = (
        By.XPATH,
        "//div[@id='releaseQAList']"
    )
    BUGS_FIXED_LIST = (
        By.XPATH,
        "//div[@id='fixedList']"
    )
    BUGS_CLOSED_DONE = (
        By.XPATH,
        "//div[@id='doneList']"
    )
    BUGS_REJECTED = (
        By.XPATH,
        "//div[@id='rejectedList']"
        
    )
    BUGS_DEFFERED_LIST = (
        
        By.XPATH,
        "//div[@id='deferredList']"
    )
    BUGS_NOTREPRO = (
        
        By.XPATH,
        "//div[@id='notReproList']"
    )
    BUGS_SELECT_GT_BOARD = (
        By.XPATH,
        "//mat-option[@id='mat-option-120']"
    )
    BUGS_SELECT_BUGS_BOARD = (
        By.XPATH,
        "//mat-option[@id='mat-option-121']"
        
    )
    #------------------BUGS SUMMARY -------------------------
    BUGS_SUMMARY = (
        By.XPATH,
        "//span[normalize-space()='Summary']"
    )

    BUGS_TOTAL_ISSUES = (
        By.XPATH,
        "//mat-card[contains(@class,'kpi-card') and contains(@class,'total')]"
    )

    BUGS_OPEN_ISSUES = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card open']"
    )

    BUGS_CLOSED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card closed']"
    )

    BUGS_UPDATED_STATUS = (
        By.XPATH,
        "//mat-card[@class='mat-mdc-card mdc-card kpi-card overdue']"
    )

    BUGS_DATE_FILTER = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    BUGS_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger export-btn mdc-button mdc-button--raised mat-mdc-raised-button mat-unthemed mat-mdc-button-base']"
    )
    BUGS_ISSUE_STATUS = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[1]"
    )
    BUGS_PRIORITY_BREAKDOWN = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[2]"
    )
    BUGS_PRIORITY_SPLIT = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[3]"
    )
    BUGS_ISSUE_TREND = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[4]"
    )
    BUGS_COMPLETION_RATE = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[5]"
    )
    BUGS_TEAM_WORKLOAD = (
        By.XPATH,
        "(//mat-card[contains(@class,'chart-card')])[6]"
    )
    
    BUGS_CYCLE_TIME_DISTRIBUTION = (
        By.XPATH,
        "(//mat-card[@class='mat-mdc-card mdc-card chart-card'])[7]"
    )
    
    BUGS_ASSIGNE_VS_TRACKER = (
        By.XPATH,
        "//mat-card[contains(@class,'table-card')]"
    )

    BUGS_DATE_FILTER_RADIO_BTN = (
        By.XPATH,
        "(//input[@type='radio'])[1]"
    )
    
    BUGS_UPDATE_BTN = (
        By.XPATH,
        "//span[text()=' Update ']"
    )
    BUGS_EXPORT_BTN = (
        
        By.XPATH,
         "//button[contains(@class,'export-btn')]"
    )
    BUGS_EXPORT_AS_CSV_BTN = (
        By.XPATH,
        "//span[text()='Export as CSV']"
    )
    BUGS_EXPORT_AS_HTML_BTN = (
        By.XPATH,
        "//span[text()='Export as HTML']"
    )
    BUGS_SUMMARY_CLOSE_CLICK = (
         By.XPATH,
         "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
    # --------------BUGS ALLWORKS Button ---------------------------------------
    
    BUGS_ALLWORKS_BTN = (
        By.XPATH,
        "//button[contains(@class,'active-link')]"
    )
    
   #-----------------------BUGS REPORTS---------------------------------------
   
    BUGS_REPORTS = (
        By.XPATH,
        "//span[normalize-space()='Reports']"
    )

    BUGS_REPORTS_SEARCH_BTN = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )
    BUGS_REPORTS_FROM_DATE = (
        By.XPATH,
        "//input[@formcontrolname='fromDate']"
    )
    BUGS_REPORTS_END_DATE = (
        By.XPATH,
        "//input[@formcontrolname='toDate']"
    )
    BUGS_REPORTS_EXPORT_BUTTON = (
        By.XPATH,
        "//button[text()=' Export ']"
    )
    BUGS_REPORTS_CHECK_BOX = (
        By.XPATH,
        "//div[contains(@class,'mdc-checkbox')]"
    )
    BUGS_REPORTS_PAGINATOR_DROPDOWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    BUGS_REPORTS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    BUGS_REPORTS_RIGHT_FULL_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[7]"
    )
    BUGS_REPORTS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    BUGS_REPORTS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[6]"
    )
    BUGS_REPORTS_EXPORT_EXCEL_BTN = (
        By.XPATH,
        "//span[text()=' Download as Excel ']"
    )
    
    BUGS_REPORTS_EXPORT_AS_HTML_BTN = (
        By.XPATH,
        "//span[text()=' Download as HTML ']"
    )
    BUGS_REPORTS_EXPORT_CLOSE_CLICK =(
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
   
   
    #-----------------------BUGS_LISTS-----------------------------------------
    
    BUGS_LISTS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Lists']"
    )
    BUGS_LISTS_SEARCH_ISSUES = (
        By.XPATH,
        "//input[@placeholder='Search Issues']"
    )
    
    BUGS_LIST_CHECKBOX_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']"
    )
    
    BUGS_LISTS_CREATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-success create-btn']"
    )
    BUGS_LISTS_TASK_BTN = (
        By.XPATH,
        "//button[@class='btn task-btn']"
    )

    BUGS_LISTS_BUG_BTN = (
        By.XPATH,
        "//button[contains(@class,'bug-btn')]"
    )

    BUGS_LISTS_PROD_BUG = (
        By.XPATH,
        "//button[@class='btn prod-btn']"
    )

    BUGS_LISTS_CR_BTN = (
        By.XPATH,
        "//button[@class='btn cr-btn']"
    )

    BUGS_LISTS_STORY_BTN = (
        By.XPATH,
        "//button[@class='btn story-btn']"
    )

    BUGS_LISTS_EPIC_BTN = (
        By.XPATH,
        "//button[@class='btn epic-btn']"
    )

    BUGS_LISTS_CLOSE_ICON = (
        By.XPATH,
        "//button[@class='close-btn']"
    )
    
    BUGS_LISTS_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-primary mat-mdc-button-base']"
    )
    BUGS_LISTS_PAGINATION = (
        By.XPATH,
        "//mat-form-field[contains(@class,'mat-mdc-paginator-page-size-select')]"
    )
    
    BUGS_LISTS_FULL_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    BUGS_LISTS_FULL_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    
    BUGS_LISTS_LEFT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    
    BUGS_LISTS_RIGHT_NAVIGATION_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    BUGS_LISTS_EXPORT_CSV_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[1]"
        
    )
    
    BUGS_LISTS_EXPORT_HTML_DEF = (
        By.XPATH,
        "(//button[@role='menuitem'])[2]"
    )
    
    BUGS_LISTS_EXPORT_CSV_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[3]"
        
    )
    BUGS_LISTS_EXPORT_HTML_ALL_FIELDS = (
        By.XPATH,
        "(//button[@role='menuitem'])[4]"
        
    )
    BUGS_LISTS_EXPORT_CLOSE_CLICK   =(
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
        
    )
    
    #------------------------BUGS_TIMESHEETS-----------------------------------------------

    BUGS_TIMESHEETS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Timesheets']"
    )
    
    BUGS_TIMESHEETS_EXPORT_BTN = (
        By.XPATH,
        "//button[@class='mat-mdc-menu-trigger btn btn-success px-3 py-2']"
    )
    
    BUGS_TIMESHEETS_PROJECT_LEFT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[1]"
    )

    BUGS_TIMESHEETS_PROJECT_RIGHT_NAV_BTN = (
        By.XPATH,
        "(//button[@class='btn btn-outline-secondary btn-sm rounded-circle'])[2]"
    )
    BUGS_TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL = (
        By.XPATH,
        "//span[text()=' Download as Excel ']"
        
    )
    BUGS_TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML = (
        By.XPATH,
        "//span[text()=' Download as HTML ']"
        
    )
    BUGS_TIMESHEETS_EXPORT_CLOSE_CLICK  = (
        By.XPATH,
        "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']"
    )
   
    BUGS_TIMESHEETS_APPROVAL = (
        By.XPATH,
        "//span[text()='Approvals']"
    )
    BUGS_TIMESHEETS_READY_TO_SUBMIT = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[1]"
        
    )
    BUGS_TIMESHEETS_WAITING_FOR_APPROVAL = (
        By.XPATH,
        "(//div[@class='approval-box mb-4'])[2]"
        
    )
    BUGS_TIMESHEETS_APPROVED = (
        By.XPATH,
        "//div[@class='approval-box']"
    )
    BUGS_TIMESHEETS_PROJECT_ISSUE = (
        By.XPATH,
        "//div[@class='card border']"
    )
    BUGS_TIMESHEETS_TIMESHEET_CARD = (
        By.XPATH,
        "//div[@class='timesheet-card']"
    )
    BUGS_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm me-2']"
    )
    BUGS_TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm ms-2']"
    )    
   
    #--------------------BUGS_Users-------------------------------------

    BUGS_USERS_BTN = (
        By.XPATH,
        "//span[normalize-space()='Users']"
    )

    BUGS_USERS_SEARCH_FIELD = (
        By.XPATH,
        "//input[@placeholder='Search ']"
    )
    BUGS_USERS_ADD_USER_BTN = (
        By.XPATH,
        "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']"
    )
    
    BUGS_USERS_CREATE_NEWUSER_USRNAME = (
        By.XPATH,
        "(//input[@type='text'])[1]"
    )
    BUGS_USERS_CREATE_NEWUSER_PWD = (
        By.XPATH,
        "//input[@type='password']"
    )

    BUGS_USERS_EMP_USERNAME = (
        By.XPATH,
        "(//input[@type='text'])[2]"
    )
    
    BUGS_USERS_EMP_EMAIL = (
        By.XPATH,
        "//input[@type='email']"
    )
    
    BUGS_USERS_EMP_TEL_NO = (
        By.XPATH,
        "//input[@type='tel']"
    )

    BUGS_USERS_ASSGN_PROJECT_DROPDWN = (
        By.XPATH,
        "(//mat-select)[1]"
    )
    
    BUGS_USERS_ASSGN_PROJ_ROLE = (
        By.XPATH,
        "(//mat-select)[2]"
    )
    
    BUGS_USERS_CREATE_USER_BTN = (
        By.XPATH,
        "//button[@class='btn-submit']"
    )
    BUGS_USERS_CANCEL_BTN = (
        By.XPATH,
        "//button[@class='btn-cancel']"
    )
    
    BUGS_USERS_BACK_BTN = (
        By.XPATH,
        "//button[@class='back-btn']"
    )
    BUGS_USERS_PAGINATOR_DRPDWN = (
        By.XPATH,
        "//div[@class='mat-mdc-paginator-touch-target']"
    )
    
    BUGS_USERS_FULL_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[2]"
    )
    BUGS_USERS_FULL_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[5]"
    )
    BUGS_USERS_LEFT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[3]"
    )
    BUGS_USERS_RIGHT_NAVIGATE_BTN = (
        By.XPATH,
        "(//button[@type='button'])[4]"
    )
    
    SCRUM_BOARD_TEAMS = [
    " GHMIS ",
    " OSS ",
    " PDS ",
    " UPEX DISTRIBUTION AND PAYMENT TEAM "
    
     ]
    
    GT_BOARD_TEAMS =[
        
        " IT Infra ",
        " IT Support ",
        " R&D Product Design & Development ",
        " R&D Software & Support "," AI/ML "
        
        
    ]
    
    """---------------Functions----------------------------------------------""" 
    
    def is_task_only_project(self):
        return self.selected_team in [
        " IT Infra ",
        " IT Support "]
        


    def is_task_bug_story_epic_project(self):
       return self.selected_team in [
       " R&D Product Design & Development ",
        " R&D Software & Support ", " PDS "
    ]


    def is_all_tracker_project(self):
      return self.selected_team in [
        " GHMIS ",
         " OSS ",
         " UPEX DISTRIBUTION AND PAYMENT TEAM "
           ]
      
    def select_filter_by_projects(self):
        
        self.driver.find_element(*self.FILTER_BY_PROJECTS).click()
        
        self.driver.find_element(*self.DESELECT_ALL).click()
        
        project_locator = (
        By.XPATH,
        f"//span[text()='{Config.PROJECT}']"
    )

        self.driver.find_element(*project_locator).click()

        
        
        self.driver.find_element(*self.CLICK_ON_HOMEPAGE).click()

        self.selected_team = Config.PROJECT
        
    def navigate_board(self):


    # Scrum Board (only for Scrum teams)
       if self.selected_team in self.SCRUM_BOARD_TEAMS:

        print(f"{self.selected_team} -> Scrum Board is available")

       
        # Return to Home Page
       

       else:

        print(f"{self.selected_team} -> Scrum Board is NOT available")
        print("Skipping Scrum Board")


   
    
    def verify_home_page(self):

        assert self.driver.find_element(*self.BOARD_TITLE).is_displayed()
        assert self.driver.find_element(*self.GT_BOARD).is_displayed()
        assert self.driver.find_element(*self.BUGS_BOARD).is_displayed()
        assert self.driver.find_element(*self.HOME_BUTTON).is_displayed()
        assert self.driver.find_element(*self.FILTER_BY_PROJECTS).is_displayed()
        assert self.driver.find_element(*self.USER_PROFILE_BTN).is_displayed()

        user_profile_btn = self.driver.find_element(*self.USER_PROFILE_BTN)
        self.driver.execute_script("arguments[0].click();", user_profile_btn)
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.USER_PROFILE_NAME).is_displayed()
        assert self.driver.find_element(*self.VIEW_PROFILE_BTN).is_displayed()
        assert self.driver.find_element(*self.THEME_BLUE_DOT_BTN).is_displayed()
        assert self.driver.find_element(*self.THEME_DOT_DARK).is_displayed()
        assert self.driver.find_element(*self.THEME_DOT_GREEN).is_displayed()
        assert self.driver.find_element(*self.CHANGE_PASSWORD_BTN).is_displayed()
        assert self.driver.find_element(*self.LOG_OUT_BTN).is_displayed()

    def verify_create_btn(self):

       WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(self.CREATE_BTN)
       ).click()
      
       if self.is_task_only_project():
        self.verify_task_only()

       elif self.is_task_bug_story_epic_project():
        self.verify_task_bug_story_epic()

       elif self.is_all_tracker_project():
        self.verify_all_trackers()

       else:
        raise Exception(f"No tracker configuration found for {self.selected_team}")
       
       self.driver.find_element(*self.CLOSE_ICON).click()
       
       
    def verify_task_only(self):

        assert self.driver.find_element(*self.TASK_BTN).is_displayed()

        print(f"{self.selected_team} -> Task tracker verified.")
    
    def verify_task_bug_story_epic(self):

       assert self.driver.find_element(*self.TASK_BTN).is_displayed()
       assert self.driver.find_element(*self.BUG_BTN).is_displayed()
       assert self.driver.find_element(*self.STORY_BTN).is_displayed()
       assert self.driver.find_element(*self.EPIC_BTN).is_displayed()

       print(f"{self.selected_team} -> Task, Bug, Story and Epic verified.")
    
    
    def verify_all_trackers(self):

       assert self.driver.find_element(*self.TASK_BTN).is_displayed()
       assert self.driver.find_element(*self.BUG_BTN).is_displayed()
       assert self.driver.find_element(*self.PROD_BUG).is_displayed()
       assert self.driver.find_element(*self.CR_BTN).is_displayed()
       assert self.driver.find_element(*self.STORY_BTN).is_displayed()
       assert self.driver.find_element(*self.EPIC_BTN).is_displayed()

       print(f"{self.selected_team} -> All trackers verified.")
    
    
    def has_scrum_board(self):
        return self.selected_team in self.SCRUM_BOARD_TEAMS



    def open_scrum_board(self):
        

        if self.selected_team not in self.SCRUM_BOARD_TEAMS:
         print(f"{self.selected_team} does not have Scrum Board")
         return False

        print(f"{self.selected_team} has Scrum Board")

        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*self.SCRUM_BOARD).click()

        return True
            
    def verify_active_sprint_module(self):

        wait = WebDriverWait(self.driver, Config.LONG_WAIT)

    # Verify Tracker Type is displayed
  
        assert wait.until(
        EC.visibility_of_element_located(self.TRACKER_TYPE)
        ).is_displayed()

    # Find Complete Sprint element
    
        complete_sprint = self.driver.find_elements(*self.COMPLETE_SPRINT)
        
    # Click Complete Sprint
        wait.until(
        EC.element_to_be_clickable(self.COMPLETE_SPRINT)
        ).click()

    # Verify Sprint Details popup
        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_DETACH_RADIO_BUTTON)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_MOVETOSPRINT_RADIO_BUTTON)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_ITEMS_PER_PAGE_DROPDOWN)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_FULL_LEFT_NAVIGATE_BTN)
        ).is_displayed()


        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_FULL_RIGHT_NAVIGATE_BTN)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_LEFT_NAVIGATE_BTN)
         ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_RIGHT_NAVIGATE_BTN)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_CANCEL_BUTTON)
         ).is_displayed()

    # Close popup
        wait.until(
        EC.element_to_be_clickable(
            self.SPRINT_DETAILS_CLOSE_BUTTON)
         ).click()

    # Verify Active Sprint Board
        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_BTN)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.SPRINT_DETAILS_CHIP)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.TO_DO)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located3(
            self.IN_PROGRESS)
        ).is_displayed()

        assert wait.until(
        EC.visibility_of_element_located(
            self.DONE)
        ).is_displayed()

        print("Active Sprint module verified successfully.")
    
    
    
    def verify_summary_module(self):

        self.driver.find_element(*self.SUMMARY).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.TOTAL_ISSUES).is_displayed()
        assert self.driver.find_element(*self.OPEN_ISSUES).is_displayed()
        assert self.driver.find_element(*self.CLOSED_STATUS).is_displayed()
        assert self.driver.find_element(*self.UPDATED_STATUS).is_displayed()
        assert self.driver.find_element(*self.DATE_FILTER).is_displayed()
        assert self.driver.find_element(*self.EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.ISSUE_STATUS).is_displayed()
        assert self.driver.find_element(*self.PRIORITY_BREAKDOWN).is_displayed()
        assert self.driver.find_element(*self.PRIORITY_SPLIT).is_displayed()
        assert self.driver.find_element(*self.ISSUE_TREND).is_displayed()
        assert self.driver.find_element(*self.COMPLETION_RATE).is_displayed()
        assert self.driver.find_element(*self.TEAM_WORKLOAD).is_displayed()
        assert self.driver.find_element(*self.CYCLE_TIME_DISTRIBUTION).is_displayed()
        assert self.driver.find_element(*self.ASSIGNE_VS_TRACKER).is_displayed()
        
        
        self.driver.find_element(*self.DATE_FILTER).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.DATE_FILTER_RADIO_BTN).is_displayed()
        
        self.driver.find_element(*self.UPDATE_BTN).is_displayed()
        
        self.driver.find_element(*self.CLICK_ON_SUMMARY_PAGE).click()
        
        self.driver.find_element(*self.EXPORT_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.EXPORT_AS_CSV_BTN).is_displayed()
        assert self.driver.find_element(*self.EXPORT_AS_HTML_BTN).is_displayed()
        
        self.driver.find_element(*self.CLICK_ON_SUMMARY_PAGE).click()

    def verify_backlog_module(self):

        self.driver.find_element(*self.BACKLOG).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.BACKLOG_OPEN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_CLOSED).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_COMPLETE_SPRINT).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_DETAILS_ICON).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_ADD_SPRINT).is_displayed()
        
        
        self.driver.find_element(*self.BACKLOG_ADD_SPRINT).click()

        try:
            error = self.driver.find_element(
                By.XPATH,
                "//*[contains(text(),'Sprint Limit Reached')]"
            )

            if error.is_displayed():
                print("Sprint Limit Reached. Skipping remaining backlog steps.")
                return

        except NoSuchElementException:
            pass
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.BACKLOG_CREATE_SPRINT_BACK_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_NAME).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_DESCRIPTION).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SHARING).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_DURATION).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_STARTDATE).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_SPRINT_ENDDATE).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_CREATE_SPRINT_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_CREATE_SPRINT_BACK_BTN).is_displayed()
        self.driver.find_element(*self.BACKLOG_ARROW_BUTTON).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BACKLOG_COMPLETE_SPRINT).click()
        
        time.sleep(Config.LONG_WAIT)
        
        assert self.driver.find_element(*self.BACKLOG_DETACH_RADIO_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_MOVETOSPRINT_RADIO_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_FULL_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_FULL_RIGHT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_RIGHT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BACKLOG_CANCEL_BTN).is_displayed()
        self.driver.find_element(*self.BACKLOG_CANCEL_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*self.BACKLOG_SPRINT_DETAILS_ICON).click()
        
        time.sleep(Config.SHORT_WAIT)
        
        self.driver.find_element(*self.BACKLOG_SPRINT_DETAILS_ICON).click()

    def verify_reports_module(self):

        self.driver.find_element(*self.REPORTS).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.REPORTS_SEARCH_BTN).is_displayed()
        assert self.driver.find_element(*self.REPORTS_FROM_DATE).is_displayed()
        assert self.driver.find_element(*self.REPORTS_END_DATE).is_displayed()
        assert self.driver.find_element(*self.REPORTS_EXPORT_BUTTON).is_displayed()
        assert self.driver.find_element(*self.REPORTS_CHECK_BOX).is_displayed()
        assert self.driver.find_element(*self.REPORTS_PAGINATOR_DROPDOWN).is_displayed()
        assert self.driver.find_element(*self.REPORTS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.REPORTS_RIGHT_FULL_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.REPORTS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.REPORTS_RIGHT_NAVIGATE_BTN).is_displayed()

    def verify_lists_module(self):

        self.driver.find_element(*self.LISTS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.LISTS_SEARCH_ISSUES)
        )

        assert self.driver.find_element(*self.LISTS_SEARCH_ISSUES).is_displayed()
        assert self.driver.find_element(*self.LIST_CHECKBOX_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_CREATE_BTN).is_displayed()

        self.driver.find_element(*self.LISTS_CREATE_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.LISTS_TASK_BTN)
        )

        assert self.driver.find_element(*self.LISTS_TASK_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_BUG_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_EPIC_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_CR_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_PROD_BUG).is_displayed()
        assert self.driver.find_element(*self.LISTS_STORY_BTN).is_displayed()

        self.driver.find_element(*self.LISTS_CLOSE_ICON).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        

        assert self.driver.find_element(*self.LISTS_EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_ITEMS_PER_PAGE).is_displayed()
        assert self.driver.find_element(*self.LISTS_FULL_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_FULL_RIGHT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.LISTS_RIGHT_NAVIGATION_BTN).is_displayed()

        
        self.driver.find_element(*self.LISTS_EXPORT_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.LISTS_EXPORT_CSV_DEF).is_displayed()
        assert self.driver.find_element(*self.LISTS_EXPORT_HTML_DEF).is_displayed()
        assert self.driver.find_element(*self.LISTS_EXPORT_CSV_ALL_FIELDS).is_displayed()
        assert self.driver.find_element(*self.LISTS_EXPORT_HTML_ALL_FIELDS).is_displayed()
        
        self.driver.find_element(*self.LISTS_EXPORT_CLOSE_CLICK).click()
        
        
            
        
#-----------------------      ALLWORKS MODULE----------------------------------

    #def verify_allworks_module(self):
        
     #   assert self.driver.find_element(*self.ALLWORKS_BTN).is_displayed()
      #  self.driver.find_element(*self.ALLWORKS_BTN).click()
        
       # print(self.driver.find_element(*self.ALLWORKS_BTN).is_displayed())

#----------------TIMESHEETS MODULE---------------------------------------------

    def verify_timesheets_module(self):

        timesheets_btn = self.driver.find_element(*self.TIMESHEETS_BTN)
        self.driver.execute_script("arguments[0].click();", timesheets_btn)

        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.TIMESHEETS_PROJECT_ISSUE).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_TIMESHEET_CARD).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_PROJECT_LEFT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_PROJECT_RIGHT_NAV_BTN).is_displayed()
        
        
        assert self.driver.find_element(*self.TIMESHEETS_PROJECT_LEFT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_PROJECT_RIGHT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_APPROVAL).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_EXPORT_BTN).is_displayed()
        self.driver.find_element(*self.TIMESHEETS_PROJECT_LEFT_NAV_BTN).click()
        self.driver.find_element(*self.TIMESHEETS_PROJECT_RIGHT_NAV_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
       
        self.driver.find_element(*self.TIMESHEETS_EXPORT_BTN).click()
        assert self.driver.find_element(*self.TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL).is_displayed()
        assert self.driver.find_element(*self.TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML).is_displayed()
        self.driver.find_element(*self.TIMESHEETS_EXPORT_CLOSE_CLICK).click()
        
 ## TIME SHEETS APPROVAL-------------------------
    
        self.driver.find_element(*self.TIMESHEETS_APPROVAL).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.TIMESHEETS_READY_TO_SUBMIT).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_WAITING_FOR_APPROVAL).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_APPROVED).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).is_displayed()
        self.driver.find_element(*self.TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).click()
        self.driver.find_element(*self.TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).click()



    def verify_users_module(self):

        self.driver.find_element(*self.USERS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.USERS_SEARCH_FIELD)
        )

        assert self.driver.find_element(*self.USERS_SEARCH_FIELD).is_displayed()
        assert self.driver.find_element(*self.USERS_ADD_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_PAGINATOR_DRPDWN).is_displayed()
        assert self.driver.find_element(*self.USERS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_FULL_RIGHT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_RIGHT_NAVIGATE_BTN).is_displayed()
        self.driver.find_element(*self.USERS_ADD_USER_BTN).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.USERS_CREATE_NEWUSER_USRNAME).is_displayed()
        assert self.driver.find_element(*self.USERS_CREATE_NEWUSER_PWD).is_displayed()
        assert self.driver.find_element(*self.USERS_EMP_USERNAME).is_displayed()
        assert self.driver.find_element(*self.USERS_EMP_EMAIL).is_displayed()
        assert self.driver.find_element(*self.USERS_EMP_TEL_NO).is_displayed()
        assert self.driver.find_element(*self.USERS_ASSGN_PROJECT_DROPDWN).is_displayed()
        assert self.driver.find_element(*self.USERS_ASSGN_PROJ_ROLE).is_displayed()
        assert self.driver.find_element(*self.USERS_CREATE_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_CANCEL_BTN).is_displayed()
        assert self.driver.find_element(*self.USERS_BACK_BTN).is_displayed()

        self.driver.find_element(*self.USERS_BACK_BTN).click()
        
        
        
        
#---------------------GT BOARD---------------------------------------
    def verify_gt_board(self):

        self.driver.find_element(*self.HOME_BUTTON).click()

        assert self.driver.find_element(*self.GT_BOARD).is_displayed()

        self.driver.find_element(*self.GT_BOARD).click()

        time.sleep(Config.MEDIUM_WAIT)

    def verify_kanban_module(self):

        assert self.driver.find_element(*self.KANBAN_SELECT_BOARD_DRPDWN).is_displayed()
        
        self.driver.find_element(*self.KANBAN_SELECT_BOARD_DRPDWN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        assert self.driver.find_element(*self.KANBAN_DROPDWN_GT_BOARD).is_displayed()
        assert self.driver.find_element(*self.KANBAN_DROPDWN_BUGS_BOARD).is_displayed()
        self.driver.find_element(*self.KANBAN_SELECT_DRPDWN_CLICK_BTN).click()
        assert self.driver.find_element(*self.KANBAN_GENERAL_TRACKER_BILLABLE).is_displayed()
        assert self.driver.find_element(*self.KANBAN_GENERAL_TRACKER_NONBILLABLE).is_displayed()
        
        
   
    #def verify_gt_allworks_module(self):
        
     #   assert self.driver.find_element(*self.GT_ALLWORKS_BTN).is_displayed()
      #  self.driver.find_element(*self.GT_ALLWORKS_BTN).click()
        
       # print(self.driver.find_element(*self.GT_ALLWORKS_BTN).is_displayed())

   
   
   
    def open_gt_board(self):    
        
        self.driver.find_element(*self.GT_BOARD).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
    def verify_gt_summary_module(self):

        self.driver.find_element(*self.GT_SUMMARY).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.GT_TOTAL_ISSUES).is_displayed()
        assert self.driver.find_element(*self.GT_OPEN_ISSUES).is_displayed()
        assert self.driver.find_element(*self.GT_CLOSED_STATUS).is_displayed()
        assert self.driver.find_element(*self.GT_UPDATED_STATUS).is_displayed()
        assert self.driver.find_element(*self.GT_DATE_FILTER).is_displayed()
        assert self.driver.find_element(*self.GT_EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_ISSUE_STATUS).is_displayed()
        assert self.driver.find_element(*self.GT_PRIORITY_BREAKDOWN).is_displayed()
        assert self.driver.find_element(*self.GT_PRIORITY_SPLIT).is_displayed()
        assert self.driver.find_element(*self.GT_ISSUE_TREND).is_displayed()
        assert self.driver.find_element(*self.GT_COMPLETION_RATE).is_displayed()
        assert self.driver.find_element(*self.GT_TEAM_WORKLOAD).is_displayed()
        assert self.driver.find_element(*self.GT_CYCLE_TIME_DISTRIBUTION).is_displayed()
        assert self.driver.find_element(*self.GT_ASSIGNE_VS_TRACKER).is_displayed()


        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.GT_DATE_FILTER).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.GT_DATE_FILTER_RADIO_BTN).is_displayed()
        
        self.driver.find_element(*self.GT_UPDATE_BTN).is_displayed()
        
        self.driver.find_element(*self.GT_DATE_FILTER_CLOSE_CLICK).click()
        
        self.driver.find_element(*self.GT_EXPORT_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.GT_EXPORT_AS_CSV_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_EXPORT_AS_HTML_BTN).is_displayed()
        
        self.driver.find_element(*self.GT_EXPORT_CLOSE_CLICK).click()
        
        
    def verify_gt_reports_module(self):

        self.driver.find_element(*self.GT_REPORTS).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.GT_REPORTS_SEARCH_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_FROM_DATE).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_END_DATE).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_EXPORT_BUTTON).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_CHECK_BOX).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_PAGINATOR_DROPDOWN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_RIGHT_FULL_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_RIGHT_NAVIGATE_BTN).is_displayed()
    
        self.driver.find_element(*self.GT_REPORTS_EXPORT_BUTTON).click()
        
        assert self.driver.find_element(*self.GT_REPORTS_EXPORT_EXCEL_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_REPORTS_EXPORT_AS_HTML_BTN).is_displayed()
        self.driver.find_element(*self.GT_REPORTS_EXPORT_CLOSE_CLICK).click()
        
        
    def verify_gt_lists_module(self):

        self.driver.find_element(*self.GT_LISTS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.GT_LISTS_SEARCH_ISSUES)
        )

        assert self.driver.find_element(*self.GT_LISTS_SEARCH_ISSUES).is_displayed()
        assert self.driver.find_element(*self.GT_LIST_CHECKBOX_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_CREATE_BTN).is_displayed()

        self.driver.find_element(*self.GT_LISTS_CREATE_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.GT_LISTS_TASK_BTN)
        )

        if self.is_task_only_project():
         self.verify_gt_task_only()

        elif self.is_task_bug_story_epic_project():
         self.verify_gt_task_bug_story_epic()

        elif self.is_all_tracker_project():
         self.verify_gt_all_trackers()

        else:
         raise Exception(f"No GT tracker configuration found for {self.selected_team}") 
        self.driver.find_element(*self.GT_LISTS_CLOSE_ICON).click()

        assert self.driver.find_element(*self.GT_LISTS_EXPORT_BTN).is_displayed()
        self.driver.find_element(*self.GT_LISTS_EXPORT_BTN).click()
        
        assert self.driver.find_element(*self.GT_LISTS_EXPORT_CSV_DEF).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_EXPORT_CSV_ALL_FIELDS).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_EXPORT_HTML_ALL_FIELDS).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_EXPORT_HTML_DEF).is_displayed()
        self.driver.find_element(*self.GT_LISTS_EXPORT_CLOSE_CLICK).click()
        
        time.sleep(Config.LONG_WAIT)
        
        
        assert self.driver.find_element(*self.GT_LISTS_ITEMS_PER_PAGE).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_FULL_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_FULL_RIGHT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_RIGHT_NAVIGATION_BTN).is_displayed()
        
        
        
    def verify_gt_task_only(self):

       assert self.driver.find_element(*self.GT_LISTS_TASK_BTN).is_displayed()

       print(f"{self.selected_team} -> GT Lists: Task only verified.") 
        
        
    def verify_gt_task_bug_story_epic(self):

        assert self.driver.find_element(*self.GT_LISTS_TASK_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_BUG_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_STORY_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_EPIC_BTN).is_displayed()

        print(f"{self.selected_team} -> GT Lists: Task, Bug, Story and Epic verified.")   
        
        
    def verify_gt_all_trackers(self):

        assert self.driver.find_element(*self.GT_LISTS_TASK_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_BUG_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_EPIC_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_CR_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_PROD_BUG).is_displayed()
        assert self.driver.find_element(*self.GT_LISTS_STORY_BTN).is_displayed()

        print(f"{self.selected_team} -> GT Lists: All trackers verified.")   
        
        
        
    def verify_gt_timesheets_module(self):

        timesheets_btn = self.driver.find_element(*self.GT_TIMESHEETS_BTN)
        self.driver.execute_script("arguments[0].click();", timesheets_btn)

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.GT_TIMESHEETS_EXPORT_BTN).is_displayed()
        self.driver.find_element(*self.GT_TIMESHEETS_EXPORT_BTN).click()
        assert self.driver.find_element(*self.GT_TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL).is_displayed()
        assert self.driver.find_element(*self.GT_TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML).is_displayed()
        self.driver.find_element(*self.GT_TIMESHEETS_EXPORT_CLOSE_CLICK).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.GT_TIMESHEETS_PROJECT_ISSUE).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_TIMESHEET_CARD).is_displayed()
        
        self.driver.find_element(*self.GT_TIMESHEETS_PROJECT_LEFT_NAV_BTN).click()
        self.driver.find_element(*self.GT_TIMESHEETS_PROJECT_RIGHT_NAV_BTN).click()
        
        assert self.driver.find_element(*self.GT_TIMESHEETS_PROJECT_LEFT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_PROJECT_RIGHT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_APPROVAL).is_displayed()
        
        self.driver.find_element(*self.GT_TIMESHEETS_APPROVAL).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.GT_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).click()
        self.driver.find_element(*self.TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.GT_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).is_displayed() 
        assert self.driver.find_element(*self.GT_TIMESHEETS_APPROVED).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_READY_TO_SUBMIT).is_displayed()
        assert self.driver.find_element(*self.GT_TIMESHEETS_WAITING_FOR_APPROVAL).is_displayed()
       
    def verify_gt_users_module(self):

        self.driver.find_element(*self.GT_USERS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.GT_USERS_SEARCH_FIELD)
        )

        assert self.driver.find_element(*self.GT_USERS_SEARCH_FIELD).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_ADD_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_PAGINATOR_DRPDWN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_FULL_RIGHT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_RIGHT_NAVIGATE_BTN).is_displayed()
        
        
        self.driver.find_element(*self.GT_USERS_ADD_USER_BTN).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.GT_USERS_CREATE_NEWUSER_USRNAME).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_CREATE_NEWUSER_PWD).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_EMP_USERNAME).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_EMP_EMAIL).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_EMP_TEL_NO).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_ASSGN_PROJECT_DROPDWN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_ASSGN_PROJ_ROLE).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_CREATE_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_CANCEL_BTN).is_displayed()
        assert self.driver.find_element(*self.GT_USERS_BACK_BTN).is_displayed()

      
        self.driver.find_element(*self.GT_USERS_BACK_BTN).click()
     
     
      ##---------------------------  BUGBOARD---------------------------------------------------------
    
    
    
    def open_bugs_board(self):    
        
        self.driver.find_element(*self.BUGS_BOARD).click()
        
        time.sleep(Config.MEDIUM_WAIT)
    
    def verify_bugs_board(self):

        self.driver.find_element(*self.HOME_BUTTON).click()

        time.sleep(Config.MEDIUM_WAIT)

        assert self.driver.find_element(*self.BUGS_BOARD).is_displayed()

        self.driver.find_element(*self.BUGS_BOARD).click()

        time.sleep(Config.MEDIUM_WAIT)


    def verify_bugs_kanban_module(self):
        
       assert self.driver.find_element(*self.BUGS_KANBAN_SELECT_BOARD).is_displayed()
        
       assert self.driver.find_element(*self.BUGS_OPEN_BACKLOG).is_displayed()
       assert self.driver.find_element(*self.BUGS_INPROGRESS).is_displayed()
       assert self.driver.find_element(*self.BUGS_CLARIFICATION_LIST).is_displayed()
       assert self.driver.find_element(*self.BUGS_RELEASE_QA).is_displayed()
       assert self.driver.find_element(*self.BUGS_FIXED_LIST).is_displayed()
       assert self.driver.find_element(*self.BUGS_CLOSED_DONE).is_displayed()
       assert self.driver.find_element(*self.BUGS_REJECTED).is_displayed()
       assert self.driver.find_element(*self.BUGS_DEFFERED_LIST).is_displayed()
       assert self.driver.find_element(*self.BUGS_NOTREPRO).is_displayed()
       
       assert self.driver.find_element(*self.BUGS_KANBAN_SELECT_BOARD).is_displayed()
       
       self.driver.find_element(*self.BUGS_KANBAN_SELECT_BOARD).click()
       
       assert self.driver.find_element(*self.BUGS_SELECT_GT_BOARD).is_displayed()
       assert self.driver.find_element(*self.BUGS_SELECT_BUGS_BOARD).is_displayed()
       
       
       
       
    def verify_bugs_summary_module(self):

        self.driver.find_element(*self.BUGS_SUMMARY).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.BUGS_TOTAL_ISSUES).is_displayed()
        assert self.driver.find_element(*self.BUGS_OPEN_ISSUES).is_displayed()
        assert self.driver.find_element(*self.BUGS_CLOSED_STATUS).is_displayed()
        assert self.driver.find_element(*self.BUGS_UPDATED_STATUS).is_displayed()
        assert self.driver.find_element(*self.BUGS_DATE_FILTER).is_displayed()
        assert self.driver.find_element(*self.BUGS_EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_ISSUE_STATUS).is_displayed()
        assert self.driver.find_element(*self.BUGS_PRIORITY_BREAKDOWN).is_displayed()
        assert self.driver.find_element(*self.BUGS_PRIORITY_SPLIT).is_displayed()
        assert self.driver.find_element(*self.BUGS_ISSUE_TREND).is_displayed()
        assert self.driver.find_element(*self.BUGS_COMPLETION_RATE).is_displayed()
        assert self.driver.find_element(*self.BUGS_TEAM_WORKLOAD).is_displayed()
        assert self.driver.find_element(*self.BUGS_CYCLE_TIME_DISTRIBUTION).is_displayed()
        assert self.driver.find_element(*self.BUGS_ASSIGNE_VS_TRACKER).is_displayed()


        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BUGS_DATE_FILTER).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BUGS_DATE_FILTER_RADIO_BTN).is_displayed()
        
        self.driver.find_element(*self.BUGS_UPDATE_BTN).is_displayed()
        
        self.driver.find_element(*self.BUGS_SUMMARY_CLOSE_CLICK).click()
        
        self.driver.find_element(*self.BUGS_EXPORT_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.BUGS_EXPORT_AS_CSV_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_EXPORT_AS_HTML_BTN).is_displayed()
        
        self.driver.find_element(*self.BUGS_SUMMARY_CLOSE_CLICK).click()
    
    def verify_bugs_reports_module(self):

        self.driver.find_element(*self.BUGS_REPORTS).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.BUGS_REPORTS_SEARCH_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_FROM_DATE).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_END_DATE).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_EXPORT_BUTTON).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_CHECK_BOX).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_PAGINATOR_DROPDOWN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_RIGHT_FULL_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_RIGHT_NAVIGATE_BTN).is_displayed()
    
        self.driver.find_element(*self.BUGS_REPORTS_EXPORT_BUTTON).click()
        
        assert self.driver.find_element(*self.BUGS_REPORTS_EXPORT_EXCEL_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_REPORTS_EXPORT_AS_HTML_BTN).is_displayed()
        self.driver.find_element(*self.BUGS_REPORTS_EXPORT_CLOSE_CLICK).click()
    
    
    def verify_bugs_lists_module(self):

        self.driver.find_element(*self.BUGS_LISTS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.BUGS_LISTS_SEARCH_ISSUES)
        )

        assert self.driver.find_element(*self.BUGS_LISTS_SEARCH_ISSUES).is_displayed()
        assert self.driver.find_element(*self.BUGS_LIST_CHECKBOX_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_CREATE_BTN).is_displayed()

        self.driver.find_element(*self.BUGS_LISTS_CREATE_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.BUGS_LISTS_TASK_BTN)
        )
        
        if self.is_task_only_project():
         self.verify_bugs_task_only()

        elif self.is_task_bug_story_epic_project():
              self.verify_bugs_task_bug_story_epic()

        elif self.is_all_tracker_project():
           self.verify_bugs_all_trackers()

        else:
         raise Exception(f"No Bugs tracker configuration found for {self.selected_team}") 
        
        self.driver.find_element(*self.BUGS_LISTS_CLOSE_ICON).click()

        assert self.driver.find_element(*self.BUGS_LISTS_EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_PAGINATION).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_FULL_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_FULL_RIGHT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_LEFT_NAVIGATION_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_RIGHT_NAVIGATION_BTN).is_displayed()
        
        self.driver.find_element(*self.BUGS_LISTS_EXPORT_BTN).click()
        assert self.driver.find_element(*self.BUGS_LISTS_EXPORT_CSV_ALL_FIELDS).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_EXPORT_CSV_DEF).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_EXPORT_HTML_ALL_FIELDS).is_displayed()
        assert self.driver.find_element(*self.BUGS_LISTS_EXPORT_HTML_DEF).is_displayed()
        self.driver.find_element(*self.BUGS_LISTS_EXPORT_CLOSE_CLICK).click()
        
        
    def verify_bugs_task_only(self):

        assert self.driver.find_element(*self.BUGS_LISTS_TASK_BTN).is_displayed()

        print(f"{self.selected_team} -> Bugs Lists: Task only verified.")
        
        
    def verify_bugs_task_bug_story_epic(self):

       assert self.driver.find_element(*self.BUGS_LISTS_TASK_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_BUG_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_STORY_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_EPIC_BTN).is_displayed()

       print(f"{self.selected_team} -> Bugs Lists: Task, Bug, Story and Epic verified.")
        
     
    def verify_bugs_all_trackers(self):

       assert self.driver.find_element(*self.BUGS_LISTS_TASK_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_BUG_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_PROD_BUG).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_CR_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_STORY_BTN).is_displayed()
       assert self.driver.find_element(*self.BUGS_LISTS_EPIC_BTN).is_displayed()

       print(f"{self.selected_team} -> All trackers verified.")
    
    #def verify_bugs_allworks_module(self):
        
     #   assert self.driver.find_element(*self.BUGS_ALLWORKS_BTN).is_displayed()
      #  self.driver.find_element(*self.BUGS_ALLWORKS_BTN).click()
        
       # print(self.driver.find_element(*self.BUGS_ALLWORKS_BTN).is_displayed())

     
     
        
    def verify_bugs_timesheets_module(self):

        timesheets_btn = self.driver.find_element(*self.BUGS_TIMESHEETS_BTN)
        self.driver.execute_script("arguments[0].click();", timesheets_btn)

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.BUGS_TIMESHEETS_EXPORT_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_PROJECT_LEFT_NAV_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_PROJECT_RIGHT_NAV_BTN).is_displayed()  
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL).is_displayed()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BUGS_TIMESHEETS_PROJECT_LEFT_NAV_BTN).click()
        self.driver.find_element(*self.BUGS_TIMESHEETS_PROJECT_RIGHT_NAV_BTN).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_PROJECT_ISSUE).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_TIMESHEET_CARD).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL).is_displayed()
        
        self.driver.find_element(*self.BUGS_TIMESHEETS_EXPORT_BTN).click()
        assert self.driver.find_element(*self.BUGS_TIME_SHEETS_EXPORT_DOWNLOAD_AS_EXCEL).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIME_SHEETS_EXPORT_DOWNLOAD_AS_HTML).is_displayed()
        
        self.driver.find_element(*self.BUGS_TIMESHEETS_EXPORT_CLOSE_CLICK).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL).click()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_WAITING_FOR_APPROVAL).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVED).is_displayed()
        assert self.driver.find_element(*self.BUGS_TIMESHEETS_READY_TO_SUBMIT).is_displayed()
        
        time.sleep(Config.MEDIUM_WAIT)
        
        self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL_PREVIOUS_WEEK_NAVIGATE_BTN).click()
        time.sleep(Config.MEDIUM_WAIT)
        self.driver.find_element(*self.BUGS_TIMESHEETS_APPROVAL_NEXT_WEEK_NAVIGATE_BTN).click()
        

    def verify_bugs_users_module(self):

        self.driver.find_element(*self.BUGS_USERS_BTN).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.BUGS_USERS_SEARCH_FIELD)
        )

        assert self.driver.find_element(*self.BUGS_USERS_SEARCH_FIELD).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_ADD_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_PAGINATOR_DRPDWN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_FULL_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_FULL_RIGHT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_LEFT_NAVIGATE_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_RIGHT_NAVIGATE_BTN).is_displayed()
        
        self.driver.find_element(*self.BUGS_USERS_ADD_USER_BTN).click()

        time.sleep(Config.LONG_WAIT)

        assert self.driver.find_element(*self.BUGS_USERS_CREATE_NEWUSER_USRNAME).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_CREATE_NEWUSER_PWD).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_EMP_USERNAME).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_EMP_EMAIL).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_EMP_TEL_NO).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_ASSGN_PROJECT_DROPDWN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_ASSGN_PROJ_ROLE).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_CREATE_USER_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_CANCEL_BTN).is_displayed()
        assert self.driver.find_element(*self.BUGS_USERS_BACK_BTN).is_displayed()

        self.driver.find_element(*self.BUGS_USERS_BACK_BTN).click()
    