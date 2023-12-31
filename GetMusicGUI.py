import os
import pyfiglet
import tkinter as tk
import threading
from tkinter import filedialog

import DownloadGUI
import GetList

# 创建一个布尔变量来控制下载线程
stop_download = False
stop_select = False
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


def stop_select_pages():
    global stop_select
    stop_select = True
    select_state_change(tk.NORMAL)


def state_change(state):
    input_entry.config(state=state)
    page_entry.config(state=state)
    index_entry.config(state=state)
    root_dir_entry.config(state=state)
    select_button.config(state=state)
    start_button.config(state=state)
    radiobutton_pages0.config(state=state)
    radiobutton_pages1.config(state=state)
    select_pages_button.config(state=state)
    pages_entry.config(state=state)
    p_label.config(state=state)
    stop_select_button.config(state=state)


def select_state_change(state):
    select_pages_button.config(state=state)
    pages_entry.config(state=state)


def select_pages():
    global stop_select
    select_state_change(tk.DISABLED)
    pages_text.delete(1.0, tk.END)
    stop_select = False
    # 创建一个新线程用于下载
    download_thread = threading.Thread(target=select_pages_thread)
    download_thread.start()


def radiobutton_pages():
    # print(radiobutton_pages_var.get())
    entry_var = tk.StringVar()
    if radiobutton_pages_var.get() == 0:  # 单选
        text_var.set("1")
        page_entry.config(from_=1, to=99, width=2, textvariable=text_var)
        pages_label.config(text="要下载的页号：")
        # index_entry.delete(0, tk.END)
        # index_entry.insert(0, "1,3,5")
        entry_var.set("1,3,5")
        index_entry.config(textvariable=entry_var)
        index_entry.config(state=tk.NORMAL)
    elif radiobutton_pages_var.get() == 1:  # 多选
        text_var.set("10")
        page_entry.config(from_=2, to=99, width=2, textvariable=text_var)
        pages_label.config(text=f"从1-{page_entry.get()}页下载：")
        # index_entry.delete(0, tk.END)
        # index_entry.insert(0, "all")
        entry_var.set("all")
        index_entry.config(textvariable=entry_var)
        index_entry.config(state=tk.DISABLED)


def spinbox_page():
    if radiobutton_pages_var.get() == 1:  # 多选
        pages_label.config(text=f"从1-{page_entry.get()}页下载：")


def select_pages_thread():
    input_value = input_entry.get()
    page_numbers = pages_entry.get()
    for page_number in range(int(page_numbers)):
        if stop_select:
            pages_text.insert(tk.END, f"在第{page_number}页-停止查询!!!\n", "red")
            pages_text.see(tk.END)
            # 如果停止按钮被点击，终止下载
            break
        pages_text.insert(tk.END, f"开始请求第{page_number + 1}页数据", "bold")
        pages_text.see(tk.END)
        data_array = GetList.get_list(input_value, page_number + 1)  # 获取搜索结果
        pages_text.insert(tk.END, f"->获取到{len(data_array)}条数据\n", "green")
        pages_text.see(tk.END)

        if len(data_array) > 0:
            # 显示查询结果
            index_int = 1
            for item in data_array:
                pages_text.insert(tk.END, f"{index_int}.{item['author']} - {item['title']} 来源: {item['type']}\n")
                index_int += 1

            pages_text.see(tk.END)

    if not stop_select:
        pages_text.insert(tk.END, f"{page_numbers}页-查询完成!!!\n", "green")
        pages_text.see(tk.END)

    select_state_change(tk.NORMAL)


def download_music():
    # ...
    global stop_download
    state_change(tk.DISABLED)
    result_text.delete(1.0, tk.END)
    stop_download = False
    stop_event.clear()
    # 创建一个新线程用于下载
    download_thread = threading.Thread(target=download_music_thread)
    download_thread.start()


def download_music_thread():
    input_value = input_entry.get()

    if radiobutton_pages_var.get() == 1:
        page_value = ','.join(str(i) for i in range(1, int(page_entry.get()) + 1))
    else:
        page_value = page_entry.get()

    index_string = index_entry.get()
    root_dir = root_dir_entry.get()

    # 下载完成后的回调函数，重新启用状态为 DISABLED 的组件
    def download_complete_callback():
        print(f"{page_number} == {page_numbers[-1]}")
        if page_number == page_numbers[-1]:
            # 如果是最后一个页面，重新启用组件
            state_change(tk.NORMAL)

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

        pages_text.insert(tk.END, f"第{page_number}页\n", "green")
        if len(data_array) > 0:
            # 显示查询结果
            index_int = 1
            for item in data_array:
                pages_text.insert(tk.END, f"{index_int}.{item['author']} - {item['title']} 来源: {item['type']}\n")
                index_int += 1

            pages_text.see(tk.END)

            result_text.insert(tk.END, f"开始下载第{page_number}页数据\n", "bold")
            result_text.see(tk.END)
            # 检查索引字符串是否为 "all"
            if index_string == 'all':
                indexes = range(len(data_array))
            else:
                # 将数字字符串拆分成数字列表，并将索引值减1
                indexes = [int(index) - 1 for index in index_string.split(',')]

            DownloadGUI.download_gui(indexes, data_array, root_dir, page_number, result_text, stop_event,
                                     download_complete_callback)
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
tk.Label(title_frame, text=pyfiglet.figlet_format(" - GetMusic v0.9.5"), font=("Courier", 12)).pack(side="left", anchor="s")

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

select_frame = tk.Frame(grid_frame)
select_frame.grid(row=0, column=2, sticky="w")
select_pages_button = tk.Button(select_frame, text="查询", command=select_pages)
select_pages_button.pack(side="left")
pages_entry = tk.Spinbox(select_frame, from_=1, to=10, width=2)
pages_entry.pack(side="left")
p_label = tk.Label(select_frame, text="页")
p_label.pack(side="left")
stop_select_button = tk.Button(select_frame, text="停止", command=stop_select_pages)
stop_select_button.pack(side="left")

pages_label = tk.Label(grid_frame, text="从1-10页下载：")
pages_label.grid(row=1, column=0, sticky="e")
# page_entry = tk.Entry(grid_frame,)
# page_entry.insert(0, "1,2,3,4,5,6,7,8,9,10")
text_var = tk.StringVar()
text_var.set("10")
page_entry = tk.Spinbox(grid_frame, from_=2, to=99, width=2, textvariable=text_var, command=spinbox_page)
page_entry.grid(row=1, column=1, sticky="w")
radiobutton_frame = tk.Frame(grid_frame)
radiobutton_frame.grid(row=1, column=2, sticky="w")
radiobutton_pages_var: tk.IntVar = tk.IntVar(value=1)
radiobutton_pages1 = tk.Radiobutton(radiobutton_frame, text="多页", variable=radiobutton_pages_var, value=1,
                                    command=radiobutton_pages)
radiobutton_pages1.pack(side="left")
radiobutton_pages0 = tk.Radiobutton(radiobutton_frame, text="单页", variable=radiobutton_pages_var, value=0,
                                    command=radiobutton_pages)
radiobutton_pages0.pack(side="left")

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
select_button.grid(row=3, column=2, sticky="w")

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

tk.Label(right_frame, text="查询结果:-----------------------").pack(side="top", anchor="w", padx=5, pady=5)
pages_text = tk.Text(right_frame)
pages_text.tag_config("bold", font=("Arial", 12, "bold"))
pages_text.tag_config("red", foreground="red")
pages_text.tag_config("green", foreground="green")
pages_text.pack(side="top", fill="both", expand=True, anchor="w", padx=5, pady=5)
tk.Button(right_frame, text="退出", command=window.destroy).pack(side="bottom", anchor="e", padx=5, pady=5)

# 运行主循环
window.mainloop()
