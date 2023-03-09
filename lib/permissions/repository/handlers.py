"""functions related to repository permissions in GitHub Apps"""

from selenium.webdriver.common.by import By

from ...common import printdebug
from .actions import handle_actions
from .administration import handle_administration
from .checks import handle_checks
from .code_scanning_alerts import handle_code_scanning_alerts
from .codespaces import handle_codespaces
from .codespaces_lifecycle_admin import handle_codespaces_lifecycle_admin
from .codespaces_metadata import handle_codespaces_metadata
from .codespaces_secrets import handle_codespaces_secrets
from .commit_statuses import handle_commit_statuses
from .contents import handle_contents
from .dependabot_alerts import handle_dependabot_alerts
from .dependabot_secrets import handle_dependabot_secrets
from .deployments import handle_deployments
from .discussions import handle_discussions
from .environments import handle_environments
from .issues import handle_issues
from .merge_queues import handle_merge_queues
from .metadata import handle_metadata
from .packages import handle_packages
from .pages import handle_pages
from .pre_receive_hooks import handle_pre_receive_hooks
from .projects import handle_projects
from .pull_requests import handle_pull_requests
from .secret_scanning_alerts import handle_secret_scanning_alerts
from .secrets import handle_secrets
from .single_file import handle_single_file
from .variables import handle_variables
from .webhooks import handle_webhooks
from .workflows import handle_workflows


def click_repository_permissions_section(driver, debug):
    """click on the Repository Permissions section"""
    if debug:
        printdebug('finding the Repository Permissions section')
    xpath = "//h4[text()='Repository permissions']"
    repository_permissions_section = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug("clicking on the Repository Permissions section")
    repository_permissions_section.click()


def handle_repository_permissions(config, driver, debug):
    """handle Repository Permissions"""
    perms = config['github_app']['repository_permissions']
    # Only open the Repository Pemissions section if there are
    # any non-default permissions (default permissions are "No access")
    if any(v != 'No access' for v in perms.values()):
        # There's a value in perms that's not "No access"
        #
        # Note: The functions of the following handlers are order-dependent
        #       Changing their order may lead to unexpected results
        click_repository_permissions_section(driver, debug)
        handle_actions(perms['actions'], driver, debug)
        handle_administration(perms['administration'], driver, debug)
        handle_checks(perms['checks'], driver, debug)
        handle_code_scanning_alerts(
            perms['code_scanning_alerts'], driver, debug)
        handle_codespaces(perms['checks'], driver, debug)
        handle_codespaces_lifecycle_admin(
            perms['codespaces_lifecycle_admin'],
            driver,
            debug)
        handle_codespaces_metadata(perms['codespaces_metadata'], driver, debug)
        handle_codespaces_secrets(perms['codespaces_secrets'], driver, debug)
        handle_commit_statuses(perms['commit_statuses'], driver, debug)
        handle_contents(perms['contents'], driver, debug)
        handle_dependabot_alerts(perms['dependabot_alerts'], driver, debug)
        handle_dependabot_secrets(perms['dependabot_secrets'], driver, debug)
        handle_deployments(perms['deployments'], driver, debug)
        handle_discussions(perms['discussions'], driver, debug)
        handle_environments(perms['environments'], driver, debug)
        handle_issues(perms['issues'], driver, debug)
        handle_merge_queues(perms['merge_queues'], driver, debug)
        handle_metadata(perms, driver, debug)
        handle_packages(perms['packages'], driver, debug)
        handle_pages(perms['pages'], driver, debug)
        handle_pre_receive_hooks(perms['pre_receive_hooks'], driver, debug)
        handle_projects(perms['projects'], driver, debug)
        handle_pull_requests(perms['pull_requests'], driver, debug)
        handle_secret_scanning_alerts(
            perms['secret_scanning_alerts'],
            driver,
            debug)
        handle_secrets(perms['secrets'], driver, debug)
        handle_single_file(perms, driver, debug)
        handle_variables(perms['variables'], driver, debug)
        handle_webhooks(perms['webhooks'], driver, debug)
        handle_workflows(perms['workflows'], driver, debug)
