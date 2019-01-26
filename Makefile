# This file contains a make script for the Coinstack application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/core/*.py src/ui/*.py
DATA_FILES=res/data/sample.script

BUILD_DIR=bin/coinstack

# This rule builds the application
build: $(SRC_FILES) $(DATA_FILES)
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(DATA_FILES) $(BUILD_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
