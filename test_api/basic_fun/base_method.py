import requests
import json

class RunMain():
    def send_get(self,url,data,header=None):
        if header!=None:
            res=requests.get(url=url,params=data,headers=header).json()
        else:
            res = requests.get(url=url, params=data).json()
        return res

    def send_post(self,url,data,header=None):
        if header != None:
            res=requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def run_main(self,url,method,data,header=None):
        res=None
        if method.lower()=='get':
            res=self.send_get(url,data,header)
        elif method.lower()=='post':
            res=self.send_post(url,data,header)
        return json.dumps(res,indent=2)