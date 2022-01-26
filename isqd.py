import json
import requests
from utils.sql import SQLHelper

# 注意填写学校代码
school = ""

qq_to_stuName = {}

# 创建每个班的提醒空列表
remainList = SQLHelper.getInitRemainList("select distinct classId from usertable")

# 班级号对应班级群号的字典
remainGroupId = SQLHelper.getInitRemainGroupId("select distinct classId,groupId from usertable")


# 获取签到状态
def getMarkStatus(stuId):
    url = 'https://fxgl.jx.edu.cn/' + school + '/public/homeQd?loginName=' + stuId + '&loginType=0'
    sess = requests.session()
    sess.get(url, allow_redirects=False)
    url_json = 'https://fxgl.jx.edu.cn/' + school + '/studentQd/studentIsQd'
    header = {
        'Host': 'fxgl.jx.edu.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Origin': 'https://fxgl.jx.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
        'Content-type': 'application/x-www-form-urlencoded',
        'Referer': 'https://fxgl.jx.edu.cn/' + school + '/user/qdbp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    r_json = sess.post(url=url_json, headers=header)
    msg = json.loads(r_json.text)
    if msg["data"] != 1:
        return False
    else:
        return True


# 获取提醒列表
def getRemainList():
    for element in SQLHelper.fetchAll("select * from usertable"):
        stuId = element["stuId"]
        qqId = element["qqId"]
        groupId = element["groupId"]
        stuName = element["stuName"]
        classId = element["classId"]
        # 获取签到状态，没签到的加入提醒和统计列表
        if not getMarkStatus(stuId):
            global qq_to_stuName
            remainList[classId].append(qqId)
            qq_to_stuName[qqId] = stuId + "-" + stuName
            print(stuId + "-" + stuName + " 未打卡")


# 通知打卡
def sendQQMessage():
    for eachClass, needRemainPerson in remainList.items():
        # print(eachClass,needRemainPerson)
        str_personsQQ = ""
        if needRemainPerson:
            for element in needRemainPerson:
                str_personsQQ = str_personsQQ + element + ','
            url = "https://api.domain.com/group?qq=%s&msg=打卡\n&key=zouhy2001&at=%s" % (remainGroupId[eachClass], str_personsQQ)
            requests.get(url)
            print(str_personsQQ)


def task():
    getRemainList()
    sendQQMessage()


if __name__ == "__main__":
    task()
