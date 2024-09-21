import time
from enum import Enum

from tencentcloud.log.cls_pb2 import LogGroupList
from tencentcloud.log.logclient import LogClient
from tencentcloud.log.logexception import LogException


class TopicID(Enum):
    NORMAL_LOG = 'a8080cef-2d84-4291-a3ee-555c3d70facc'
    # 可以根据需要添加更多 topic_id


class AlphaxLogUploader:
    def __init__(self):
        # 固定配置
        self.endpoint = 'https://ap-chongqing.cls.tencentcs.com'
        self.access_key_id = 'AKIDnhYxGap12AAkKsLhru9Y6mhV6XtBKWZV'
        self.access_key = 'CJOXexNl053wfBnP0hYYgxN1WuCIBsgf'
        self.client = LogClient(self.endpoint, self.access_key_id, self.access_key)

    def upload(self, topic: TopicID, content_dict: dict) -> bool:
        # Create a LogGroupList
        log_group_list = LogGroupList()
        log_group = log_group_list.logGroupList.add()

        # 设置日志组元数据
        log_group.filename = "none"
        log_group.source = "127.0.0.1"

        # 添加日志条目
        log_entry = log_group.logs.add()
        log_entry.time = int(round(time.time() * 1000000))

        # 添加日志内容
        for key in content_dict.keys():
            content = log_entry.contents.add()
            content.key = str(key)
            content.value = str(content_dict[key])

        # 尝试上传日志
        try:
            request = self.client.put_log_raw(topic.value, log_group_list)
            print(f"Request ID: {request.get_request_id()} 上传成功")
            return True
        except LogException as e:
            print(f"日志上传失败: {e}")
            return False
