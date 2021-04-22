# This file is licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

load("//mlir_bazel/testing:gen_lit_test.bzl", "gen_lit_test")

filegroup(
    name = "standalone_litcfg",
    testonly = True,
    srcs = [
        "standalone.lit.site.cfg.py",
    ],
)

gen_lit_test(
    data = [
        ":standalone_litcfg",
        "//mlir_bazel/standalone:standalone-opt",
    ],
    litprefix = "standalone.lit",
    mlirfiles = [
        "standalone.foo.mlir",
        "standalone-opt.mlir",
    ],
    root_test_dir = "mlir_bazel/standalone/tests/",
)
