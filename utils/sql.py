import pymysql


class SQLHelper:
    host = ''
    port = 3306
    user = ''
    passwd = ''
    db = ''
    charset = 'utf8'

    def __init__(self, host: str, user: str, passwd: str, db: str, port: int = 3306, charset: str = "utf8"):
        host = host
        user = user
        passwd = passwd
        port = port
        db = db
        charset = charset

    @staticmethod
    def fetchOne(sql: str, args: list = []) -> dict:
        db = pymysql.connect(host=SQLHelper.host, port=SQLHelper.port, user=SQLHelper.user, passwd=SQLHelper.passwd, db=SQLHelper.db,
                             charset=SQLHelper.charset)  # 打开数据库连接
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, args);
        data = cursor.fetchone()
        db.close()
        return data

    @staticmethod
    def fetchAll(sql: str, args: list = []) -> dict:
        db = pymysql.connect(host=SQLHelper.host, port=SQLHelper.port, user=SQLHelper.user, passwd=SQLHelper.passwd, db=SQLHelper.db,
                             charset=SQLHelper.charset)  # 打开数据库连接
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, args);
        data = cursor.fetchall()
        db.close()
        return data

    @staticmethod
    def getInitRemainList(sql: str) -> dict:
        groupDict = {}
        for eachElement in SQLHelper.fetchAll(sql):
            for key, val in eachElement.items():
                groupDict[val] = []
        return groupDict

    @staticmethod
    def getInitRemainGroupId(sql: str) -> dict:
        groupIdDict = {}
        for eachElement in SQLHelper.fetchAll(sql):
            groupIdDict[eachElement["classId"]] = eachElement["groupId"]
        return groupIdDict
