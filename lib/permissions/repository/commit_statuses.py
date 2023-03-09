"""functions related to 'Commit_Statuses' repository permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_commit_statuses(permissions, driver, debug):
    """handle Commit_Statuses permissions"""
    move_to_the_commit_statuses_menu(driver, debug)
    open_commit_statuses_menu(driver, debug)
    if debug:
        printdebug(
            "determining which permissions to give to 'Commit_Statuses'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_commit_statuses_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_commit_statuses_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_commit_statuses_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Commit_Statuses' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Codespaces secrets' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_commit_statuses_menu(driver, debug):
    """move to the 'Commit_Statuses' permissions menu"""
    if debug:
        printdebug("moving to the 'Commit_Statuses' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Commit_Statuses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_commit_statuses_menu(driver, debug):
    """open the 'Commit_Statuses' permissions menu"""
    if debug:
        printdebug("opening the 'Commit_Statuses' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Commit_Statuses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_commit_statuses_no_access(driver, debug):
    """select 'No access' in the 'Commit_Statuses' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Commit_Statuses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Commit_Statuses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_commit_statuses_read_only(driver, debug):
    """select 'Read-only' in the 'Commit_Statuses' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Commit_Statuses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Commit_Statuses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_commit_statuses_read_and_write(driver, debug):
    """select 'Read and write' in the 'Commit_Statuses' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Commit_Statuses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
