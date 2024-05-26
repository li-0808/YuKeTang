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


# 读取config文件并检查必填和非必填字段，并对非必填字段施加默认值
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)

    # 必填字段
    required_fields = {
        'basic': ['school_name', 'school_id', 'cookie'],
        'email': ['receiver', 'sender', 'user', 'password']
    }

    # 默认值
    default_values = {
        'email': {
            'host': 'smtp.qq.com',
            'port': '465',
        }
    }

    # 检查必填字段
    for section, fields in required_fields.items():
        if section not in config:
            raise ValueError(f"The section '{section}' is missing in the configuration file.")
        for field in fields:
            if field not in config[section] or not config[section][field]:
                raise ValueError(f"The field '{field}' in the section '{section}' cannot be empty.")

    # 填充默认值
    for section, fields in default_values.items():
        if section not in config:
            config[section] = {}
        for field, default_value in fields.items():
            if field not in config[section] or not config[section][field]:
                print(f"The field '{field}' in the section '{section}' is empty. Using default value: {default_value}")
                config[section][field] = default_value

    return config


def get_headers_host():
    school_name = config['basic']['school_name']
    headers_host = school_name + ".yuketang.cn"
    return headers_host


config = load_config()
headers_Host = get_headers_host()
