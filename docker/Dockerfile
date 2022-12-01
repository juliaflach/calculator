# For more information, please refer to:
# https://aka.ms/vscode-docker-python
# https://docs.docker.com/engine/reference/builder/

############ Base image ############
FROM python:3.10.7-slim as math_test_base

# Set apt config for not use interactive method.
ENV DEBIAN_FRONTEND='noninteractive'

# Set TZ.
ENV TZ='America/Sao_Paulo'

# Keeps Python from generating .pyc files in the container.
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging.
ENV PYTHONUNBUFFERED=1

# System update.
RUN apt-get update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get -y autoclean && rm -rf /var/lib/apt/lists/*

# apt-utils: needed for some internal configs of apt command.
# Build-essentials: the package for compiling things, needed for things on requirements.txt.
RUN apt-get update && \
    apt-get install -y apt-utils build-essential && \
    apt-get -y autoremove && \
    apt-get -y autoclean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade PIP for last version.
RUN /usr/local/bin/python -m pip install --upgrade pip

# Copy some env scripts.
COPY docker/python3.sh /etc/profile.d/
COPY docker/init.sh /etc/profile.d/

# Create workspace folder.
RUN mkdir -p /var/app

# Install application needed packages.
COPY requirements.txt /tmp/requirements.txt
RUN /usr/local/bin/pip3 install --no-cache-dir --requirement /tmp/requirements.txt


############ VS Code stuff to develop ############
FROM math_test_base as math_test_base_vscode

# Python libraries to help on python development best practices.
RUN /usr/local/bin/pip3 install --no-cache-dir ipython pylint pycodestyle coverage
