"""functions related to 'Merge_Queues' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_merge_queues(permissions, driver, debug):
    """handle Merge_Queues permissions"""
    move_to_the_merge_queues_menu(driver, debug)
    open_merge_queues_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Merge_Queues'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_merge_queues_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_merge_queues_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_merge_queues_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Merge_Queues' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Issues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_merge_queues_menu(driver, debug):
    """move to the 'Merge_Queues' permissions menu"""
    if debug:
        printdebug("moving to the 'Merge_Queues' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Merge_Queues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_merge_queues_menu(driver, debug):
    """open the 'Merge_Queues' permissions menu"""
    if debug:
        printdebug("opening the 'Merge_Queues' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Merge_Queues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_merge_queues_no_access(driver, debug):
    """select 'No access' in the 'Merge_Queues' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Merge_Queues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Merge_Queues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_merge_queues_read_only(driver, debug):
    """select 'Read-only' in the 'Merge_Queues' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Merge_Queues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Merge_Queues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_merge_queues_read_and_write(driver, debug):
    """select 'Read and write' in the 'Merge_Queues' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Merge_Queues' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
