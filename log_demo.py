# This is a sample Python script.
import time

from tencentcloud.log.cls_pb2 import LogGroupList
from tencentcloud.log.logclient import LogClient
from tencentcloud.log.logexception import LogException


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def upload(topic_id, client):
    LogLogGroupList = LogGroupList()
    LogGroup = LogLogGroupList.logGroupList.add()
    LogGroup.filename = "python.log"
    LogGroup.source = "127.0.0.1"

    #
    # LogTag = LogGroup.logTags.add()
    # LogTag.key = "key"
    # LogTag.value = "value"

    Log = LogGroup.logs.add()
    Log.time = int(round(time.time() * 1000000))

    Content = Log.contents.add()
    Content.key = "Hello"
    Content.value = "World"
    try:
        request = client.put_log_raw(topic_id, LogLogGroupList)
        print(f"{request.get_request_id()} 成功")
    except LogException as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    endpoint = 'https://ap-chongqing.cls.tencentcs.com'
    accessKeyId = 'AKIDnhYxGap12AAkKsLhru9Y6mhV6XtBKWZV'
    accessKey = 'CJOXexNl053wfBnP0hYYgxN1WuCIBsgf'
    topic_id = 'a8080cef-2d84-4291-a3ee-555c3d70facc'
    client = LogClient(endpoint, accessKeyId, accessKey)
    upload(topic_id, client)
