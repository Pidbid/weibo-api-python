"""
name:微博API
site:https://www.wicos.me
"""

import requests as rq
import json

class Weibo():
    def __init__(self, appKey, appSecret, redirectUrl, token=None):
        super(Weibo, self).__init__()
        self.appKey = appKey
        self.appSecret = appSecret
        self.redirectUrl = redirectUrl
        if token:
            self.token = token

    def error(self,msg):
        status = 0
        if "error_code" in msg and "error" in msg:
            rt = {"status":1,"error_code":msg['error_code'],"error_msg":msg["error"]}
            return rt
        else:
            return {"status":status}

    def chectToken(self, setTime=3600):
        preData = {
            "access_token": self.token
        }
        getMsg = rq.post("https://api.weibo.com/oauth2/get_token_info", data=preData)
        getJson = getMsg.json()
        error = self.error(getJson)
        if self.error(getJson)['status'] == 1:
            return error
        if getJson['expire_in'] < setTime:
            rt = '{"error":"1","msg":"Token is valid for only 1 hour"}'
        else:
            rt = '{"error":"0","msg":"Token is valid"}'
        return rt

    def isToken(self,t):
        if not t:
            self.token = t
            return self.token
        else:
            try:
                with open("weibo.json", 'rb') as fp:
                    a = json.load(fp)
                self.token = a['token']
                return self.token
            except:
                return ""


    def Client(self):
        # urlDict = {":":"%3A","/":"%2F","?":"%3F","&":"%26"}
        rt = "https://api.weibo.com/2/oauth2/authorize?client_id=" + self.appKey + "&response_type=code&display=default&redirect_uri=" + self.redirectUrl
        print(rt)
        return rt

    def getToken(self, code,save=None):
        preData = {
            "client_id": self.appKey,
            "client_secret": self.appSecret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirectUrl
        }
        getMsg = rq.post("https://api.weibo.com/oauth2/access_token", data=preData)
        getJson = getMsg.json()
        error = self.error(getJson)
        if self.error(getJson)['status'] == 1:
            return error
        token = getJson['access_token']
        msg = {"token":token}
        if save:
            with open("weibo.json", 'w+', encoding='utf-8') as fp:
                fp.write(json.dumps(msg, indent=4))
        print("token:%s"%token)
        return token

    def getUsermsg(self, value, getType=None):
        if getType:
            key = "screen_name"
        else:
            key = "uid"
        preParams = {
            "access_token": self.token,
            key: value
        }
        getMsg = rq.get("https://api.weibo.com/2/users/show.json", params=preParams)
        getJson = getMsg.json()
        error = self.error(getJson)
        if self.error(getJson)['status'] == 1:
            return error
        return getJson

    def postArticle(self, title, coverLink, content, text, summary=None):
        preData = {
            "title": title,
            "content": content,
            "cover": coverLink,
            "text": text,
            "access_token": self.token
        }
        if summary:
            preData.update({"summary": summary})
        getMsg = rq.post("https://api.weibo.com/proxy/article/publish.json", data=preData)
        getJson = getMsg.json()
        error = self.error(getJson)
        if self.error(getJson)['status'] == 1:
            return error
        print(getJson)

    def postWeibo(self, content, securityDomain, picFilePath=None,token=None):
        if token:
            self.token = token
        preData = {
            "access_token": self.token,
            "status": content + securityDomain
        }
        if picFilePath:
            fp = open(picFilePath, "rb")
            fileName = fp.name
            file = {
                "pic": (fileName, open(picFilePath, "rb"))
            }
            getMsg = rq.post("https://api.weibo.com/2/statuses/share.json", data=preData, files=file)
        else:
            getMsg = rq.post("https://api.weibo.com/2/statuses/share.json", data=preData)
        getJson = getMsg.json()
        error = self.error(getJson)
        if self.error(getJson)['status'] == 1:
            return error
        return getJson
