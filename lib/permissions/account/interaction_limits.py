"""'Interaction_Limits' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_interaction_limits(permissions, driver, debug):
    """handle Interaction_Limits permissions"""
    move_to_the_interaction_limits_menu(driver, debug)
    open_interaction_limits_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Interaction_Limits'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_interaction_limits_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_interaction_limits_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_interaction_limits_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Interaction_Limits' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Git SSH keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_interaction_limits_menu(driver, debug):
    """move to the 'Interaction_Limits' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Interaction_Limits' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Interaction_Limits' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_interaction_limits_menu(driver, debug):
    """open the 'Interaction_Limits' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Interaction_Limits' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Interaction_Limits' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_interaction_limits_no_access(driver, debug):
    """select 'No access' in the 'Interaction_Limits' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Interaction_Limits' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Interaction_Limits' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_interaction_limits_read_only(driver, debug):
    """select 'Read-only' in the 'Interaction_Limits' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Interaction_Limits' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Interaction_Limits' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_interaction_limits_read_and_write(driver, debug):
    """select 'Read and write' in 'Interaction_Limits' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Interaction_Limits' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
