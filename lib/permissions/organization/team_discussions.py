"""functions related to 'Team_Discussions' organization permissions"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from ...common import printerr_exit, printdebug


def handle_team_discussions(permissions, driver, debug):
    """handle Team_Discussions permissions"""
    move_to_the_team_discussions_menu(driver, debug)
    open_team_discussions_menu(driver, debug)
    if debug:
        printdebug(
            "determining which permissions to give to 'Team_Discussions'")
    if permissions == 'No access':
        if debug:
            printdebug("Desired permissions: 'No access'")
        select_team_discussions_no_access(driver, debug)
    elif permissions == 'Read-only':
        if debug:
            printdebug("Desired permissions: 'Read-only'")
        select_team_discussions_read_only(driver, debug)
    elif permissions == 'Read and write':
        if debug:
            printdebug("Desired permissions: 'Read and write'")
        select_team_discussions_read_and_write(driver, debug)
    else:
        printerr_exit(
            f"Unexpected 'Team_Discussions' permissions: '{permissions}'")


# Note: This function assumes the active element is
#       the 'Self-hosted runners' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def move_to_the_team_discussions_menu(driver, debug):
    """move to the 'Team_Discussions' permissions menu"""
    if debug:
        printdebug("moving to the 'Team_Discussions' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()


# Note: This function assumes the active element is
#       the 'Team_Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def open_team_discussions_menu(driver, debug):
    """open the 'Team_Discussions' permissions menu"""
    if debug:
        printdebug("opening the 'Team_Discussions' permissions menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()


# Note: This function relies on the active element being
#       the 'Team_Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_team_discussions_no_access(driver, debug):
    """select 'No access' in the 'Team_Discussions' menu"""
    if debug:
        printdebug("selecting 'No access' in the 'Team_Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function assumes the active element is
#       the 'Team_Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_team_discussions_read_only(driver, debug):
    """select 'Read-only' in the 'Team_Discussions' menu"""
    if debug:
        printdebug("selecting 'Read-only' in the 'Team_Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()


# Note: This function relies on the active element being
#       the 'Team_Discussions' drop down menu
#
#       If the active element is anything else, this function may
#       produce unpredictable results
def select_team_discussions_read_and_write(driver, debug):
    """select 'Read and write' in the 'Team_Discussions' menu"""
    if debug:
        printdebug(
            "selecting 'Read and write' in the 'Team_Discussions' menu")
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
