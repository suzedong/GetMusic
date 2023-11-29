import sys
import requests
import os
import pyfiglet

import Config
import Utils
import GetList
import Download

result = pyfiglet.figlet_format("BreakDay")
print(result)

print(f"\033[35;1m搜索服务由：{Config.url} 提供。\033[0m")
Utils.print_colored("本程序由SZD提供支持。", "34;1")

# 检查命令行参数数量
if len(sys.argv) >= 4:
    input_value = sys.argv[1]
    page_value = sys.argv[2]
    index_string = sys.argv[3]
    root_dir = sys.argv[4]
else:
    # 默认值
    input_value = None  # '汽车音乐'
    page_value = None  # '1,2,3,4,5,6,7,8,9,10' # '1'
    index_string = None  # 'all' # '1,3,5'
    root_dir = None  # os.path.expanduser('~/Downloads/GetMusic')  # 默认为用户的下载文件夹

    # 提示用户输入参数并使用默认值
    if not input_value:
        input_value = Utils.input_colored("请输入搜索关键词（默认为'汽车音乐'）：", "32;4") or '汽车音乐'
        print(f"您输入的文本是：{input_value}")
    if not page_value:
        page_value = Utils.input_colored(
            "请输入要下载的页号（指定页号时请输入具体页号，如：'1'，如多页请用逗号分隔，默认为'1,2,3,4,5,6,7,8,9,10'）：",
            "32;4") or '1,2,3,4,5,6,7,8,9,10'
        print(f"您输入的文本是：{page_value}")
    if not index_string:
        index_string = Utils.input_colored(
            "请输入要下载的索引（逗号分隔，如：'1,3,5'或 'all'，如果是多页索引自动为 'all'，默认为 'all'）：", "32;4") or 'all'
        print(f"您输入的文本是：{index_string}")
    if not root_dir:
        root_dir = Utils.input_colored("请输入下载文件的根目录（默认为'~/Downloads/GetMusic'）：",
                                       "32;4") or os.path.expanduser(
            '~/Downloads/GetMusic')
        print(f"您输入的文本是：{root_dir}")

# 检查逗号分割的数字字符串
if ',' in page_value:
    # 将数字字符串拆分成数字列表
    page_numbers = [int(number) for number in page_value.split(',')]
    index_string = 'all'
else:
    page_numbers = [int(page_value)]

for page_number in page_numbers:
    data_array = GetList.get_list(input_value, page_number)  # 获取搜索结果

    # 检查索引字符串是否为 "all"
    if index_string == 'all':
        indexes = range(len(data_array))
    else:
        # 将数字字符串拆分成数字列表，并将索引值减1
        indexes = [int(index) - 1 for index in index_string.split(',')]

    Download.get_file(indexes, data_array, root_dir, page_number)

# python your_script.py 汽车音乐 1 1,3,5

# 是的，您可以将程序及其相关依赖打包成一个可运行的包。一种常用的方法是使用 Python 的打包工具，如 setuptools 和 pip。

# 以下是一般的步骤：

# 创建一个新的文件夹来容纳您的项目。
# 在该文件夹中创建一个名为 setup.py 的文件，并将以下内容复制到该文件中：
# from setuptools import setup

# setup(
#     name='your_package_name',
#     version='1.0',
#     packages=[''],
#     install_requires=[
#         'requests',
#     ],
#     entry_points={
#         'console_scripts': [
#             'your_script_name = your_script_file:main',
#         ],
#     },
# )
# 请将 your_package_name 替换为您的包名称，将 your_script_name 替换为您想要的命令行脚本名称，将 your_script_file 替换为包含您的脚本代码的文件名。

# 将您的脚本代码复制到与 setup.py 文件相同的文件夹中，并将其命名为 your_script_file.py（与 setup.py 文件中的名称一致）。
# 在命令行中进入项目文件夹，并运行以下命令来构建您的包：
# $ python setup.py sdist
# 这将在项目文件夹中创建一个名为 dist 的文件夹，并在其中生成一个压缩文件，其中包含您的包及其依赖项。

# 您可以将生成的压缩文件分发给其他人，并让他们通过以下命令来安装和运行您的程序：
# $ pip install your_package_name
# $ your_script_name [arguments]
# 请确保将 your_package_name 和 your_script_name 替换为相应的名称。

# 通过这些步骤，您可以将您的程序及其相关依赖打包成一个可运行的包，并使其他人能够轻松地安装和运行它。

# ----------------------------------------------------------------------------

# 要将Python脚本打包成可在macOS下直接运行的程序，您可以使用PyInstaller工具。PyInstaller可以将Python脚本打包成独立的可执行文件，其中包含了所需的Python解释器和依赖库。

# 请按照以下步骤操作：

# 安装PyInstaller：在终端中运行以下命令安装PyInstaller：
# pip install pyinstaller
# 切换到包含您的Python脚本的目录。

# 使用以下命令将脚本打包为可执行文件：

# pyinstaller --onefile your_script_name.py
# 将 your_script_name.py 替换为您的Python脚本的文件名。

# 执行上述命令后，PyInstaller会在当前目录下创建一个名为 dist 的文件夹，并在其中生成可执行文件。

# 在 dist 文件夹中，您将找到一个与您的Python脚本同名的可执行文件。您可以将此文件复制到其他位置，并在macOS上直接运行它。

# 请注意，生成的可执行文件将包含您的Python脚本和所需的依赖项，因此它可能会比较大。如果您希望生成更小的可执行文件，可以尝试使用PyInstaller的一些选项进行优化。

# 希望这能帮助到您！如果您有任何其他问题，请随时提问。

# --------------------------------------------------------------------------


