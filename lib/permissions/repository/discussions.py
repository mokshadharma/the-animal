"""functions related to 'Discussions' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_discussions(permissions, driver, debug):
    """handle Discussions permissions"""
    move_to_the_discussions_menu(driver, debug)
    open_discussions_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Discussions'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_discussions_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_discussions_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_discussions_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Discussions' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Deployments' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_discussions_menu(driver, debug):
    """move to the 'Discussions' permissions menu"""
    if debug:
        printdebug("moving to the 'Discussions' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_discussions_menu(driver, debug):
    """open the 'Discussions' permissions menu"""
    if debug:
        printdebug("opening the 'Discussions' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_discussions_no_access(driver, debug):
    """select 'No access' in the 'Discussions' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_discussions_read_only(driver, debug):
    """select 'Read-only' in the 'Discussions' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_discussions_read_and_write(driver, debug):
    """select 'Read and write' in the 'Discussions' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
