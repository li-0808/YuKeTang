import json
import requests
from urllib.parse import quote
from globalVar import Var
from globalVar import config


def get_json():
    school_name = config['basic']['school_name']
    headers_Host = school_name + ".yuketang.cn"
    headers_cookie = config['basic']['cookie']
    headers_University_Id = config['basic']['school_id']


    # 目标网站的URL
    url = f"https://{headers_Host}/mooc-api/v1/lms/user/user-courses/"

    # 需要发送的请求头
    headers = {
        "Host": headers_Host,
        "Cookie": headers_cookie,
        "University-Id": headers_University_Id,
        "Xtbz": "cloud",
        # 添加其他头部信息
    }

    # 发送GET请求
    response = requests.get(url, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应的文本内容（假设返回的是JSON）
        Var.classInfo_json = response.json()
        #print(Var.classInfo_json)
        if Var.sendemail_info is None :
            print("错误：未获取课程信息，请检查cookie完整性（请输入xijing.yuketang.cn登陆后的cookie）")



    else:
        if response.status_code == 403:
            print("错误403，请检查cookie是否有误（过期）")
        else:
            print("错误代码：Error:", response.status_code)



def cache_mode():
    # 提取所需信息
    Var.classInfo_data = [
        {
            "course_name": item["course_name"],
            "course_sign": item["course_sign"],
            "classroom_id": item["classroom_id"]
        }
        for item in Var.classInfo_json["data"]["product_list"]
    ]

    #print(Var.classInfo_data)
