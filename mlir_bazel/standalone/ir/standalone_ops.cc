// This file is licensed under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

#include "mlir_bazel/standalone/ir/standalone_ops.h"

#include "mlir/IR/OpImplementation.h"
#include "mlir_bazel/standalone/ir/standalone_dialect.h"

#define GET_OP_CLASSES
#include "mlir_bazel/standalone/ir/standalone_ops.cc.inc"
