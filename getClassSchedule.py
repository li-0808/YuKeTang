import requests
from urllib.parse import quote
from globalVar import Var


def get_json():
    # 目标网站的URL
    url = "https://xijing.yuketang.cn/mooc-api/v1/lms/learn/course/schedule"

    # 需要发送的请求头
    headers = {
        "Host": "xijing.yuketang.cn",
        "Cookie": Var.cookie,
        "University-Id": "2679",
        "Xtbz": "cloud",
        # 根据需要添加其他头部信息
    }

    # 如果需要，这里可以添加请求的参数
    params = {
        "cid": Var.cid,
        "sign": "1",
        # 根据需要添加其他参数
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应的文本内容（假设返回的是JSON）
        Var.classSchedule_json = response.json()
        # print(Var.classSchedule_json)
    else:
        print("Error:", response.status_code)


def cache_mode():
    # 提取包含 total 和 done 字段的条目
    Var.classSchedule_work = [
        {id: {"total": details["total"], "done": details["done"]}}
        for id, details in Var.classSchedule_json["data"]["leaf_schedules"].items()
        if isinstance(details, dict)
    ]

    # 提取值为1或0的条目
    Var.classSchedule_sign = [
        {id: value}
        for id, value in Var.classSchedule_json["data"]["leaf_schedules"].items()
        if value in [1, 0]
    ]
