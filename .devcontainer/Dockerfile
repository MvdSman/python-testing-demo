# Setup base image
# See https://github.com/devcontainers/images/tree/main/src/python
ARG IMAGE_SEMVER=
ARG PYTHON_VERSION="3.12"
ARG VARIANT=
# ARG VARIANT="-buster" # Use -bullseye variants on arm64/Apple Silicon
FROM mcr.microsoft.com/vscode/devcontainers/python:${IMAGE_SEMVER}${PYTHON_VERSION}${VARIANT}
SHELL ["/bin/bash", "-c"]

ARG USER="vscode"
ARG HOME="/home/$USER"
## Reflect new user in PATH
ENV PATH="${HOME}/.local/bin:$PATH"

# Define the path to the virtualenv to work with
ARG VENV_PATH="$HOME/venv"

# Install Poetry
ARG POETRY_VERSION="1.8.3"
ENV PATH="/opt/poetry/bin:$PATH"

## NOTE: When using in-project venv, prepend Python commands with "poetry run" i.e. "poetry run pytest"
USER "root"
RUN pip3 install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION} \
	&& poetry config virtualenvs.in-project true

# Install additional dependencies
RUN pip3 install pipx && pipx ensurepath && pipx install pre-commit && pipx install copier && pipx install pytest

# Give user $USER Poetry permissions
RUN chown -R $USER:$USER /home/$USER/.config

# Change back to user
USER $USER

# Setup local workdir
WORKDIR ${HOME}/tmp/poetry

# Install required dependencies into local venv
RUN python3 -m venv ${VENV_PATH}
