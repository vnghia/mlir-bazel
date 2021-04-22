# This file is licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import os

import lit.formats
import lit.util

from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst

# Configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = "MLIR_" + os.environ["TEST_TARGET"]

config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

# suffixes: A list of file extensions to treat as test files.
config.suffixes = [".mlir"]

# test_source_root: The root path where tests are located.
config.test_source_root = config.mlir_test_dir

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.environ["RUNFILES_DIR"]

llvm_config.use_default_substitutions()

# Tweak the PATH to include the tools dir.
llvm_config.with_environment("PATH", config.llvm_tools_dir, append_path=True)

tool_dirs = config.mlir_tools_dirs + [config.llvm_tools_dir]

tool_names = config.mlir_tool_names

tools = [ToolSubst(s, unresolved="ignore") for s in tool_names]
llvm_config.add_tool_substitutions(tools, tool_dirs)
