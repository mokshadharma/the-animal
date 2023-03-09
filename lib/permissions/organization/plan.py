"""functions related to 'Plan' organization permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_plan(permissions, driver, debug):
    """handle Plan permissions"""
    move_to_the_plan_menu(driver, debug)
    open_plan_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Plan'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_plan_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_plan_read_only(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Plan' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Organization Dependabot Secrets' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_plan_menu(driver, debug):
    """move to the 'Plan' permissions menu"""
    if debug:
        printdebug("moving to the 'Plan' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Plan' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_plan_menu(driver, debug):
    """open the 'Plan' permissions menu"""
    if debug:
        printdebug("opening the 'Plan' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Plan' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_plan_no_access(driver, debug):
    """select 'No access' in the 'Plan' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Plan' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Plan' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_plan_read_only(driver, debug):
    """select 'Read-only' in the 'Plan' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Plan' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
