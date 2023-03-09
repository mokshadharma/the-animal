"""functions used in many other places in the program"""
# SPDX-FileCopyrightText: @mokshadharma
# SPDX-License-Identifier: MIT

# For sys.stderr.write()
import sys

# For os.path.basename(__file__)
import os

# For DNS lookups
import socket

# For extracting domain names from URLs
from urllib.parse import urlparse

# For validating URLs
import validators

# The name of this script (to be used for reporting errors in printerr() below)
this_file = os.path.basename(sys.argv[0])


def lookup_domain_in_dns(config, debug):
    """look up GHES domain from URL in config file in DNS"""
    if debug:
        printdebug("extracting domain from GHES URL")
    domain = urlparse(config['server']['url']).netloc
    if debug:
        printdebug(f"performing a DNS lookup on '{domain}'")
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        printerr_exit(f"no such domain: '{domain}'")


def printdebug(*args, **kwargs):
    """print given args to STDERR,
    prefixed with the name of this program and 'DEBUG:' """
    print_to_stderr(this_file + ": DEBUG: ", *args, **kwargs)


def printerr(*args, **kwargs):
    """print given args to STDERR,
    prefixed with the name of this program and 'Error:' """
    print_to_stderr(this_file + ": Error: ", *args, **kwargs)


def printerr_exit(*args, **kwargs):
    """print given arguments to STDERR and exit with an error code of 1"""
    printerr(*args, **kwargs)
    sys.exit(1)


def print_to_stderr(*args, **kwargs):
    """print given arguments to STDERR"""
    print(*args, file=sys.stderr, **kwargs)


def validate_url(url):
    """make sure the given url is valid"""
    if validators.url(url):
        return
    printerr_exit(f"Invalid URL '{url}'")
