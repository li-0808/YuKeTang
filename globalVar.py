import json


class Var:
    def __init__(self):
        self.cid = None
        self.cookie = None
        self.classInfo_json = None
        self.classInfo_data = None
        self.classChapter_json = None
        self.classChapter_data = None
        self.classSchedule_json = None
        self.classSchedule_work = None
        self.classSchedule_sign = None
        self.finished_work = None
        self.unfinished_work = None
        self.sendemail_info = None


Var = Var()


def load_config():
    with open('config.json', 'r') as config_json:
        config = json.load(config_json)
    return config


config = load_config()
