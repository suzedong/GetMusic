import requests
import os

import Utils

global file_path


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
            except requests.exceptions.HTTPError as e:
                print(f"第{page_number}页-第{index + 1}首-下载文件失败: {e}")
                # 删除下载过程中产生的文件
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"第{page_number}页-第{index + 1}首-删除文件: {file_path}")
        else:
            print(f"索引 {index + 1} 超出数据范围")
