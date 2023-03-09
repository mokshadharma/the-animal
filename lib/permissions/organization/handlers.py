"""functions related to organization permissions in GitHub Apps"""

from selenium.webdriver.common.by import By

from ...common import printdebug
from .administration import handle_administration
from .blocking_users import handle_blocking_users
from .events import handle_events
from .members import handle_members
from .organization_codespaces import handle_organization_codespaces
from .organization_codespaces_settings import \
    handle_organization_codespaces_settings
from .organization_dependabot_secrets import \
    handle_organization_dependabot_secrets
from .plan import handle_plan
from .pre_receive_hooks import handle_pre_receive_hooks
from .projects import handle_projects
from .secrets import handle_secrets
from .self_hosted_runners import handle_self_hosted_runners
from .team_discussions import handle_team_discussions
from .variables import handle_variables
from .webhooks import handle_webhooks


def click_organization_permissions_section(driver, debug):
    """click on the Organization Permissions section"""
    if debug:
        printdebug('finding the Organization Permissions section')
    xpath = "//h4[text()='Organization permissions']"
    organization_permissions_section = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug("clicking on the Organization Permissions section")
    organization_permissions_section.click()


def handle_organization_permissions(config, driver, debug):
    """handle Organization Permissions"""
    perms = config['github_app']['organization_permissions']
    # Only open the Organization Pemissions section if there are
    # any non-default permissions (default permissions are "No access")
    if any(v != 'No access' for v in perms.values()):
        # There's a value in perms that's not "No access"
        #
        # Note: The functions of the following handlers are order-dependent
        #       Changing their order may lead to unexpected results
        click_organization_permissions_section(driver, debug)
        handle_administration(perms['administration'], driver, debug)
        handle_blocking_users(perms['blocking_users'], driver, debug)
        handle_events(perms['events'], driver, debug)
        handle_members(perms['members'], driver, debug)
        handle_organization_codespaces(
            perms['organization_codespaces'], driver, debug)
        handle_organization_codespaces_settings(
            perms['organization_codespaces_settings'], driver, debug)
        handle_organization_dependabot_secrets(
            perms['organization_dependabot_secrets'], driver, debug)
        handle_plan(perms['plan'], driver, debug)
        handle_pre_receive_hooks(perms['pre_receive_hooks'], driver, debug)
        handle_projects(perms['projects'], driver, debug)
        handle_secrets(perms['secrets'], driver, debug)
        handle_self_hosted_runners(perms['self_hosted_runners'], driver, debug)
        handle_team_discussions(perms['team_discussions'], driver, debug)
        handle_variables(perms['variables'], driver, debug)
        handle_webhooks(perms['webhooks'], driver, debug)
