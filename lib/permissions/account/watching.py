"""'Watching' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_watching(permissions, driver, debug):
    """handle Watching permissions"""
    move_to_the_watching_menu(driver, debug)
    open_watching_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Watching'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_watching_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_watching_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_watching_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Watching' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Starring' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_watching_menu(driver, debug):
    """move to the 'Watching' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Watching' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Watching' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_watching_menu(driver, debug):
    """open the 'Watching' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Watching' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Watching' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_watching_no_access(driver, debug):
    """select 'No access' in the 'Watching' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Watching' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Watching' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_watching_read_only(driver, debug):
    """select 'Read-only' in the 'Watching' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Watching' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Watching' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_watching_read_and_write(driver, debug):
    """select 'Read and write' in 'Watching' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Watching' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
