"""functions related to 'Pages' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_pages(permissions, driver, debug):
    """handle Pages permissions"""
    move_to_the_pages_menu(driver, debug)
    open_pages_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Pages'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_pages_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_pages_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_pages_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Pages' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Packages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_pages_menu(driver, debug):
    """move to the 'Pages' permissions menu"""
    if debug:
        printdebug("moving to the 'Pages' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Pages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_pages_menu(driver, debug):
    """open the 'Pages' permissions menu"""
    if debug:
        printdebug("opening the 'Pages' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Pages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pages_read_only(driver, debug):
    """select 'Read-only' in the 'Pages' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Pages' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Pages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pages_read_and_write(driver, debug):
    """select 'Read and write' in the 'Pages' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Pages' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Pages' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_pages_no_access(driver, debug):
    """select 'No access' in the 'Pages' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Pages' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
