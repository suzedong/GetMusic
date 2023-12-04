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

---

如果你使用Python编写带有GUI的软件，并希望实现自动更新功能，可以按照以下步骤进行操作：

1. 版本管理：在你的软件中定义一个版本号变量，用于标识当前软件的版本。例如，你可以在代码中定义一个变量 `current_version = "1.0"`。

2. 版本检测：编写代码来检查远程服务器上是否有新的版本可用。你可以使用Python的网络请求库（如requests）向服务器发送请求，并获取最新版本的信息。服务器可以提供一个API接口或一个包含最新版本信息的文件。

    以下是一个使用requests库进行版本检测的示例代码：
    ```python
    import requests
    
    def check_update():
        url = "http://your-server.com/version.txt"  # 远程服务器上保存最新版本信息的文件URL
        response = requests.get(url)
        latest_version = response.text.strip()  # 获取最新版本号，假设版本号以文本形式保存在文件中
        return latest_version
    
    def compare_versions(current_version, latest_version):
        # 比较当前版本和最新版本，判断是否有新版本可用
        return latest_version > current_version
    
    # 在适当的时机调用 check_update() 函数，并与当前版本进行比较
    latest_version = check_update()
    if compare_versions(current_version, latest_version):
        # 有新版本可用，执行更新操作
        # 下面的步骤将在后续解释
    ```
3. 下载更新：如果检测到有新版本可用，你可以使用requests库下载更新文件。更新文件可以是一个压缩包或安装程序，根据你的需求进行选择。

    以下是一个使用requests库下载更新文件的示例代码：
    ```python
    def download_update():
        url = "http://your-server.com/update.zip"  # 远程服务器上保存更新文件的URL
        response = requests.get(url)
        with open("update.zip", "wb") as file:
            file.write(response.content)
    ```
4. 更新安装：下载更新文件后，你需要编写逻辑来安装更新。这可能涉及解压文件、替换旧文件、执行必要的配置更改等。你可以使用Python的zipfile模块来解压文件，并根据需要进行其他操作。

    以下是一个使用zipfile模块解压更新文件的示例代码：
    ```python
    import zipfile
    import os
    
    def install_update():
        zip_file = "update.zip"  # 下载的更新文件名
        extract_path = "update"  # 解压路径
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_path)
        # 执行其他更新操作，例如替换旧文件、执行配置更改等
        # 注意：在执行更新前，请确保备份用户数据和设置
    
        # 更新完成后，删除下载的更新文件和解压后的文件夹
        os.remove(zip_file)
        os.rmdir(extract_path)
    ```
5. 用户通知：在更新过程中，向用户提供适当的通知和反馈。你可以使用Python的GUI库（如Tkinter、PyQt等）来创建通知窗口、进度条或其他界面元素，以显示更新进度和结果。

    以下是一个使用Tkinter库创建简单通知窗口的示例代码：
    ```
    import tkinter as tk
    
    def show_notification(message):
        root = tk.Tk()
        root.title("更新通知")
        label = tk.Label(root, text=message)
        label.pack()
        root.mainloop()
    
    # 在适当的时机调用 show_notification() 函数，向用户显示更新通知
    show_notification("有新版本可用！正在下载更新...")
    ```
请注意，以上示例代码只是提供了一个基本的框架，你需要根据你的具体需求进行适当的修改和完善。此外，自动更新涉及到网络请求、文件操作等敏感操作，因此要确保代码的安全性和稳定性，以及适当的错误处理和异常处理。

