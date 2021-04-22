# This file is licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

load("@llvm-project//mlir:tblgen.bzl", "gentbl")

gentbl(
    name = "standalone_dialect_inc_gen",
    tbl_outs = [
        ("-gen-dialect-decls", "ir/standalone_dialect.h.inc"),
        ("-gen-dialect-doc", "ir/standalone_dialect.md"),
    ],
    tblgen = "@llvm-project//mlir:mlir-tblgen",
    td_file = "ir/standalone_dialect.td",
    deps = [
        "@llvm-project//mlir:OpBaseTdFiles",
    ],
)

gentbl(
    name = "standalone_ops_inc_gen",
    tbl_outs = [
        ("-gen-op-decls", "ir/standalone_ops.h.inc"),
        ("-gen-op-defs", "ir/standalone_ops.cc.inc"),
        ("-gen-op-doc", "ir/standalone_ops.md"),
    ],
    tblgen = "@llvm-project//mlir:mlir-tblgen",
    td_file = "ir/standalone_ops.td",
    td_srcs = ["ir/standalone_dialect.td"],
    deps = [
        "@llvm-project//mlir:OpBaseTdFiles",
        "@llvm-project//mlir:SideEffectTdFiles",
    ],
)

cc_library(
    name = "standalone_mlir",
    srcs = [
        "ir/standalone_dialect.cc",
        "ir/standalone_ops.cc",
    ],
    hdrs = [
        "ir/standalone_dialect.h",
        "ir/standalone_ops.h",
    ],
    deps = [
        ":standalone_dialect_inc_gen",
        ":standalone_ops_inc_gen",
        "@llvm-project//mlir:IR",
    ],
)

cc_binary(
    name = "standalone-opt",
    srcs = ["standalone_opt.cc"],
    visibility = ["//visibility:public"],
    deps = [
        ":standalone_mlir",
        "@llvm-project//llvm:Support",
        "@llvm-project//mlir:AllPassesAndDialects",
        "@llvm-project//mlir:MlirOptLib",
        "@llvm-project//mlir:Support",
    ],
)
