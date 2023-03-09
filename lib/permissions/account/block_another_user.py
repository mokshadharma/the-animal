"""'Block_Another_User' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_block_another_user(permissions, driver, debug):
    """handle Block_Another_User permissions"""
    move_to_the_block_another_user_menu(driver, debug)
    open_block_another_user_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Block_Another_User'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_block_another_user_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_block_another_user_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_block_another_user_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Block_Another_User' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Account permissions' section
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_block_another_user_menu(driver, debug):
    """move to the 'Block_Another_User' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Block_Another_User' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Block_Another_User' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_block_another_user_menu(driver, debug):
    """open the 'Block_Another_User' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Block_Another_User' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Block_Another_User' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_block_another_user_no_access(driver, debug):
    """select 'No access' in the 'Block_Another_User' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Block_Another_User' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Block_Another_User' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_block_another_user_read_only(driver, debug):
    """select 'Read-only' in the 'Block_Another_User' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Block_Another_User' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Block_Another_User' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_block_another_user_read_and_write(driver, debug):
    """select 'Read and write' in 'Block_Another_User' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Block_Another_User' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
