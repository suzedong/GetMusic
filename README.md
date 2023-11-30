# GetMusic v0.8.0
## 简介
一个简单的爬虫，可以爬取网易云音乐的歌曲，并下载到本地。

## 依赖
requests
sys
os
pyfiglet

## 使用
``` 
python GetMusic.py 汽车音乐 1 1,3,5
python GetMusic.py 汽车音乐 1,2,3,4,5,6,7,8,9,10 all

python GetMusic.py 周杰伦 2 1,3,5
python GetMusic.py 周杰伦 2 all
``` 

## 说明
1. 第一个参数为歌曲的关键字或歌手名，第二个参数为获取列表的页号，多页用逗号隔开，第三个参数为列表中歌曲的序号，用逗号隔开，如果需要获取全部歌曲，则用all代替序号。
2. 脚本会自动创建文件夹，并将歌曲下载到本地。
3. ~~脚本会自动跳过已经下载过的歌曲。~~


## 打包
是的，您可以将程序及其相关依赖打包成一个可运行的包。一种常用的方法是使用 Python 的打包工具，如 `setuptools` 和 `pip`。

以下是一般的步骤：

创建一个新的文件夹来容纳您的项目。
在该文件夹中创建一个名为 `setup.py` 的文件，并将以下内容复制到该文件中：
```python
from setuptools import setup

setup(
    name='your_package_name',
    version='1.0',
    packages=[''],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_script_file:main',
        ],
    },
)
```
请将 `your_package_name` 替换为您的包名称，将 `your_script_name` 替换为您想要的命令行脚本名称，将 `your_script_file` 替换为包含您的脚本代码的文件名。

将您的脚本代码复制到与 `setup.py` 文件相同的文件夹中，并将其命名为 `your_script_file.py`（与 `setup.py` 文件中的名称一致）。
在命令行中进入项目文件夹，并运行以下命令来构建您的包：
```shell
$ python setup.py dist
```
这将在项目文件夹中创建一个名为 `dist` 的文件夹，并在其中生成一个压缩文件，其中包含您的包及其依赖项。

您可以将生成的压缩文件分发给其他人，并让他们通过以下命令来安装和运行您的程序：
```shell
$ pip install your_package_name
$ your_script_name [arguments]
```
请确保将 `your_package_name` 和 `your_script_name` 替换为相应的名称。

通过这些步骤，您可以将您的程序及其相关依赖打包成一个可运行的包，并使其他人能够轻松地安装和运行它。

## 打包成可在macOS下直接运行的程序
```shell
pyinstaller -F --collect-all pyfiglet GetMusic.py 
pyinstaller -F --windowed --collect-all pyfiglet GetMusicGUI.py
```

`pyinstaller -F --windowed --collect-all pyfiglet GetMusicGUI.py` 是一个使用 PyInstaller 打包包含 `pyfiglet` 库和 `GetMusicGUI.py` 脚本的命令。

具体解释如下：

- `pyinstaller` 是 PyInstaller 的命令行工具，用于将 Python 脚本打包成可执行文件。
- `-F` 参数指定将所有依赖项打包到一个单独的可执行文件中，而不是生成多个文件。
- `--windowed` 参数告诉 PyInstaller 创建一个没有命令行窗口的可执行文件，这意味着它将作为一个 GUI 应用程序运行。
- `--collect-all` 参数告诉 PyInstaller 收集所有的依赖项，包括那些在代码中动态导入的模块。
- `pyfiglet` 是要打包的库或模块的名称。
- `GetMusicGUI.py` 是要打包的 Python 脚本文件的名称。

综合起来，这个命令的目的是将 `GetMusicGUI.py` 脚本及其所有依赖项（包括 `pyfiglet` 库）打包成一个独立的可执行文件。打包后的可执行文件将作为一个没有命令行窗口的 GUI 应用程序运行，可以在适当的操作系统上直接运行，而无需安装 Python 和额外的依赖项。

请确保在执行此命令之前已经安装了 PyInstaller，并在命令行中可以访问到它。此外，你还需要在包含 `GetMusicGUI.py` 脚本的目录中执行此命令，以确保正确地打包所有依赖项。

---

要将Python脚本打包成可在macOS下直接运行的程序，您可以使用`PyInstaller`工具。`PyInstaller`可以将Python脚本打包成独立的可执行文件，其中包含了所需的Python解释器和依赖库。

请按照以下步骤操作：

安装`PyInstaller`：在终端中运行以下命令安装`PyInstaller`：
```shell
pip install pyinstaller
```
切换到包含您的Python脚本的目录。

使用以下命令将脚本打包为可执行文件：
```shell
pyinstaller --onefile your_script_name.py
```
将 `your_script_name.py` 替换为您的Python脚本的文件名。

执行上述命令后，`PyInstaller`会在当前目录下创建一个名为 `dist` 的文件夹，并在其中生成可执行文件。

在 `dist` 文件夹中，您将找到一个与您的Python脚本同名的可执行文件。您可以将此文件复制到其他位置，并在macOS上直接运行它。

请注意，生成的可执行文件将包含您的Python脚本和所需的依赖项，因此它可能会比较大。如果您希望生成更小的可执行文件，可以尝试使用PyInstaller的一些选项进行优化。
