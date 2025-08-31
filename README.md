# app_interpreter
![build status](https://github.com/praisetompane/app_interpreter/actions/workflows/app.yaml/badge.svg)


## Objectives
A toy Postfix notation program interpreter.

## Project Structure
- docs: Project documentation lives in here.
- src: Production code lives in folder and is divided in the modules below:
    - app_interpreter: Project package.
    - app.py: Entry point to startup the application
- tests: Test code lives in folder.
    The tests are intentionally separated from production code.
    - benefits:
        - Tests can run against an installed version after executing `pip install .`.
        - Tests can run against the local copy with an editable install after executing `pip install --edit`.
    - more in depth discussion here: https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules
  -

## Dependencies
- [python 3.12+](https://www.python.org/downloads/)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development.
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## Usage
    ```shell
    python src/app.py ./tests/resources/factorial.txt
    ```

## Testing
- Run unit and integration tests
    ```shell
    pytest
    ```
- End to End tests
    - Not Implemented

## Git Conventions
- **NB:** The main is locked and all changes must come through a Pull Request.
- Commit Messages:
    - Provide concise commit messages that describe what you have done.
        ```shell
        # example:
        git commit -m "feat(core): algorithm" -m"implement my new shiny faster algorithm"
        ```
    - References:
        - https://www.conventionalcommits.org/en/v1.0.0/
        - https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

**Disclaimer**: This is still work in progress.