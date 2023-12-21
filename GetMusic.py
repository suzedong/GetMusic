import sys
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
