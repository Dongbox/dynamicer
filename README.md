# dynamicer Library

`dynamicer` is a Python library designed to dynamically load and execute Python modules and C dynamic libraries. It provides a convenient way to import and run Python functions or classes and C functions from specified files dynamically.

[中文文档](README_CN.md)

## Features

- Import Python functions or classes dynamically from a module
- Run Python functions dynamically from a module
- Run C functions from a dynamic library
- Customized exception handling during service execution
- Cross-platform support for Linux and Windows

## Requirements

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)

## Installation

You can install `dynamicer` using pip:

```sh
pip install dynamicer
```

## Usage
from dynamicer import dynamicer

# Create an instance of dynamicer
dp = dynamicer()

# Import and run a Python function
func = dp.import_py("module_path", "function_name")
result = dp.run_py("module_path", "function_name", *args, **kwargs)

# Run a C function
dp.run_c("dll_path", "function_name", *args, arg_encoding="utf-8")

## Logging
The library uses Python's built-in logging module. You can enable or disable logging and set the logging level when initializing the dynamicer instance.

## Exceptions
- ModuleExecutionError: Raised when there is an error during the module execution phase.
- FunctionLoadError: Raised when the function cannot be loaded from the module or library.
- FunctionCallError: Raised when there is an error calling the function.

## Contributing
Please refer to the CONTRIBUTING.md for information on how to contribute to dynamicer.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.