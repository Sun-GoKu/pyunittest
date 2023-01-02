import requests
import json
import time
from TestFile.test_api import server

class RunMain():
    def send_post(self, url, data):
        respone = requests.post(url=url, data=data)
        result = respone.json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        respone.close()
        return res

    def send_get(self, url, data):
        respone = requests.get(url=url, data=data)
        result = respone.json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        respone.close()
        return res

    def run_what(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误,请检查!")

        return result


if __name__ == "__main__":
    # server.run(debug=True, port=8888, host="127.0.0.1")
    result1 = RunMain().run_what('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '123456'})
    result2 = RunMain().run_what('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '123'})
    print(result1)
    print(result2)