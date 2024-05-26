from globalVar import Var
from globalVar import headers_Host
from getJson import get_json



def cache_mode(cid):
    url = f"https://{headers_Host}/mooc-api/v1/lms/learn/course/schedule"

    params = {
        "cid": cid,
        "sign": "1"
    }

    response = get_json(url, params)
    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应的文本内容（假设返回的是JSON）
        Var.classSchedule_json = response.json()
        # print(Var.classSchedule_json)
    else:
        print("Error:", response.status_code)

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
