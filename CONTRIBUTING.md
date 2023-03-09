## Contributing

[fork]: https://github.com/mokshadharma/the-animal/fork
[pr]: https://github.com/mokshadharma/the-animal/compare
[style]: https://github.com/mokshadharma/the-animal/blob/main/.golangci.yaml
[code-of-conduct]: CODE_OF_CONDUCT.md

Hi there! We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great.

Contributions to this project are released to the public under the [project's open source license](LICENSE.txt).

Please note that this project is released with a [Contributor Code of Conduct][code-of-conduct]. By participating in this project you agree to abide by its terms.

## Prerequisites for running and testing code

These are one time installations required to be able to test your changes locally as part of the pull request (PR) submission process.

On MacOS:

1. [Install homebrew](https://brew.sh/)
1. `brew install selenium-server`

## Submitting a pull request

1. [Fork][fork] and clone the repository
1. `python3 -m venv venv`
1. `. ./venv/bin/activate`
1. `pip3 install -r requirements.txt`
1. `make test`
1. Ensure that all test pass
1. Create a new branch: `git checkout -b my-branch-name`
1. Make your change, add tests, and make sure the tests and linter still pass
1. Push to your fork and [submit a pull request][pr]
1. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Follow the [style guide](https://peps.python.org/pep-0008/).
- Write tests.
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)
