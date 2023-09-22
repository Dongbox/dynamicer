# dynamicer 库

`dynamicer` 是一个Python库，旨在动态加载和执行Python模块和C动态库。它提供了一种方便的方法，可以从指定的文件动态地导入并运行Python函数或类和C函数。

[English Documentation](README.md)

## 特性

- 从模块动态导入Python函数或类
- 从模块动态运行Python函数
- 从动态库运行C函数
- 服务执行过程中的自定义异常处理
- 跨平台支持Linux和Windows

## 要求

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)

## 安装

您可以使用pip安装`dynamicer`：

```sh
pip install dynamicer
```

## 使用
from dynamicer import dynamicer

# 创建 dynamicer 实例
dp = dynamicer()

# 导入并运行Python函数
func = dp.import_py("module_path", "function_name")
result = dp.run_py("module_path", "function_name", *args, **kwargs)

# 运行C函数
dp.run_c("dll_path", "function_name", *args, arg_encoding="utf-8")

## 日志
该库使用Python的内置日志模块。您可以在初始化dynamicer实例时启用或禁用日志，并设置日志级别。

## 异常
- ModuleExecutionError：在模块执行阶段出现错误时引发。
- FunctionLoadError：当无法从模块或库加载函数时引发。
- FunctionCallError：在调用函数时出现错误时引发。

## 贡献
有关如何向dynamicer贡献的信息，请参阅CONTRIBUTING.md。

## 许可证
该项目根据MIT许可证授权 - 有关详细信息，请参阅LICENSE.md文件。

