import os
from setuptools import setup, find_packages

# 获取项目的元数据
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "dynamicer", "__version__.py"), encoding="utf-8") as f:
    exec(f.read(), about)

# 读取README文件作为长描述
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

# 依赖列表
requires = [
]

# 测试需求
test_requirements = [
]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],  # 分类器列表，指定了项目的发展状态、主题和支持的Python版本等信息
    python_requires='>=3.6',  # 指定项目所需的Python版本
    tests_require=test_requirements,
)
