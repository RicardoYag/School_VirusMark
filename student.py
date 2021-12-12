import json, requests


class Data():
    def __init__(self, school, stuid, jing, wei, province, city, district, street) -> None:
        self.school = str(school)
        self.stuid = str(stuid)
        self.jing = jing
        self.wei = wei
        self.province = province
        self.city = city
        self.district = district
        self.street = street

    def post(self):
        try:
            url = 'https://fxgl.jx.edu.cn/' + self.school + '/public/homeQd?loginName=' + self.stuid + '&loginType=0'
            sess = requests.session()
            sess.get(url)
            url_json = 'https://fxgl.jx.edu.cn/' + self.school + '/studentQd/saveStu'
            header = {
                'Host': 'fxgl.jx.edu.cn',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Origin': 'https://fxgl.jx.edu.cn',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Content-type': 'application/x-www-form-urlencoded',
                'Referer': 'https://fxgl.jx.edu.cn/' + self.school + '/user/qdbp',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
            }
            addall = self.province + self.city + self.district + self.street
            js = {"xszt": "0", "lng": self.jing, "lat": self.wei, "province": addall, "city": self.city,
                  "district": self.district, "street": self.street, "sddlwz": addall, "mqtw": "0", "mqtwxq": "",
                  "zddlwz": addall,
                  "bprovince": self.province, "bcity": self.city, "bdistrict": self.district, "bstreet": self.street,
                  "sprovince": self.province, "scity": self.city, "sdistrict": self.district, "sfby": "1", "jkzk": "0",
                  "jkzkxq": "", "sfgl": "1", "gldd": ""}
            r_json = sess.post(url=url_json, data=js, headers=header)
            return json.loads(r_json.text)['msg']
        except:
            return "未知错误"

    def verify(self):
        url = 'https://fxgl.jx.edu.cn/' + self.school + '/public/homeQd?loginName=' + self.stuid + '&loginType=0'
        sess = requests.session()
        sess.get(url)
        # 上传数据签到
        url_json = 'https://fxgl.jx.edu.cn/' + self.school + '/studentQd/studentIsQd'
        header = {
            'Host': 'fxgl.jx.edu.cn',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Origin': 'https://fxgl.jx.edu.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
            'Content-type': 'application/x-www-form-urlencoded',
            'Referer': 'https://fxgl.jx.edu.cn/' + self.school + '/user/qdbp',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        try:
            r_json = sess.post(url=url_json, headers=header)
            msg = json.loads(r_json.text)
            if msg["data"] == 1:
                print(self.stuid + " 已签到")
            else:
                print(self.stuid + " 未签")
        except:
            print("数据错误")


def main(*args):
    # 参数需修改 1.学校代码 2.个人学号 3，4.打卡位置的经纬 5，6，7，8 按照打卡位置填对应经纬
    data = Data(4136010403, 8000123456, 115.801325, 28.656317, "江西省", "南昌市", "红谷滩区", "学府大道999号")
    # 上传打卡数据
    data.post()
    data.verify()


if __name__ == '__main__':
    main()
