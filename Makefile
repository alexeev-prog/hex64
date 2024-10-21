CC = gcc
CC_FLAGS = -shared -W -fPIC

BASE_SRC_DIR = hex64_diagnostic/clibs/src
BASE_BIN_DIR = hex64_diagnostic/clibs/bin
RAM_LIB_SRC = $(BASE_SRC_DIR)/ram.c
RAM_LIB_SO = $(BASE_SRC_DIR)/ram.so

build:
	@echo "CC 		| ${RAM_LIB_SRC} -> ${RAM_LIB_SO}"
	@$(CC) $(CC_FLAGS) $(RAM_LIB_SRC) -o $(RAM_LIB_SO)
