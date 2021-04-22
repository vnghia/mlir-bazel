# This file is licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import os
import lit.llvm

real_test_srcdir = os.environ["TEST_SRCDIR"]
external_srcdir = real_test_srcdir

config.llvm_tools_dir = os.path.join(external_srcdir, "llvm-project", "llvm")

standalone_tools_dirs = ["mlir_bazel/standalone/"]
config.mlir_tools_dirs = [
    os.path.join(real_test_srcdir, os.environ["TEST_WORKSPACE"], s)
    for s in standalone_tools_dirs
]

test_dir = os.environ["TEST_TARGET"]
test_dir = test_dir.strip("/").rsplit(":", 1)[0]
config.mlir_test_dir = os.path.join(
    real_test_srcdir, os.environ["TEST_WORKSPACE"], test_dir
)

config.mlir_tool_names = ["standalone-opt"]

lit.llvm.initialize(lit_config, config)

# Let the main config do the real work.
lit_config.load_config(
    config,
    os.path.join(
        os.path.join(
            real_test_srcdir,
            os.environ["TEST_WORKSPACE"],
            "mlir_bazel/testing/lit.cfg.py",
        )
    ),
)
