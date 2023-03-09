"""functions related to 'Metadata' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_metadata(perms, driver, debug):
    """handle Metadata permissions"""
    permissions = perms['metadata']
    move_to_the_metadata_menu(driver, debug)
    open_metadata_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Metadata'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        if any(v != 'No access' for v in perms.values()):
            printerr_exit(
                "metadata can only be set to 'No access' " +
                "if every other permission in the 'Repository Permissions' " +
                "section is set to 'No access'")
        select_metadata_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_metadata_read_only(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Metadata' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Merge queues' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_metadata_menu(driver, debug):
    """move to the 'Metadata' permissions menu"""
    if debug:
        printdebug("moving to the 'Metadata' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Metadata' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_metadata_menu(driver, debug):
    """open the 'Metadata' permissions menu"""
    if debug:
        printdebug("opening the 'Metadata' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Metadata' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_metadata_read_only(driver, debug):
    """select 'Read-only' in the 'Metadata' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Metadata' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Metadata' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_metadata_no_access(driver, debug):
    """select 'No access' in the 'Metadata' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Metadata' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
