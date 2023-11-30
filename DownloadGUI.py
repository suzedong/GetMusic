import os
import requests
import tkinter as tk

import Utils

global file_path


def download_gui(indexes, data_array, root_dir, page_number, result_text, stop_event):
    global file_path
    for index in indexes:
        if stop_event.is_set():
            # 如果停止按钮被点击，终止下载
            break
        if 0 <= index < len(data_array):
            item = data_array[index]
            file_url = item['url']
            author = item['author']
            title = item['title']
            try:
                file_path = Utils.download_file(file_url, author, title, root_dir)

                result_text.insert(tk.END, f"第{page_number}页-第{index + 1}首-已下载文件: {file_path}\n")
                result_text.see(tk.END)
            except requests.exceptions.HTTPError as e:
                result_text.insert(tk.END, f"第{page_number}页-第{index + 1}首-下载文件失败: {e}", "red")
                # 删除下载过程中产生的文件
                if os.path.exists(file_path):
                    os.remove(file_path)
                    result_text.insert(tk.END, f"第{page_number}页-第{index + 1}首-删除文件: {file_path}", "red")
        else:
            result_text.insert(tk.END, f"第{page_number}页-索引 {index + 1} 超出数据范围\n", "red")
            result_text.see(tk.END)
    if stop_event.is_set():
        result_text.insert(tk.END, f"第{page_number}页-下载已停止\n", "red")
    else:
        # 如果下载完成，显示下载完成的提示
        result_text.insert(tk.END, f"第{page_number}页-下载完成\n", "green")
    result_text.see(tk.END)
