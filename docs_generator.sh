#!/usr/bin/env bash

MODULE_PATH=$1

# Generate source files from module path
sphinx-apidoc -f -o docs/source $MODULE_PATH

# Insert source file name
sed "s/Contents:/Contents:\n\n   $MODULE_PATH/g" docs/source/index.tmpl.rst > docs/source/index.rst

# Generate html documentation from source files
sphinx-build -b html docs/source docs/build
