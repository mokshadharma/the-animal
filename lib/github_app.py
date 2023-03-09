"""github-app-related functions"""
# SPDX-FileCopyrightText: @mokshadharma
# SPDX-License-Identifier: MIT

# For generating random notes
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from .common import printdebug, printerr_exit, print_to_stderr, urlparse
from .login import login
from .selenium import setup_webdriver
from .permissions.repository.handlers import handle_repository_permissions
from .permissions.organization.handlers import handle_organization_permissions
from .permissions.account.handlers import handle_account_permissions
from .subscribe_to_events import subscribe_to_events


def allow_installation_on(config, driver, debug):
    """Handle 'Allow installation on' preference"""
    if debug:
        printdebug("handling 'Allow installation on' preference")
    preference = config['github_app']['allow_installation_on']
    if preference == 'Only on this account':
        id_value = "integration_public_false"
    elif preference == 'Any account':
        id_value = "integration_public_true"
    else:
        printerr_exit(
            f"Invalid 'Allow installation on' preference: '{preference}'")
    if debug:
        printdebug(f"allowing installation on: '{preference}'")
        printdebug('finding radio box to click on')
    radiobox = driver.find_element(By.ID, id_value)
    if debug:
        printdebug('clicking on radiobox')
        radiobox.click()


def click_add_callback_url_button(driver, debug):
    """click on the Add Callback URL button"""
    if debug:
        printdebug('finding the Add Callback URL button')
    xpath = "//button[contains(text(), 'Add Callback URL')]"
    add_callback_url_button = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug("clicking on the Add Callback URL button")
    add_callback_url_button.click()


def click_create_github_app(driver, debug):
    """click on the Create GitHub App button"""
    if debug:
        printdebug('finding the Create GitHub App button')
    xpath = "//input[@value='Create GitHub App']"
    create_github_app_button = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug("clicking on the Create GitHub App button")
    create_github_app_button.click()


def click_disable_ssl_verification(driver, debug):
    """click on the 'Disable' checkbox"""
    if debug:
        printdebug("disabling SSL verification")
        printdebug("finding the 'insecure_ssl_1' checkbox")
    ident = 'insecure_ssl_1'
    insecure_ssl_1 = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on the 'insecure_ssl_1' checkbox")

    # Note, we use ActionChains here because a simple .click()
    # errors out with an "Other element would receive the click" error
    action_chain = ActionChains(driver)
    action_chain.move_to_element(insecure_ssl_1).click().perform()


def click_disable_ssl_warning_button(driver, debug):
    """click the Disable SSL warning button"""
    class_name = 'btn.btn-block.btn-danger'
    if debug:
        printdebug("finding Disable SSL warning button")
    disable_ssl_warning_button = driver.find_element(By.CLASS_NAME, class_name)

    if debug:
        printdebug("clicking Disable SSL warning button")
    disable_ssl_warning_button.click()


def click_enable_ssl_verification(driver, debug):
    """click on the 'Enable SSL verification' checkbox"""
    if debug:
        printdebug("finding the 'insecure_ssl_0' checkbox")
    ident = 'insecure_ssl_0'
    insecure_ssl_0 = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on the 'insecure_ssl_0' checkbox")
    insecure_ssl_0.click()


def click_expire_user_auth_tokens(driver, debug):
    """click on the 'Expire user authorization tokens' checkbox"""
    if debug:
        printdebug("finding the 'Expire user authorization tokens' checkbox")
    ident = 'integration_user_token_expiration_enabled'
    add_callback_url_button = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on 'Expire user authorization tokens' checkbox")
    add_callback_url_button.click()


def click_redirect_on_update(driver, debug):
    """click on the 'Redirect on update' checkbox"""
    if debug:
        printdebug("finding 'Redirect on update' checkbox")
    ident = 'integration_setup_on_update'
    redirect_on_update_checkbox = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on 'Redirect on update' checkbox")
    redirect_on_update_checkbox.click()


def click_request_user_auth_checkbox(driver, debug):
    """click on the 'Request user authorization (OAuth) during installation'"""
    if debug:
        printdebug("finding 'Request user authorization' checkbox")
    ident = 'integration_request_oauth_on_install'
    request_user_auth_checkbox = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on 'Request user authorization' checkbox")
    request_user_auth_checkbox.click()


def click_webhook_active(driver, debug):
    """click on the Webhook 'Active' checkbox"""
    if debug:
        printdebug("finding Webhook 'Active' checkbox")
    ident = 'integration_hook_attributes_active'
    webhook_active_checkbox = driver.find_element(By.ID, ident)

    if debug:
        printdebug("clicking on Webhook 'Active' checkbox")
    webhook_active_checkbox.click()


def create_github_app(config, debug):
    """create a GitHub App"""
    driver = setup_webdriver(config, debug)
    login(config, driver, debug)
    navigate_to_register_new_github_app_page(config, driver, debug)
    handle_github_app_name(config, driver, debug)
    handle_github_app_description(config, driver, debug)
    handle_github_app_homepage(config, driver, debug)
    handle_callback_urls(config, driver, debug)
    handle_expire_user_auth_tokens(config, driver, debug)
    handle_request_oauth_on_install(config, driver, debug)
    handle_setup_url(config, driver, debug)
    handle_redirect_on_update(config, driver, debug)
    handle_webhook_active(config, driver, debug)
    handle_webhook_url(config, driver, debug)
    handle_webhook_secret(config, driver, debug)
    handle_enable_ssl_verification(config, driver, debug)
    handle_repository_permissions(config, driver, debug)
    handle_organization_permissions(config, driver, debug)
    handle_account_permissions(config, driver, debug)
    subscribe_to_events(config, driver, debug)
    allow_installation_on(config, driver, debug)
    click_create_github_app(driver, debug)

    if config['selenium']['pause_at_end']:
        print_to_stderr("Hit ENTER to quit")
        input()


def handle_callback_urls(config, driver, debug):
    """handle callback URLs"""
    callback_urls = config['github_app']['callback_urls']
    if len(callback_urls) > 0:
        url = callback_urls[0]
        i = 0
        wait_for_callback_url_field(i, driver, debug)
        type_callback_url(url, i, driver, debug)
        for i in range(1, len(callback_urls)):
            url = callback_urls[i]
            click_add_callback_url_button(driver, debug)
            wait_for_callback_url_field(i, driver, debug)
            type_callback_url(url, i, driver, debug)


def handle_enable_ssl_verification(config, driver, debug):
    """handle 'Enable SSL verification"""
    if config['github_app']['enable_ssl_verification']:
        wait_for_enable_ssl_verification(driver, debug)
        click_enable_ssl_verification(driver, debug)
    else:
        wait_for_disable_ssl_verification(driver, debug)
        click_disable_ssl_verification(driver, debug)
        wait_for_disable_ssl_warning_button(driver, debug)
        click_disable_ssl_warning_button(driver, debug)


def handle_expire_user_auth_tokens(config, driver, debug):
    """handle 'Expire user authorization tokens' checkbox"""
    if not config['github_app']['expire_user_auth_tokens']:
        click_expire_user_auth_tokens(driver, debug)


def handle_github_app_name(config, driver, debug):
    """handle GitHub App name"""
    wait_for_integration_name_field_to_appear(driver, debug)
    type_github_app_name_in_integration_name_field(config, driver, debug)


def handle_github_app_description(config, driver, debug):
    """handle GitHub App description"""
    wait_for_integrator_description_field_to_appear(driver, debug)
    type_github_app_description_in_integrator_description_field(
        config,
        driver,
        debug)


def handle_github_app_homepage(config, driver, debug):
    """handle GitHub App homepage"""
    wait_for_integration_url_field_to_appear(driver, debug)
    type_github_app_homepage_in_integration_url_field(config, driver, debug)


def handle_setup_url(config, driver, debug):
    """handle integration setup URL"""
    type_setup_url(config, driver, debug)


def handle_redirect_on_update(config, driver, debug):
    """handle 'Redirect on update' checkbox"""
    if config['github_app']['redirect_on_update']:
        click_redirect_on_update(driver, debug)


def handle_request_oauth_on_install(config, driver, debug):
    """handle 'Request user authorization (OAuth) during installation'"""
    if config['github_app']['request_oauth_during_install']:
        click_request_user_auth_checkbox(driver, debug)


def handle_webhook_active(config, driver, debug):
    """handle Webhook 'Active' checkbox"""
    if not config['github_app']['webhook_active']:
        click_webhook_active(driver, debug)


def handle_webhook_secret(config, driver, debug):
    """handle Webhook secrete"""
    type_webhook_secret(config, driver, debug)


def handle_webhook_url(config, driver, debug):
    """handle Webhook URL"""
    type_webhook_url(config, driver, debug)


def navigate_to_register_new_github_app_page(config, driver, debug):
    """navigate to the 'Register new GitHub App' page"""
    if debug:
        printdebug("extracting domain from GHES URL")
    domain = urlparse(config['server']['url']).netloc
    register_new_github_app_page = f"https://{domain}/settings/apps/new"
    if debug:
        printdebug("navigating to 'Register new GitHub App' page")
    driver.get(register_new_github_app_page)


# Note: This function uses a full xpath, which is fragile.
#       It should ideally be replaced by finding the field by ID,
#       but as of GHES 3.8.0 this will not work without indexing in to
#       the field, as the first two such fields have duplicate IDs
def type_callback_url(url, i, driver, debug):
    """type callback url"""
    # we increment i by 1, because the xpath is 1-indexed
    i = i + 1
    xpath = f"/html/body/div[4]/main/div/div/div/form/div[3]/dl[{i}]/dd/input"
    if debug:
        printdebug(f"finding {xpath} field")
    callback_url_field = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug(f"typing callback url in to {xpath} field")
    callback_url_field.send_keys(url)


def type_github_app_description_in_integrator_description_field(
        config,
        driver,
        debug):
    """type GitHub App description in integrator_description field"""
    if debug:
        printdebug('finding integrator_description field')
    integrator_description = driver.find_element(
        By.ID,
        'integrator_description')

    if config['github_app']['description'] == ">>>RANDOM<<<":
        if debug:
            printdebug('generating random GitHub App description')
        github_app_description = "the animal app " + str(uuid.uuid4())
    else:
        if debug:
            printdebug('using GitHub App description in config file')
        github_app_description = config['github_app']['description']

    if debug:
        printdebug('typing GitHub App description')
    integrator_description.send_keys(github_app_description)


def type_github_app_homepage_in_integration_url_field(
        config,
        driver,
        debug):
    """type GitHub App homepage in integration_url field"""
    if debug:
        printdebug('finding integration_url field')
    integration_url = driver.find_element(
        By.ID,
        'integration_url')

    github_app_url = config['github_app']['homepage']

    if debug:
        printdebug('typing GitHub App homepage in to integration_url field')
    integration_url.send_keys(github_app_url)


def type_webhook_url(config, driver, debug):
    """type Webhook URL"""
    if debug:
        printdebug('finding integration_hook_attributes_url field')
    ident = 'integration_hook_attributes_url'
    integration_hook_attributes_url_field = driver.find_element(By.ID, ident)

    webhook_url = config['github_app']['webhook_url']

    if debug:
        printdebug('typing webhook URL')
    integration_hook_attributes_url_field.send_keys(webhook_url)


def type_github_app_name_in_integration_name_field(config, driver, debug):
    """type GitHub App name in integration_name field"""
    if debug:
        printdebug('finding integration_name field')
    integration_name = driver.find_element(
        By.ID,
        'integration_name')

    if config['github_app']['name'] == ">>>RANDOM<<<":
        if debug:
            printdebug('generating random GitHub App name')
        github_app_name = "the animal app " + str(uuid.uuid4())
        # Note: App name is not allowed to be longer than 34 characters
        #       so we'll truncate the random name
        github_app_name = github_app_name[0:33]
    else:
        if debug:
            printdebug('using GitHub App name in config file')
        github_app_name = config['github_app']['name']

    if debug:
        printdebug('typing GitHub App name in to integration_name field')
    integration_name.send_keys(github_app_name)


def type_setup_url(config, driver, debug):
    """type setup URL"""
    if debug:
        printdebug('finding integration_setup_url field')
    integration_setup_url_field = driver.find_element(
        By.ID,
        'integration_setup_url')

    setup_url = config['github_app']['setup_url']

    if debug:
        printdebug('typing integration setup URL')
    integration_setup_url_field.send_keys(setup_url)


def type_webhook_secret(config, driver, debug):
    """type Webhook secret"""
    if debug:
        printdebug('finding integration_hook_attributes_secret field')
    ident = 'integration_hook_attributes_secret'
    integration_hook_attributes_secret = driver.find_element(By.ID, ident)

    webhook_secret = config['github_app']['webhook_secret']

    if debug:
        printdebug('typing webhook secret')
    integration_hook_attributes_secret.send_keys(webhook_secret)


# NOTE: The following function does not work on GHES 3.8.0 because
#       the first callback url field's id is:
#
#          integration_application_callback_urls_attributes_0_url
#
#       the second is:
#
#          integration_application_callback_urls_attributes_0_url
#
#       the third is:
#
#          integration_application_callback_urls_attributes_1_url
#
#       the fourth is:
#
#          integration_application_callback_urls_attributes_2_url
#
#       etc...
#
#       This smells like a bug, and because of it we
#       are forced to either use a full xpath, or index
#       in to:
#
# def wait_for_callback_url_field(i, driver, debug):
#     """wait for the callback url field to appear on the page"""
#     ident =  f"integration_application_callback_urls_attributes_{i}_url"
#     if debug:
#         printdebug(f"waiting for {id} field to appear on the page")
#     wait = WebDriverWait(driver, 10)
#     wait.until(ec.visibility_of_element_located((By.ID,
#                                                  ident)))


# Note: This function uses a full xpath, which is fragile.
#       It should ideally be replaced by finding the field by ID,
#       but as of GHES 3.8.0 this will not work without indexing in to
#       the field, as the first two such fields have duplicate IDs
def wait_for_callback_url_field(i, driver, debug):
    """wait for the callback url field to appear on the page"""
    # we increment i by 1, because the xpath is 1-indexed
    i = i + 1
    xpath = f"/html/body/div[4]/main/div/div/div/form/div[3]/dl[{i}]/dd/input"
    if debug:
        printdebug(f"waiting for {xpath} field to appear on the page")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def wait_for_disable_ssl_verification(driver, debug):
    """wait for the 'Disable' radio box to be interactable"""
    if debug:
        printdebug("waiting for 'Disable' radio box")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.ID, 'insecure_ssl_1')))


def wait_for_disable_ssl_warning_button(driver, debug):
    """wait for the Disable SSL warning button"""
    if debug:
        printdebug("waiting for Disable SSL warning button")
    wait = WebDriverWait(driver, 10)
    button_text = 'Disable, I understand my webhooks may not be secure'
    xpath = f"//div[contains(., '{button_text}')]"
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def wait_for_enable_ssl_verification(driver, debug):
    """wait for the 'Enable SSL verification' radio box to be interactable"""
    if debug:
        printdebug("waiting for 'Enable SSL verification' radio box")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, 'insecure_ssl_0')))


def wait_for_integrator_description_field_to_appear(driver, debug):
    """wait for the integrator_description field to appear on the page"""
    if debug:
        printdebug('waiting for integrator_description field ' +
                   'to appear on the page')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID,
                                                 'integrator_description')))


def wait_for_integration_name_field_to_appear(driver, debug):
    """wait for the integration_name field to appear on the page"""
    if debug:
        printdebug("waiting for integration_name field to appear on the page")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, 'integration_name')))


def wait_for_integration_url_field_to_appear(driver, debug):
    """wait for the integration_url field to appear on the page"""
    if debug:
        printdebug("waiting for integration_url field to appear on the page")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, 'integration_url')))
