#!/usr/bin/env python
from __future__ import annotations

import re
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def exception_message() -> str:
    exception_message = f'\n{bcolors.BOLD}{bcolors.FAIL}!!! Commit messages must follow the format  <type prefix>: <commit message>.\n'  # noqa: E501
    additional_info_header = f'\n{bcolors.OKCYAN}Allowed prefixes:\n'
    additional_info_msg = f"""{bcolors.OKCYAN}
        chore: Repository management
        ci: Updates to continuous integration
        docs: Updating repository and code documenation
    **  feat: Introducing new features
    **  fix: Fixing bugs within the code base
    **  improvement: Improving performance or simplifying existing features
    **  refactor: Rewriting code without changing business objectives/functionality
        test: Updating test files and configurations
        ** denotes that the prefix will trigger a new release version

    """  # noqa: E501

    return sys.argv[1] + exception_message + additional_info_header + additional_info_msg


def main() -> None:
    # example:
    # feat: added the ability to add api key to configuration
    sys.tracebacklimit = 0
    pattern = r'(feat|fix|improvement|docs|refactor|test|ci|chore)(\([\w\-]+\))?:\s.*'  # noqa: E501
    filename = sys.argv[1]
    ss = open(filename).read()
    m = re.match(pattern, ss)
    if m is None:
        raise Exception(exception_message())


if __name__ == '__main__':
    main()
