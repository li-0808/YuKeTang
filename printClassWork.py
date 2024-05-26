from globalVar import Var
import datetime

def cache_mode():
    # 创建两个空的字符串变量来存储分类后的数据
    Var.unfinished_work = ""
    Var.finished_work = ""

    # 遍历列表1，为每个元素寻找匹配的列表2中的数据
    for item in Var.classChapter_data:
        item_id = str(item['id'])  # 将ID转换为字符串，以便与列表2的键匹配
        for data in Var.classSchedule_work:
            if item_id in data:
                # 匹配到后，修改键名并添加到matched_items中
                workInfo = {
                    '题目': item['name'],
                    '总题数': data[item_id]['total'],
                    '已完成数': data[item_id]['done'],
                    '完成情况': '已完成' if data[item_id]['total'] == data[item_id]['done'] else '未完成',
                    '截止时间': item['score_deadline']
                }
                #时间戳转换为可读的时间
                deadline_timestamp = workInfo['截止时间']
                deadline_datetime = datetime.datetime.fromtimestamp(deadline_timestamp / 1000)
                # 格式化时间
                deadline_str = deadline_datetime.strftime('%Y-%m-%d %H:%M:%S')
                # 根据完成情况分类存储信息
                if workInfo['完成情况'] == '未完成':
                    Var.unfinished_work += f"》题目:{workInfo['题目']}\n\t┏完成情况(总/已完成):{workInfo['总题数']}/{workInfo['已完成数']}\n\t┗截止时间:{deadline_str}\n"
                else:
                    Var.finished_work += f"题目：{workInfo['题目']}作业已完成✓\n"

    # 返回分类后的字符串变量
    return Var.unfinished_work, Var.finished_work
