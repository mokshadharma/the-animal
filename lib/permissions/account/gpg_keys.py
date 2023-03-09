"""'Gpg_Keys' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_gpg_keys(permissions, driver, debug):
    """handle Gpg_Keys permissions"""
    move_to_the_gpg_keys_menu(driver, debug)
    open_gpg_keys_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Gpg_Keys'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_gpg_keys_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_gpg_keys_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_gpg_keys_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Gpg_Keys' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Followers' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_gpg_keys_menu(driver, debug):
    """move to the 'Gpg_Keys' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Gpg_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Gpg_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_gpg_keys_menu(driver, debug):
    """open the 'Gpg_Keys' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Gpg_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Gpg_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_gpg_keys_no_access(driver, debug):
    """select 'No access' in the 'Gpg_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Gpg_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Gpg_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_gpg_keys_read_only(driver, debug):
    """select 'Read-only' in the 'Gpg_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Gpg_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Gpg_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_gpg_keys_read_and_write(driver, debug):
    """select 'Read and write' in 'Gpg_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Gpg_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
