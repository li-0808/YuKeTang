import requests
from urllib.parse import quote
from globalVar import Var



def get_json():
    school_name = config['basic']['school_name']
    headers_Host = school_name + ".yuketang.cn"
    headers_cookie = config['basic']['cookie']
    headers_University_Id = config['basic']['school_id']
    # 目标网站的URL
    url = "https://xijing.yuketang.cn/mooc-api/v1/lms/learn/course/chapter"

    # 需要发送的请求头
    headers = {
        "Host": headers_Host,
        "Cookie": headers_cookie,
        "University-Id": headers_University_Id,
        "Xtbz": "cloud",
        # 根据需要添加其他头部信息
    }

    # 如果需要,这里可以添加请求的参数
    params = {
        "cid": Var.cid,
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应的文本内容(假设返回的是JSON)
        Var.classChapter_json = response.json()
        # print(Var.classChapter_json)
    else:
        print("Error:", response.status_code)




def cache_mode():
    Var.classChapter_data = []
    for chapter in Var.classChapter_json["data"]["course_chapter"]:
        for section in chapter["section_leaf_list"]:
            if "leaf_list" in section:  # 检查是否存在leaf_list
                for leaf in section["leaf_list"]:
                    Var.classChapter_data.append({
                        "name": leaf["name"],
                        "id": leaf["id"],
                        "score_deadline": leaf.get("score_deadline")
                    })
            else:
                Var.classChapter_data.append({
                    "name": section["name"],
                    "id": section["id"],
                    "score_deadline": section.get("score_deadline")
                })

    #print(Var.classChapter_data)
