# pytest demo

![example workflow](https://github.com/moshi4/github_action_tutorial/actions/workflows/CI.yml/badge.svg)
[![codecov](https://codecov.io/gh/moshi4/github_action_tutorial/branch/main/graph/badge.svg?token=SWC6XGVADQ)](https://codecov.io/gh/moshi4/github_action_tutorial)

pytest run example

```bash
# Install pytest pytest-cov
poetry install
# Activate poetry venv 
poetry shell
# Run pytest
pytest
# Run pytest with coverage
pytest --cov --cov-report xml
```
