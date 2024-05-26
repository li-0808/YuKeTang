from getJson import get_json
from globalVar import Var
from globalVar import headers_Host



def cache_mode():
    url = f"https://{headers_Host}/mooc-api/v1/lms/user/user-courses/"
    response = get_json(url)

    if response.status_code == 200:
        # 打印响应的文本内容（假设返回的是JSON）
        Var.classInfo_json = response.json()
        #print(Var.classInfo_json)
        if Var.classInfo_json is None:
            print("错误：未获到课程信息，请检查cookie正确性（请输入登陆后的cookie）")
    else:
        if response.status_code == 403:
            print("错误403，请检查cookie是否有误（过期）")
        else:
            print("错误:", response.status_code)
    # 提取所需信息
    Var.classInfo_data = [
        {
            "course_name": item["course_name"],
            "course_sign": item["course_sign"],
            "classroom_id": item["classroom_id"]
        }
        for item in Var.classInfo_json["data"]["product_list"]
    ]

    print(Var.classInfo_data)
