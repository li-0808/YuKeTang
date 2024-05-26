import globalVar
import requests


def get_json(url, params=None):
    school_name = globalVar.config['basic']['school_name']
    headers_Host = school_name + ".yuketang.cn"
    headers_cookie = globalVar.config['basic']['cookie']
    headers_University_Id = globalVar.config['basic']['school_id']

    # 需要发送的请求头
    headers = {
        "Host": headers_Host,
        "Cookie": headers_cookie,
        "University-Id": headers_University_Id,
        "Xtbz": "cloud",
        # 添加其他头部信息
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    return response
