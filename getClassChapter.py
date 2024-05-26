from getJson import get_json
from globalVar import Var
from globalVar import headers_Host


def cache_mode(cid):
    url = f"https://{headers_Host}/mooc-api/v1/lms/learn/course/chapter"
    params = {
        "cid": cid
    }
    response = get_json(url, params)
    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应的文本内容(假设返回的是JSON)
        Var.classChapter_json = response.json()
        # print(Var.classChapter_json)
    else:
        print("Error:", response.status_code)

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

    # print(Var.classChapter_data)
