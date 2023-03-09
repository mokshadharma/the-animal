"""configuration-related functions"""
# SPDX-FileCopyrightText: @mokshadharma
# SPDX-License-Identifier: MIT

# TOML-format configuration files
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from .common import printdebug


def get_config(config_file, debug):
    """Get options from configuration file"""
    if debug:
        printdebug(f"reading config file '{config_file}'")
    with open(config_file, mode="rb") as opened_config_file:
        config = tomllib.load(opened_config_file)
    return config


def override_config(config, url, username, password, debug):
    """Override some options in the config file"""
    if url:
        if debug:
            msg = 'overriding url in config file ' \
                'with one passed on the command line'
            printdebug(msg)
        config['server']['url'] = url
    if username:
        if debug:
            msg = 'overriding username in config file ' \
                'with one passed on the command line'
            printdebug(msg)
        config['server']['username'] = username
    if password:
        if debug:
            msg = 'overriding password in config file ' \
                'with one passed on the command line'
            printdebug(msg)
        config['server']['password'] = password
    return config
