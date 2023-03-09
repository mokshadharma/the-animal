"""functions related to 'Variables' organization permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_variables(permissions, driver, debug):
    """handle Variables permissions"""
    move_to_the_variables_menu(driver, debug)
    open_variables_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Variables'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_variables_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_variables_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_variables_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Variables' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Team discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_variables_menu(driver, debug):
    """move to the 'Variables' permissions menu"""
    if debug:
        printdebug("moving to the 'Variables' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Variables' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_variables_menu(driver, debug):
    """open the 'Variables' permissions menu"""
    if debug:
        printdebug("opening the 'Variables' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Variables' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_variables_read_only(driver, debug):
    """select 'Read-only' in the 'Variables' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Variables' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Variables' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_variables_read_and_write(driver, debug):
    """select 'Read and write' in the 'Variables' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Variables' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Variables' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_variables_no_access(driver, debug):
    """select 'No access' in the 'Variables' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Variables' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
