"""login-related functions"""
# SPDX-FileCopyrightText: @mokshadharma
# SPDX-License-Identifier: MIT

# For regular expressions
import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from lib.validate_config import validate_login_page
from .common import printdebug, printerr_exit


def get_version(driver, debug):
    """get the version of GHES running on this instance"""
    if debug:
        printdebug("finding GHES version element")
    version_element = driver.find_element(By.CLASS_NAME, 'current-branch-name')
    if debug:
        printdebug("getting GHES version element content")
    raw_version = version_element.get_attribute('innerHTML')
    result = re.match(r'.*Version (?P<version>.*)\n', raw_version, re.DOTALL)
    version = result.group('version')
    return version


def handle_incorrect_username_or_password(driver, debug):
    """handle incorrect username or password"""
    if debug:
        msg = "waiting for potential 'Incorrect username or password' error"
        printdebug(msg)
    wait = WebDriverWait(driver, 1)
    xpath = "//div[contains(., 'Incorrect username')]"
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        return
    printerr_exit('Incorrect username or password')


def login(config, driver, debug):
    """login to a GHES instance"""
    login_page = config['server']['url']
    if debug:
        printdebug(f"opening login page '{login_page}'")
    driver.get(login_page)
    validate_login_page(driver, debug)
    type_username_on_login_page(config, driver, debug)
    type_password_on_login_page(config, driver, debug)
    submit_login_form_on_login_page(driver, debug)
    handle_incorrect_username_or_password(driver, debug)
    wait_for_version_number_to_appear(driver, debug)
    version = get_version(driver, debug)
    if debug:
        printdebug(f"detected GHES version: '{version}'")


def submit_login_form_on_login_page(driver, debug):
    """submits the login form on the login page"""
    if debug:
        printdebug("finding 'commit' (the 'Sign in' button) on login page")
    sign_in_button = driver.find_element(By.NAME, 'commit')
    if debug:
        printdebug("submitting login form on login page")
    sign_in_button.submit()


def type_password_on_login_page(config, driver, debug):
    """type the password in to the password field on the login page"""
    if debug:
        printdebug("finding password field on login page")
    password_field = driver.find_element(By.ID, 'password')

    if debug:
        printdebug("typing password in to password field on login page")
    password_field.send_keys(config['server']['password'])


def type_username_on_login_page(config, driver, debug):
    """type the username in to the username field on the login page"""
    if debug:
        printdebug("finding login_field id on login page")
    login_field = driver.find_element(By.ID, 'login_field')

    if debug:
        printdebug("typing username in to login_field on login page")
    login_field.send_keys(config['server']['username'])


def wait_for_version_number_to_appear(driver, debug):
    """wait for the GHES version number to appear on the page"""
    if debug:
        printdebug("waiting for GHES version number to appear on the page")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME,
                                                 'current-branch-name')))
