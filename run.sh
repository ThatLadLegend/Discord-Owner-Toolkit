#!/bin/bash

# Ensure we're in the Colour Gen directory
cd "$(dirname "$BASH_SOURCE")"

# Set variables for python versions. Could probably be done cleaner, but this works.
PYTHON38_VERSION=`python3.8 -c 'import sys; version=sys.version_info[:3]; print("{0}".format(version[1]))' || { echo "no py38"; }`

if [ "$PYTHON38_VERSION" -eq "8" ]; then # Python3.8 = 3.8
    python3.8 main.py
    exit
fi

echo "You are running an unsupported Python version."
echo "Please use a version of Python above 3.8"
