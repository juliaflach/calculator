#!/usr/bin/env bash

# Dont write pyc files
export PYTHONDONTWRITEBYTECODE=1
# Uses /tmp for cache files (__pycache__)
export PYTHONPYCACHEPREFIX=/tmp
# Turns off buffering for easier container logging
export PYTHONUNBUFFERED=1
