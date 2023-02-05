# pre-commit-hooks
Some opinionated hooks for pre-commit


[![build status](https://github.com/nfernal/pre-commit-hooks/actions/workflows/main.yml/badge.svg)](https://github.com/nfernal/pre-commit-hooks/actions/workflows/main.yml)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nfernal/pre-commit-hooks/main.svg)](https://results.pre-commit.ci/latest/github/nfernal/pre-commit-hooks/main)

pre-commit-hooks



Usage
--------

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/nfernal/pre-commit-hooks
    rev: v1.0.0  # Use the ref you want to point at
    hooks:
    -   id: check-commit-message-format
    # -   id: ...
```

Hooks
--------

-
