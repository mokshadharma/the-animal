"""functions related to account permissions in GitHub Apps"""

from selenium.webdriver.common.by import By

from ...common import printdebug
from .block_another_user import \
    handle_block_another_user
from .codespaces_user_secrets import \
    handle_codespaces_user_secrets
from .email_addresses import handle_email_addresses
from .followers import handle_followers
from .gpg_keys import handle_gpg_keys
from .gists import handle_gists
from .git_ssh_keys import handle_git_ssh_keys
from .interaction_limits import handle_interaction_limits
from .plan import handle_plan
from .profile import handle_profile
from .ssh_signing_keys import handle_ssh_signing_keys
from .starring import handle_starring
from .watching import handle_watching


def click_account_permissions_section(driver, debug):
    """click on the Account Permissions section"""
    if debug:
        printdebug('finding the Account Permissions section')
    xpath = "//h4[text()='Account permissions']"
    account_permissions_section = driver.find_element(By.XPATH, xpath)

    if debug:
        printdebug("clicking on the Account Permissions section")
    account_permissions_section.click()


def handle_account_permissions(config, driver, debug):
    """handle Account Permissions"""
    perms = config['github_app']['account_permissions']
    # Only open the Account Pemissions section if there are
    # any non-default permissions (default permissions are "No access")
    if any(v != 'No access' for v in perms.values()):
        # There's a value in perms that's not "No access"
        #
        # Note: The functions of the following handlers are order-dependent
        #       Changing their order may lead to unexpected results
        click_account_permissions_section(driver, debug)
        handle_block_another_user(
            perms['block_another_user'], driver, debug)
        handle_codespaces_user_secrets(
            perms['codespaces_user_secrets'], driver, debug)
        handle_email_addresses(perms['email_addresses'], driver, debug)
        handle_followers(perms['followers'], driver, debug)
        handle_gpg_keys(perms['gpg_keys'], driver, debug)
        handle_gists(perms['gists'], driver, debug)
        handle_git_ssh_keys(perms['git_ssh_keys'], driver, debug)
        handle_interaction_limits(perms['interaction_limits'], driver, debug)
        handle_plan(perms['plan'], driver, debug)
        handle_profile(perms['profile'], driver, debug)
        handle_ssh_signing_keys(perms['ssh_signing_keys'], driver, debug)
        handle_starring(perms['starring'], driver, debug)
        handle_watching(perms['watching'], driver, debug)
