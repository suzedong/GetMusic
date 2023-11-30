import os
import pyfiglet
import tkinter as tk
import threading
from tkinter import filedialog

import DownloadGUI
import GetList

# 创建一个布尔变量来控制下载线程
stop_download = False
# 创建一个 Event 对象用于控制下载线程
stop_event = threading.Event()


def select_directory():
    initial_dir = os.path.expanduser("~/Downloads")  # 初始路径
    directory = filedialog.askdirectory(initialdir=initial_dir)  # 选择文件夹
    root_dir_entry.delete(0, tk.END)  # 清空输入框
    root_dir_entry.insert(0, directory)  # 输入文件夹路径


def stop_download_music():
    global stop_download
    stop_download = True
    stop_event.set()  # 设置 Event 对象，通知下载线程停止下载
    state_change(tk.NORMAL)


def state_change(state):
    input_entry.config(state=state)
    page_entry.config(state=state)
    index_entry.config(state=state)
    root_dir_entry.config(state=state)
    select_button.config(state=state)
    start_button.config(state=state)


def download_music():
    # ...
    state_change(tk.DISABLED)
    result_text.delete(1.0, tk.END)
    # 创建一个新线程用于下载
    download_thread = threading.Thread(target=download_music_thread)
    download_thread.start()


def download_music_thread():
    input_value = input_entry.get()
    page_value = page_entry.get()
    index_string = index_entry.get()
    root_dir = root_dir_entry.get()

    # 检查逗号分割的数字字符串
    if ',' in page_value:
        # 将数字字符串拆分成数字列表
        page_numbers = [int(number) for number in page_value.split(',')]
        index_string = 'all'
    else:
        page_numbers = [int(page_value)]

    for page_number in page_numbers:
        if stop_download:
            # 如果停止按钮被点击，终止下载
            break
        result_text.insert(tk.END, f"开始请求第{page_number}页数据", "bold")
        result_text.see(tk.END)
        data_array = GetList.get_list(input_value, page_number)  # 获取搜索结果
        result_text.insert(tk.END, f"->获取到{len(data_array)}条数据\n", "green")
        result_text.see(tk.END)

        if len(data_array) > 0:
            result_text.insert(tk.END, f"开始下载第{page_number}页数据\n", "bold")
            result_text.see(tk.END)
            # 检查索引字符串是否为 "all"
            if index_string == 'all':
                indexes = range(len(data_array))
            else:
                # 将数字字符串拆分成数字列表，并将索引值减1
                indexes = [int(index) - 1 for index in index_string.split(',')]

            DownloadGUI.download_gui(indexes, data_array, root_dir, page_number, result_text, stop_event)
        else:
            result_text.insert(tk.END, f"没有找到第{page_number}页数据\n", "red")


# 创建主窗口
window = tk.Tk()
window.title("音乐下载器")

# title_frame--------
title_frame = tk.Frame(window)
title_frame.pack(anchor="nw")
# 创建标题
tk.Label(title_frame, text=pyfiglet.figlet_format("BreakDay"), font=("Courier", 20)).pack(side="left")
tk.Label(title_frame, text=pyfiglet.figlet_format(" - GetMusic"), font=("Courier", 12)).pack(side="left", anchor="s")

# left_frame--------
left_frame = tk.Frame(window)
left_frame.pack(side="left", fill="y")
# grid_frame--------
grid_frame = tk.Frame(left_frame)
grid_frame.pack()

# 创建输入框和标签
tk.Label(grid_frame, text="搜索关键词：").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(grid_frame)
input_entry.insert(0, "汽车音乐")
input_entry.grid(row=0, column=1)

tk.Label(grid_frame, text="要下载的页号：").grid(row=1, column=0, sticky="e")
page_entry = tk.Entry(grid_frame)
page_entry.insert(0, "1,20,3,4,5,6,7,8,9,10")
page_entry.grid(row=1, column=1)

tk.Label(grid_frame, text="要下载的索引：").grid(row=2, column=0, sticky="e")
index_entry = tk.Entry(grid_frame)
index_entry.insert(0, "all")
index_entry.grid(row=2, column=1)

tk.Label(grid_frame, text="下载文件的根目录：").grid(row=3, column=0, sticky="e")
root_dir_entry = tk.Entry(grid_frame)
default_dir = os.path.expanduser("~/Downloads/GetMusic")
root_dir_entry.insert(0, default_dir)
root_dir_entry.grid(row=3, column=1)

# 添加文件夹选择按钮
select_button = tk.Button(grid_frame, text="选择文件夹", command=select_directory)
select_button.grid(row=3, column=2)

# 创建一个框架来容纳按钮
button_frame = tk.Frame(left_frame)
button_frame.pack(pady=10)

# 创建开始下载按钮
start_button = tk.Button(button_frame, text="开始下载", command=download_music)
start_button.pack(side=tk.LEFT, padx=10)

# 创建停止下载按钮
stop_button = tk.Button(button_frame, text="停止下载", command=stop_download_music)
stop_button.pack(side=tk.LEFT, padx=10)

# 创建结果标签
result_frame = tk.Frame(left_frame, padx=5, pady=5)
result_frame.pack(fill="both", expand=True)
result_text = tk.Text(result_frame)
result_text.tag_config("bold", font=("Arial", 12, "bold"))
result_text.tag_config("red", foreground="red")
result_text.tag_config("green", foreground="green")
result_text.insert(tk.END, "Hello, World!")
result_text.pack(fill="both", expand=True)

# right_frame--------
right_frame = tk.Frame(window)
right_frame.pack(fill="both", expand=True)

tk.Label(right_frame, text="Hello World!-----------------------").pack(side="top", anchor="w", padx=5, pady=5)
tk.Text(right_frame).pack(side="top", fill="both", expand=True, anchor="w", padx=5, pady=5)
tk.Button(right_frame, text="退出", command=window.destroy).pack(side="bottom", anchor="e", padx=5, pady=5)

# 运行主循环
window.mainloop()
