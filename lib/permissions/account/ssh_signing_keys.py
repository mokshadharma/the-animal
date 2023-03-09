"""'Ssh_Signing_Keys' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_ssh_signing_keys(permissions, driver, debug):
    """handle Ssh_Signing_Keys permissions"""
    move_to_the_ssh_signing_keys_menu(driver, debug)
    open_ssh_signing_keys_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Ssh_Signing_Keys'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_ssh_signing_keys_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_ssh_signing_keys_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_ssh_signing_keys_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Ssh_Signing_Keys' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Profile' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_ssh_signing_keys_menu(driver, debug):
    """move to the 'Ssh_Signing_Keys' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Ssh_Signing_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Ssh_Signing_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_ssh_signing_keys_menu(driver, debug):
    """open the 'Ssh_Signing_Keys' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Ssh_Signing_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Ssh_Signing_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_ssh_signing_keys_no_access(driver, debug):
    """select 'No access' in the 'Ssh_Signing_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Ssh_Signing_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Ssh_Signing_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_ssh_signing_keys_read_only(driver, debug):
    """select 'Read-only' in the 'Ssh_Signing_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Ssh_Signing_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Ssh_Signing_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_ssh_signing_keys_read_and_write(driver, debug):
    """select 'Read and write' in 'Ssh_Signing_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Ssh_Signing_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
