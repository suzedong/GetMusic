import os
import requests
import tkinter as tk


def download_gui(indexes, data_array, root_dir, page_number, result_text, stop_event):
    for index in indexes:
        if stop_event.is_set():
            # 如果停止按钮被点击，终止下载
            break
        if 0 <= index < len(data_array):
            item = data_array[index]
            file_url = item['url']
            author = item['author']
            title = item['title']

            response = requests.get(file_url)

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

            result_text.insert(tk.END, f"第{page_number}页-第{index + 1}首-已下载文件: {file_path}\n")
            result_text.see(tk.END)
        else:
            result_text.insert(tk.END, f"第{page_number}页-索引 {index + 1} 超出数据范围\n", "red")
            result_text.see(tk.END)
    if stop_event.is_set():
        result_text.insert(tk.END, f"第{page_number}页-下载已停止\n", "red")
    else:
        # 如果下载完成，显示下载完成的提示
        result_text.insert(tk.END, f"第{page_number}页-下载完成\n", "green")
    result_text.see(tk.END)
