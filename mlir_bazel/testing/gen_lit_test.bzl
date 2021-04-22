# This file is licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

load("@bazel_skylib//lib:paths.bzl", "paths")

def gen_lit_test(name = "", root_test_dir = "", mlirfiles = [], litprefix = "lit", data = []):
    for i, mlirfile in enumerate(mlirfiles):
        native.py_test(
            name = mlirfile.replace(".", "_").replace("-", "_"),
            srcs = ["@llvm-project//llvm:lit"],
            args = [
                "{mlirpath} ".format(mlirpath = paths.join(root_test_dir, mlirfile)) +
                "--config-prefix={litprefix} ".format(litprefix = litprefix) +
                "-v",
            ],
            data = data + [
                "//{}:{}".format(root_test_dir.rstrip("/"), mlirfile),
                "//mlir_bazel/testing:litcfg",
                "@llvm-project//llvm:FileCheck",
                "@llvm-project//llvm:count",
                "@llvm-project//llvm:not",
            ],
            main = "lit.py",
        )
