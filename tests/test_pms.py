import pytest
from selenium import webdriver

from config.config import Config
from pages.login_page import LoginPage
from pages.home_page import HomePage


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", Config.CHROME_PREFS)
    options.add_argument("--incognito")
    options.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(Config.BASE_URL)

    return driver


def login_and_get_home_page():
    driver = setup_driver()
    login_page = LoginPage(driver)
    login_page.login()
    return driver, HomePage(driver)


# --- Login ---

def test_login():
    driver = setup_driver()
    try:
        LoginPage(driver).login()
    finally:
        driver.quit()







# --- Home Page ---

def test_verify_home_page():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.verify_home_page()
    finally:
        driver.quit()


####-----------------Verify scrum board based on manager------------------

def open_scrum_if_available(home_page):


    if not home_page.has_scrum_board():
        pytest.skip("Scrum Board not available for this project")

    home_page.open_scrum_board()




def test_verify_create_btn():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.verify_create_btn()
    finally:
        driver.quit()


# --- Scrum Board Modules ---

def test_verify_active_sprint_module():
    driver, home_page = login_and_get_home_page()

    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()

        open_scrum_if_available(home_page)
        home_page.verify_active_sprint_module()
    finally:
        driver.quit()

def test_verify_summary_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()

        open_scrum_if_available(home_page)
        home_page.verify_summary_module()
    finally:
        driver.quit()


def test_verify_backlog_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()

        open_scrum_if_available(home_page)
        home_page.verify_backlog_module()
    finally:
        driver.quit()


"""def test_verify_allworks_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.open_scrum_board()
        home_page.verify_allworks_module()
    finally:
        driver.quit() """




def test_verify_reports_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        open_scrum_if_available(home_page)
        home_page.verify_reports_module()
    finally:
        driver.quit()


def test_verify_lists_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        open_scrum_if_available(home_page)
        home_page.verify_lists_module()
    finally:
        driver.quit()


def test_verify_timesheets_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        open_scrum_if_available(home_page)
        home_page.verify_timesheets_module()
    finally:
        driver.quit()


def test_verify_users_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        open_scrum_if_available(home_page)
        home_page.verify_users_module()
    finally:
        driver.quit()


# --- GT Board Modules ---

def test_verify_gt_board():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_board()
    finally:
        driver.quit()


def test_verify_kanban_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_kanban_module()
    finally:
        driver.quit()
        
        
def test_verify_gt_summary_module():       
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_summary_module()
    finally:
        driver.quit()






def test_verify_gt_reports_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_reports_module()
    finally:
        driver.quit()

def test_verify_gt_lists_module():       
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_lists_module()
    finally:
        driver.quit()


def test_verify_gt_timesheets_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_timesheets_module()
    finally:
        driver.quit()



def test_verify_gt_users_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_gt_board()
        home_page.verify_gt_users_module()
    finally:
        driver.quit()

"""-------------------BUGS BOARD---------------------------------------"""



def test_verify_bugs_board():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_bugs_board()
        home_page.verify_bugs_board()
    finally:
        driver.quit()

def test_verify_bugs_summary_module():       
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_bugs_board()
        home_page.verify_bugs_summary_module()
    finally:
        driver.quit()



"""def test_verify_bugs_allworks_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.open_bugs_board()
        home_page.verify_bugs_allworks_module()
    finally:
        driver.quit()"""

def test_verify_bugs_reports_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.navigate_board()
        home_page.open_bugs_board()
        home_page.verify_bugs_reports_module()
    finally:
        driver.quit()


def test_verify_bugs_lists_module():       
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.open_bugs_board()
        home_page.verify_bugs_lists_module()
    finally:
        driver.quit()


def test_verify_bugs_timesheets_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.open_bugs_board()
        home_page.verify_bugs_timesheets_module()
    finally:
        driver.quit()



def test_verify_bugs_users_module():
    driver, home_page = login_and_get_home_page()
    try:
        home_page.select_filter_by_projects()
        home_page.open_bugs_board()
        home_page.verify_bugs_users_module()
    finally:
        driver.quit()
