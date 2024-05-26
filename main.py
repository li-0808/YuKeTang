import time
import random

import getClassInfo
import getClassChapter
import getClassSchedule
import printClassWork
import sendEmail
from globalVar import Var
from globalVar import config

if __name__ == "__main__":

    # 获取课程信息（课程名对应cid）
    getClassInfo.cache_mode()
    # 初始化[发邮正文内容]变量
    Var.sendemail_info = """ """
    # 初始化[未完成作业内容]变量
    unfinishedWork = ""
    # 每次请求后随机等待n秒(在config中填写,不填写随机等待1-10秒)
    if config['other']['wait_time'] == 0:
        wait_time = random.uniform(1, 10)
    else:
        wait_time = config['other']['wait_time']
    # 开始运行
    for course in Var.classInfo_data:
        # 初始化课程代码
        cid = 0
        print(f"课程名称: {course['course_name']}")
        cid = course['classroom_id']
        sendemail_classname = course['course_name']
        time.sleep(wait_time)
        # 获取所有的课程
        getClassChapter.cache_mode(cid)
        time.sleep(wait_time)
        # 获取每个课程下的作业情况
        getClassSchedule.cache_mode(cid)
        # 打印作业完成情况
        printClassWork.cache_mode()
        if not Var.unfinished_work:
            # print(Var.unfinished_work)
            # print("该课程所有作业已完成")

            Var.sendemail_info = "《" + sendemail_classname + "》所有作业已完成✓\n" + Var.sendemail_info
        else:
            # print(Var.unfinished_work)
            # unfinishedWork = sendemail_classname + Var.unfinished_work
            Var.sendemail_info = Var.sendemail_info + "▇▇▇▇▇《" + course[
                'course_name'] + "》▇▇▇▇▇\n" + Var.unfinished_work
        # Var.sendemail_info += Var.unfinished_work
    print(Var.sendemail_info)
    sendEmail.send_email()
