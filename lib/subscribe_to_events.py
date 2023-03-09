"""Subscribe to events"""

from selenium.webdriver.common.by import By

from .common import printdebug


def subscribe_to_events(config, driver, debug):
    """Subscribe to events"""
    if debug:
        printdebug('subscribing to events')
    events = config['github_app']['subscribe_to_events']

    for event, subscribe in events.items():
        handle_subscription(event, subscribe, driver, debug)


def handle_subscription(event, subscribe, driver, debug):
    """Handle subscription to event"""
    if subscribe:
        if debug:
            printdebug(f"subscribing to: '{event}'")
            printdebug('finding event checkbox')
        xpath = f"//input[@type='checkbox' and @value='{event}']"
        checkbox = driver.find_element(By.XPATH, xpath)
        if not checkbox.is_selected():
            if debug:
                printdebug('event checkbox is NOT already checked')
                printdebug('clicking on event checkbox')
            checkbox.click()
        else:
            if debug:
                printdebug('event checkbox IS already checked')
                printdebug('doing nothing')
    else:
        printdebug(f"NOT subscribing to: '{event}'")
