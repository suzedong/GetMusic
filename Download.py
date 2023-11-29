import requests
import os
import Config

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
                response = requests.get(file_url)
                response.raise_for_status()  # 检查是否下载成功

                # 提取扩展名
                ext = os.path.splitext(file_url)[1]

                # 构造文件夹名和文件名
                folder_name = author
                file_name = f"{author} - {title}{ext}"

                # 创建文件夹（如果不存在）
                folder_path = os.path.join(root_dir, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # 下载文件并保存到相应的文件夹中
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)

                print(f"第{page_number}页-第{index + 1}首-已下载文件: {file_path}")
            except requests.exceptions.HTTPError as e:
                print(f"第{page_number}页-第{index + 1}首-下载文件失败: {e}")
                # 删除下载过程中产生的文件
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"第{page_number}页-第{index + 1}首-删除文件: {file_path}")
        else:
            print(f"索引 {index + 1} 超出数据范围")
