"""functions related to 'Codespaces_Lifecycle_Admin' repository permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_codespaces_lifecycle_admin(permissions, driver, debug):
    """handle Codespaces_Lifecycle_Admin permissions"""
    move_to_the_codespaces_lifecycle_admin_menu(driver, debug)
    open_codespaces_lifecycle_admin_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to " +
                   "'Codespaces_Lifecycle_Admin'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_codespaces_lifecycle_admin_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_codespaces_lifecycle_admin_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_codespaces_lifecycle_admin_read_and_write(driver, debug)
    else:
        printerr_exit(
            "Unexpected 'Codespaces_Lifecycle_Admin' permissions: "
            f"'{permissions}'")


# Note: This function assumes the active element is
#       the 'Codespaces' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_codespaces_lifecycle_admin_menu(driver, debug):
    """move to the 'Codespaces_Lifecycle_Admin' permissions menu"""
    if debug:
        printdebug(
            "moving to the 'Codespaces_Lifecycle_Admin' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Codespaces_Lifecycle_Admin' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_codespaces_lifecycle_admin_menu(driver, debug):
    """open the 'Codespaces_Lifecycle_Admin' permissions menu"""
    if debug:
        printdebug("opening the 'Codespaces_Lifecycle_Admin' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Codespaces_Lifecycle_Admin' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_codespaces_lifecycle_admin_read_only(driver, debug):
    """select 'Read-only' in the 'Codespaces_Lifecycle_Admin' menu"""
    if debug:
        printdebug(
            "selecting 'Read-only' in the 'Codespaces_Lifecycle_Admin' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Codespaces_Lifecycle_Admin' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_codespaces_lifecycle_admin_read_and_write(driver, debug):
    """select 'Read and write' in the 'Codespaces_Lifecycle_Admin' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the " +
            "'Codespaces_Lifecycle_Admin' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Codespaces_Lifecycle_Admin' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_codespaces_lifecycle_admin_no_access(driver, debug):
    """select 'No access' in the 'Codespaces_Lifecycle_Admin' menu"""
    if debug:
        printdebug(
            "selecting 'No access' in the " +
            "'Codespaces_Lifecycle_Admin' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
