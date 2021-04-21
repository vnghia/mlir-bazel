# MLIR dialect examples with `Bazel`

This repo contains some easy dialect examples for [MLIR](https://mlir.llvm.org/) beginners but using `Bazel` as the build system (instead of `Cmake`) thanks to [llvm-bazel](https://github.com/google/llvm-bazel/).

## Examples

### An out-of-tree MLIR dialect

Based on [llvm-standalone](https://github.com/llvm/llvm-project/tree/main/mlir/examples/standalone).

#### Building

```bash
bazel build //mlir_bazel/standalone:standalone_opt --config=generic_clang
```
