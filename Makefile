# SPDX-FileCopyrightText: @mokshadharma
# SPDX-License-Identifier: MIT

# Some magic for make to see the exit value of a command who's output is piped
SHELL = bash
.SHELLFLAGS = -o pipefail -c


FLAKE8='flake8'
BEHAVE='behave'
PYLINT=pylint

LIB_DIR=lib
SOURCE=animal
SOURCE+=$(LIB_DIR)/classic_pat.py
SOURCE+=$(LIB_DIR)/common.py
SOURCE+=$(LIB_DIR)/config.py
SOURCE+=$(LIB_DIR)/github_app.py
SOURCE+=$(LIB_DIR)/login.py
SOURCE+=$(LIB_DIR)/org.py
SOURCE+=$(LIB_DIR)/permissions/repository/actions.py
SOURCE+=$(LIB_DIR)/permissions/repository/administration.py
SOURCE+=$(LIB_DIR)/permissions/repository/checks.py
SOURCE+=$(LIB_DIR)/permissions/repository/code_scanning_alerts.py
SOURCE+=$(LIB_DIR)/permissions/repository/codespaces.py
SOURCE+=$(LIB_DIR)/permissions/repository/codespaces_lifecycle_admin.py
SOURCE+=$(LIB_DIR)/permissions/repository/codespaces_metadata.py
SOURCE+=$(LIB_DIR)/permissions/repository/codespaces_secrets.py
SOURCE+=$(LIB_DIR)/permissions/repository/commit_statuses.py
SOURCE+=$(LIB_DIR)/permissions/repository/contents.py
SOURCE+=$(LIB_DIR)/permissions/repository/dependabot_alerts.py
SOURCE+=$(LIB_DIR)/permissions/repository/dependabot_secrets.py
SOURCE+=$(LIB_DIR)/permissions/repository/deployments.py
SOURCE+=$(LIB_DIR)/permissions/repository/discussions.py
SOURCE+=$(LIB_DIR)/permissions/repository/environments.py
SOURCE+=$(LIB_DIR)/permissions/repository/issues.py
SOURCE+=$(LIB_DIR)/permissions/repository/merge_queues.py
SOURCE+=$(LIB_DIR)/permissions/repository/metadata.py
SOURCE+=$(LIB_DIR)/permissions/repository/packages.py
SOURCE+=$(LIB_DIR)/permissions/repository/pages.py
SOURCE+=$(LIB_DIR)/permissions/repository/pre_receive_hooks.py
SOURCE+=$(LIB_DIR)/permissions/repository/projects.py
SOURCE+=$(LIB_DIR)/permissions/repository/pull_requests.py
SOURCE+=$(LIB_DIR)/permissions/repository/secret_scanning_alerts.py
SOURCE+=$(LIB_DIR)/permissions/repository/secrets.py
SOURCE+=$(LIB_DIR)/permissions/repository/single_file.py
SOURCE+=$(LIB_DIR)/permissions/repository/webhooks.py
SOURCE+=$(LIB_DIR)/permissions/repository/workflows.py
SOURCE+=$(LIB_DIR)/permissions/repository/handlers.py
SOURCE+=$(LIB_DIR)/permissions/repository/variables.py
SOURCE+=$(LIB_DIR)/permissions/organization/handlers.py
SOURCE+=$(LIB_DIR)/permissions/organization/administration.py
SOURCE+=$(LIB_DIR)/permissions/organization/blocking_users.py
SOURCE+=$(LIB_DIR)/permissions/organization/events.py
SOURCE+=$(LIB_DIR)/permissions/organization/members.py
SOURCE+=$(LIB_DIR)/permissions/organization/organization_codespaces.py
SOURCE+=$(LIB_DIR)/permissions/organization/organization_codespaces_settings.py
SOURCE+=$(LIB_DIR)/permissions/organization/organization_dependabot_secrets.py
SOURCE+=$(LIB_DIR)/permissions/organization/plan.py
SOURCE+=$(LIB_DIR)/permissions/organization/pre_receive_hooks.py
SOURCE+=$(LIB_DIR)/permissions/organization/projects.py
SOURCE+=$(LIB_DIR)/permissions/organization/secrets.py
SOURCE+=$(LIB_DIR)/permissions/organization/self_hosted_runners.py
SOURCE+=$(LIB_DIR)/permissions/organization/team_discussions.py
SOURCE+=$(LIB_DIR)/permissions/organization/variables.py
SOURCE+=$(LIB_DIR)/permissions/organization/webhooks.py
SOURCE+=$(LIB_DIR)/permissions/account/handlers.py
SOURCE+=$(LIB_DIR)/permissions/account/block_another_user.py
SOURCE+=$(LIB_DIR)/permissions/account/codespaces_user_secrets.py
SOURCE+=$(LIB_DIR)/permissions/account/email_addresses.py
SOURCE+=$(LIB_DIR)/permissions/account/followers.py
SOURCE+=$(LIB_DIR)/permissions/account/gpg_keys.py
SOURCE+=$(LIB_DIR)/permissions/account/gists.py
SOURCE+=$(LIB_DIR)/permissions/account/git_ssh_keys.py
SOURCE+=$(LIB_DIR)/permissions/account/interaction_limits.py
SOURCE+=$(LIB_DIR)/permissions/account/plan.py
SOURCE+=$(LIB_DIR)/permissions/account/profile.py
SOURCE+=$(LIB_DIR)/permissions/account/ssh_signing_keys.py
SOURCE+=$(LIB_DIR)/permissions/account/starring.py
SOURCE+=$(LIB_DIR)/permissions/account/watching.py
SOURCE+=$(LIB_DIR)/subscribe_to_events.py
SOURCE+=$(LIB_DIR)/selenium.py
SOURCE+=$(LIB_DIR)/validate_config.py

PYLINT_OPTS=--disable=similarities

.PHONY: test

all: test

flake8: $(SOURCE)
	$(FLAKE8) --show-source $(SOURCE)

pylint: $(SOURCE)
	$(PYLINT) $(PYLINT_OPTS) $(SOURCE)

test: pylint flake8

#test: pylint flake8
#	cd test && make

