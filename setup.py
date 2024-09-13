from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='yaml_plotter',                  # 包名
    version='0.1.0',                   # 版本号
    description='A Python plotter using yaml',  # 简短描述
    author='Yezheng Zhang',                # 作者姓名
    author_email='cozardzhang@gmail.com',  # 作者邮箱
    url='https://github.com/pxxxl/yaml-plotter',  # 项目的主页
    packages=find_packages(),          # 自动发现包
    install_requires=parse_requirements('requirements.txt'),  # 依赖列表
    classifiers=[                      # 分类标签，便于在 PyPI 上查找
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',           # Python 版本要求
)
