"""'Followers' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_followers(permissions, driver, debug):
    """handle Followers permissions"""
    move_to_the_followers_menu(driver, debug)
    open_followers_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Followers'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_followers_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_followers_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_followers_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Followers' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Email addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_followers_menu(driver, debug):
    """move to the 'Followers' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Followers' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Followers' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_followers_menu(driver, debug):
    """open the 'Followers' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Followers' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Followers' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_followers_no_access(driver, debug):
    """select 'No access' in the 'Followers' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Followers' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Followers' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_followers_read_only(driver, debug):
    """select 'Read-only' in the 'Followers' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Followers' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Followers' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_followers_read_and_write(driver, debug):
    """select 'Read and write' in 'Followers' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Followers' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
