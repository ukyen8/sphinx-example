#!/usr/bin/env bash

MODULE_PATH=$1
SOURCE_DIR=docs/source
BUILD_DIR=docs/build

# Generate source files from module path
sphinx-apidoc -f -o $SOURCE_DIR $MODULE_PATH

# Insert source file name
sed "s/Contents:/Contents:\n\n   $MODULE_PATH/g" $SOURCE_DIR/index.tmpl.rst > $SOURCE_DIR/index.rst

# Generate html documentation from source files
sphinx-build -b html $SOURCE_DIR $BUILD_DIR/$MODULE_PATH
