"""'Email_Addresses' account perms functions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_email_addresses(permissions, driver, debug):
    """handle Email_Addresses permissions"""
    move_to_the_email_addresses_menu(driver, debug)
    open_email_addresses_menu(driver, debug)
    if debug:
        printdebug('determining which permissions to give ' +
                   "to 'Email_Addresses'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_email_addresses_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_email_addresses_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_email_addresses_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Email_Addresses' permissions: " +
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Codespaces user secrets' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_email_addresses_menu(driver, debug):
    """move to the 'Email_Addresses' permissions menu"""
    if debug:
        printdebug(
            "moving to the " +
            "'Email_Addresses' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Email_Addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_email_addresses_menu(driver, debug):
    """open the 'Email_Addresses' permissions menu"""
    if debug:
        printdebug(
            "opening the 'Email_Addresses' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Email_Addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_email_addresses_no_access(driver, debug):
    """select 'No access' in the 'Email_Addresses' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Email_Addresses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Email_Addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_email_addresses_read_only(driver, debug):
    """select 'Read-only' in the 'Email_Addresses' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the " +
            "'Email_Addresses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Email_Addresses' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_email_addresses_read_and_write(driver, debug):
    """select 'Read and write' in 'Email_Addresses' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Email_Addresses' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
