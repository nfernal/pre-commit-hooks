# Check commit message format

 The function of this program defines a regular expression pattern and checks if the commit message provided in the argument matches the pattern. If it does not match, an exception is raised with a message explaining the format of the commit message.

## The regular expression pattern

is defined as

`r'(feat|fix|improvement|docs|refactor|test|ci|chore)(\([\w\-]+\))?:\s.*'`

 and is used to match the commit message. The pattern matches one of the accepted prefixes:

* feat
* fix
* improvement
* docs
* refactor
* test
* ci
* chore

 followed by an optional argument `(\([\w\-]+\))` which is expected to be the commit message.

## The exception_message function
is called when the commit message does not match the pattern. This function returns a message explaining the format of the commit message and provides a list of allowed prefixes.

> The exception_message function is used to provide a message explaining the format of the commit message and a list of allowed prefixes. This message is returned when the commit message provided does not match the regular expression pattern defined in the `main()` function.

The message is formatted using escape characters to provide *color* and *bolding*. The message consists of two parts:

A header explaining that the commit message must follow the expected format

`<type prefix>: <commit message>`

and a list of allowed prefixes with a short explanation of each.
The list of allowed prefixes is:

- chore: Repository management
- ci: Updates to continuous integration
- docs: Updating repository and code documenation
- feat: Introducing new features
- fix: Fixing bugs within the code base
improvement: Improving performance or simplifying existing features
- refactor: Rewriting code without changing business objectives/functionality
- test: Updating test files and configurations
