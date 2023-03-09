"""functions related to 'Self_Hosted_Runners' organization permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_self_hosted_runners(permissions, driver, debug):
    """handle Self_Hosted_Runners permissions"""
    move_to_the_self_hosted_runners_menu(driver, debug)
    open_self_hosted_runners_menu(driver, debug)
    if debug:
        printdebug(
            "determining which permissions to give to 'Self_Hosted_Runners'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_self_hosted_runners_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_self_hosted_runners_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_self_hosted_runners_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Self_Hosted_Runners' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Secrets' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_self_hosted_runners_menu(driver, debug):
    """move to the 'Self_Hosted_Runners' permissions menu"""
    if debug:
        printdebug("moving to the 'Self_Hosted_Runners' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Self_Hosted_Runners' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_self_hosted_runners_menu(driver, debug):
    """open the 'Self_Hosted_Runners' permissions menu"""
    if debug:
        printdebug("opening the 'Self_Hosted_Runners' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Self_Hosted_Runners' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_self_hosted_runners_no_access(driver, debug):
    """select 'No access' in the 'Self_Hosted_Runners' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Self_Hosted_Runners' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Self_Hosted_Runners' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_self_hosted_runners_read_only(driver, debug):
    """select 'Read-only' in the 'Self_Hosted_Runners' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Self_Hosted_Runners' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Self_Hosted_Runners' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_self_hosted_runners_read_and_write(driver, debug):
    """select 'Read and write' in the 'Self_Hosted_Runners' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the 'Self_Hosted_Runners' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
