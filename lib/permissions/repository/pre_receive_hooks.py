"""functions related to 'Pre_Receive_Hooks' repository permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_pre_receive_hooks(permissions, driver, debug):
    """handle Pre_Receive_Hooks permissions"""
    move_to_the_pre_receive_hooks_menu(driver, debug)
    open_pre_receive_hooks_menu(driver, debug)
    if debug:
        printdebug(
            "determining which permissions to give to 'Pre_Receive_Hooks'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_pre_receive_hooks_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_pre_receive_hooks_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_pre_receive_hooks_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Pre_Receive_Hooks' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Pages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_pre_receive_hooks_menu(driver, debug):
    """move to the 'Pre_Receive_Hooks' permissions menu"""
    if debug:
        printdebug("moving to the 'Pre_Receive_Hooks' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Pre_Receive_Hooks' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_pre_receive_hooks_menu(driver, debug):
    """open the 'Pre_Receive_Hooks' permissions menu"""
    if debug:
        printdebug("opening the 'Pre_Receive_Hooks' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Pre_Receive_Hooks' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pre_receive_hooks_read_only(driver, debug):
    """select 'Read-only' in the 'Pre_Receive_Hooks' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Pre_Receive_Hooks' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Pre_Receive_Hooks' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pre_receive_hooks_read_and_write(driver, debug):
    """select 'Read and write' in the 'Pre_Receive_Hooks' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the 'Pre_Receive_Hooks' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Pre_Receive_Hooks' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pre_receive_hooks_no_access(driver, debug):
    """select 'No access' in the 'Pre_Receive_Hooks' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Pre_Receive_Hooks' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
