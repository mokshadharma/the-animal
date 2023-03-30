# The Animal

automate GHES... like an animal

## IMPORTANT

This is an *experimental* project.  It is neither supported nor endorsed by GitHub.  Use it at your own risk.

## Purpose

[The Animal](https://github.com/mokshadharma/the-animal) is a command-line tool with which you can automate [GHES](https://docs.github.com/en/enterprise-server) through its web UI.

This can be useful when you can't do the same thing through its [API](https://docs.github.com/en/rest/overview/about-githubs-apis), or for testing.


## Features

- Create and return a classic [PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Create an [organization](https://docs.github.com/en/organizations)
- Create a [GitHub App](https://docs.github.com/en/developers/apps)

## Limitations

- Currently only works with [GHES](https://docs.github.com/en/enterprise-server)
- Currently does not work on [GHEC](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-enterprise-cloud)
- Currently does not work on [github.com](https://github.com)

## Requirements

- [Selenium Server](https://www.selenium.dev/)
- [Python](https://www.python.org/) 3.11.2
- Python packages listed in [requirements.txt](requirements.txt)

## Installation

    brew install selenium-server
    python3 -m venv venv
    . ./venv/bin/activate
    pip3 install -r requirements.txt


## Configuration

    cp etc/example.toml etc/my-ghes-test.toml
    vi etc/my-ghes-test.toml


## Usage

    Usage: animal [OPTIONS]

      automate GHES... like an animal

    Options:
      --config-file PATH              [required]
      --url URL                       Overrides config file
      --username USERNAME             Overrides config file
      --password PASSWORD             Overrides config file
      --debug
      --create [classic-pat|github-app|org]
      --help                          Show this message and exit.

## Examples


### Create a classic PAT

    ./animal --config-file etc/my-ghes-test.toml --create classic-pat


### Create a github-app

    ./animal --config-file etc/my-ghes-test.toml --create github-app


### Create an organization

    ./animal --config-file etc/my-ghes-test.toml --create org


### Create a classic PAT, with debugging turned on

    ./animal --config-file etc/my-ghes-test.toml --create classic-pat --debug


## Changelog

- 2022-02-26 - documentation improvements
- 2022-02-25 - documentation improvements
- 2022-02-25 - added: LICENSE.txt, SECURITY.md, SUPPORT.md, CODE_OF_CONDUCT.md
- 2022-02-23 - gracefully handling unexpected web pages
- 2022-02-23 - validating URLs before using them
- 2022-02-23 - gracefully erroring out when given incorrect username/password
- 2022-02-23 - added command line options: --url, --username, --password
- 2022-02-22 - documentation fixes
- 2022-02-21 - new option: --create org
- 2022-02-21 - renamed --get to --create
- 2022-02-20 - initial release


## Tested

### create classic-pat

| Python | GHES  |
|--------|-------|
| 3.11.2 | 3.7.6 |
| 3.11.2 | 3.8.0 |


### create org

| Python | GHES  |
|--------|-------|
| 3.11.2 | 3.7.6 |
| 3.11.2 | 3.8.0 |

### create app

| Python | GHES  |
|--------|-------|
| 3.11.2 | 3.8.0 |


## Contributions
We warmly welcome contributions to improve this project. Please see [CONTRIBUTING](CONTRIBUTING.md) for how to get involved.


## Support

If you need support using this project, have questions about it, or need to report security issues, please [open up an issue in this repository](https://github.com/mokshadharma/the-animal/issues).

*The Animal* is NOT supported by GitHub.


## License

This project is licensed under the terms of the MIT open source license. Please refer to [LICENSE](LICENSE.txt) for the full terms.


## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.


## Maintainers


[The Animal](https://github.com/mokshadharma/the-animal) is maintained by [@mokshadharma](https://github.com/mokshadharma)
