// This file is licensed under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

#ifndef MLIR_BAZEL_STANDALONE_IR_STANDALONE_OPS_H_
#define MLIR_BAZEL_STANDALONE_IR_STANDALONE_OPS_H_

#include "mlir/IR/BuiltinTypes.h"
#include "mlir/IR/Dialect.h"
#include "mlir/IR/OpDefinition.h"
#include "mlir/Interfaces/SideEffectInterfaces.h"

#define GET_OP_CLASSES
#include "mlir_bazel/standalone/ir/standalone_ops.h.inc"

#endif  // MLIR_BAZEL_STANDALONE_IR_STANDALONE_OPS_H_
