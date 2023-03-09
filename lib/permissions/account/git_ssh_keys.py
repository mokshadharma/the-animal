"""'Git_Ssh_Keys' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_git_ssh_keys(permissions, driver, debug):
    """handle Git_Ssh_Keys permissions"""
    move_to_the_git_ssh_keys_menu(driver, debug)
    open_git_ssh_keys_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Git_Ssh_Keys'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_git_ssh_keys_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_git_ssh_keys_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_git_ssh_keys_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Git_Ssh_Keys' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Email addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_git_ssh_keys_menu(driver, debug):
    """move to the 'Git_Ssh_Keys' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Git_Ssh_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Git_Ssh_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_git_ssh_keys_menu(driver, debug):
    """open the 'Git_Ssh_Keys' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Git_Ssh_Keys' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Git_Ssh_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_git_ssh_keys_no_access(driver, debug):
    """select 'No access' in the 'Git_Ssh_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Git_Ssh_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Git_Ssh_Keys' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_git_ssh_keys_read_only(driver, debug):
    """select 'Read-only' in the 'Git_Ssh_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Git_Ssh_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Gists' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_git_ssh_keys_read_and_write(driver, debug):
    """select 'Read and write' in 'Git_Ssh_Keys' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Git_Ssh_Keys' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
