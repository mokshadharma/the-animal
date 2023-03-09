"""functions related to 'Issues' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_issues(permissions, driver, debug):
    """handle Issues permissions"""
    move_to_the_issues_menu(driver, debug)
    open_issues_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Issues'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_issues_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_issues_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_issues_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Issues' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Environments' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_issues_menu(driver, debug):
    """move to the 'Issues' permissions menu"""
    if debug:
        printdebug("moving to the 'Issues' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Issues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_issues_menu(driver, debug):
    """open the 'Issues' permissions menu"""
    if debug:
        printdebug("opening the 'Issues' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Issues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_issues_no_access(driver, debug):
    """select 'No access' in the 'Issues' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Issues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Issues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_issues_read_only(driver, debug):
    """select 'Read-only' in the 'Issues' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Issues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Issues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_issues_read_and_write(driver, debug):
    """select 'Read and write' in the 'Issues' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Issues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
