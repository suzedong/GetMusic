import requests
import os

import Utils

global file_path


def check_and_remove_empty_folder(folder_path):
    # 检查文件夹是否为空
    if not os.listdir(folder_path):
        # 如果为空，删除文件夹
        os.rmdir(folder_path)
        Utils.print_colored(f"删除'{folder_path}'文件夹!!!", "31")
        # 同时检查并递归删除父文件夹
        parent_folder = os.path.dirname(folder_path)
        if not os.listdir(parent_folder):
            os.rmdir(parent_folder)
            Utils.print_colored(f"删除'{parent_folder}'文件夹!!!", "31")


def get_file(indexes, data_array, root_dir, page_number):
    """
    下载指定索引的文件并保存到指定目录中

    参数：
    indexes: 要下载的文件的索引列表
    data_array: 存储文件信息的数据数组
    root_dir: 文件保存的根目录
    page_number: 当前页码

    返回值：
    无

    """
    global file_path
    for index in indexes:
        if 0 <= index < len(data_array):
            item = data_array[index]
            file_url = item['url']
            author = item['author']
            title = item['title']

            try:
                file_path = Utils.download_file(file_url, author, title, root_dir)

                print(f"第{page_number}页-第{index + 1}首-已下载文件: {file_path}")
                # 判断文件大小
                file_size = os.path.getsize(file_path)
                if file_size < 3000000:  # 3M
                    os.remove(file_path)
                    Utils.print_colored(f"但是文件小于3M已经删除!!!", "31")
                    # 检查并删除空文件夹
                    check_and_remove_empty_folder(os.path.dirname(file_path))
            except requests.exceptions.HTTPError as e:
                Utils.print_colored(f"第{page_number}页-第{index + 1}首-下载文件失败: {e}", "31")
                # 删除下载过程中产生的文件
                if os.path.exists(file_path):
                    os.remove(file_path)
                    Utils.print_colored(f"第{page_number}页-第{index + 1}首-删除文件: {file_path}", "31")
        else:
            Utils.print_colored(f"索引 {index + 1} 超出数据范围", "31")
