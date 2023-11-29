import requests
import Config


def get_list(input_value, page_number):
    # 构造请求数据
    data = {
        'input': input_value,  # 输入值
        'filter': 'name',  # 过滤条件
        'type': Config.type_value,  # 音乐来源
        'page': str(page_number)  # 页码
    }

    # 发送POST请求
    response = requests.post(Config.url, headers=Config.headers, data=data)

    # 将响应数据解析为JSON格式
    json_data = response.json()

    # 获取数据数组
    data_array = json_data['data']

    # 返回数据数组
    return data_array

