#!/usr/bin/env bash

# Move to directory of any-project-setup.
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd $SCRIPT_DIR/any-project-setup

python -m src.{MODULE}.main $SCRIPT_DIR/{CFG}
