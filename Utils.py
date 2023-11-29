# 以下是一些常用的ANSI转义序列示例：

# 控制文本颜色：

# \033[30m：黑色
# \033[31m：红色
# \033[32m：绿色
# \033[33m：黄色
# \033[34m：蓝色
# \033[35m：洋红色
# \033[36m：青色
# \033[37m：白色
# 控制背景颜色：

# \033[40m：黑色背景
# \033[41m：红色背景
# \033[42m：绿色背景
# \033[43m：黄色背景
# \033[44m：蓝色背景
# \033[45m：洋红色背景
# \033[46m：青色背景
# \033[47m：白色背景
# 控制样式：

# \033[1m：粗体
# \033[4m：下划线
# 重置所有样式：

# \033[0m

def print_colored(text, color_code):
    """
    打印带有颜色的文本。

    参数：
    text (str): 需要打印的文本。
    color_code (int): 文本的颜色代码。

    返回：
    无返回值。
    """
    print(f"\033[{color_code}m{text}\033[0m")


def input_colored(prompt, color_code):
    """
    根据给定的颜色代码，打印带有颜色的提示，并接收用户的输入。

    参数：
    prompt (str) -- 要显示的提示信息
    color_code (int) -- 颜色代码

    返回：
    str -- 用户输入的字符串
    """
    print(f"\033[{color_code}m{prompt}\033[0m", end='')
    return input()
