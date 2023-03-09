"""'Gists' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_gists(permissions, driver, debug):
    """handle Gists permissions"""
    move_to_the_gists_menu(driver, debug)
    open_gists_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Gists'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_gists_no_access(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_gists_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Gists' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'GPG keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_gists_menu(driver, debug):
    """move to the 'Gists' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Gists' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Gists' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_gists_menu(driver, debug):
    """open the 'Gists' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Gists' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Gists' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_gists_no_access(driver, debug):
    """select 'No access' in the 'Gists' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Gists' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Gists' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_gists_read_and_write(driver, debug):
    """select 'Read and write' in 'Gists' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Gists' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
