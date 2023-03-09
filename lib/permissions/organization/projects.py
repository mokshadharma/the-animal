"""functions related to 'Projects' organization permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_projects(permissions, driver, debug):
    """handle Projects permissions"""
    move_to_the_projects_menu(driver, debug)
    open_projects_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Projects'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_projects_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_projects_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_projects_read_and_write(driver, debug)
    elif permissions == 'Admin':
        if debug:
            printdebug("Desired permissions: 'Admin'")
        select_projects_admin(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Projects' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Pre-receive hooks' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_projects_menu(driver, debug):
    """move to the 'Projects' permissions menu"""
    if debug:
        printdebug("moving to the 'Projects' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Projects' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_projects_menu(driver, debug):
    """open the 'Projects' permissions menu"""
    if debug:
        printdebug("opening the 'Projects' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Projects' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_projects_admin(driver, debug):
    """select 'Admin' in the 'Projects' menu"""
    if debug:
        printdebug("selecting 'Admin' in the 'Projects' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Projects' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_projects_no_access(driver, debug):
    """select 'No access' in the 'Projects' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Projects' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Projects' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_projects_read_only(driver, debug):
    """select 'Read-only' in the 'Projects' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Projects' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Projects' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_projects_read_and_write(driver, debug):
    """select 'Read and write' in the 'Projects' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Projects' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
