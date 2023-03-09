"""functions related to 'Single_File' repository permissions in GitHub Apps"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_single_file(perms, driver, debug):  # pylint: disable=R0912
    """handle Single_File permissions"""
    permissions = perms['single_file']
    move_to_the_single_file_menu(driver, debug)
    open_single_file_menu(driver, debug)
    if debug:
        printdebug("determining which permissions to give to 'Single_File'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_single_file_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_single_file_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_single_file_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Single_File' permissions: '{permissions}'")

    if permissions == 'No access':
        if debug:
            printdebug("Nothing left to do for 'No access'")
        return
    single_file_paths = perms['single_file_paths']
    move_to_the_paths_field(driver, debug)
    for path in single_file_paths:
        if path == "":
            printerr_exit("At least one file path required")
        type_path(path, driver, debug)
    move_to_the_add_button(driver, debug)
    for _ in single_file_paths:
        move_to_the_x_button(driver, debug)


# Note: This function assumes the active element is
#       the 'Path' field
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_add_button(driver, debug):
    """move to the 'Add' button"""
    if debug:
        printdebug("moving to the 'Add' button")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Add' button
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_x_button(driver, debug):
    """move to the 'Add' button"""
    if debug:
        printdebug("moving to the 'x' button")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Secrets' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_single_file_menu(driver, debug):
    """move to the 'Single_File' permissions menu"""
    if debug:
        printdebug("moving to the 'Single_File' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Single file' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_paths_field(driver, debug):
    """move to the 'Paths' field"""
    if debug:
        printdebug("moving to the 'Paths' field")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Single_File' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_single_file_menu(driver, debug):
    """open the 'Single_File' permissions menu"""
    if debug:
        printdebug("opening the 'Single_File' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function assumes the active element is
#       the 'Add' button
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def press_the_add_button(driver, debug):
    """press the 'Add' button"""
    if debug:
        printdebug("pressing the 'Add' button")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Single_File' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_single_file_read_only(driver, debug):
    """select 'Read-only' in the 'Single_File' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Single_File' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Single_File' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_single_file_read_and_write(driver, debug):
    """select 'Read and write' in the 'Single_File' menu"""
    if debug:
        printdebug("selecting 'Read and write' in the 'Single_File' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Single_File' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_single_file_no_access(driver, debug):
    """select 'No access' in the 'Single_File' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Single_File' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


def type_path(path, driver, debug):
    """type the given path"""
    if debug:
        printdebug("typing the path")
    action = ActionChains(driver)
    action.send_keys(path).send_keys(Keys.RETURN).perform()
