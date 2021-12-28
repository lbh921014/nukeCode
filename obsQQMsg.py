from flask import Flask, request

import asyncio
import time
import json
import requests
import datetime
from playwright.sync_api import sync_playwright

'''注意，这里的import api是另一个py文件，下文会提及'''
# import nukeCode

app = Flask(__name__)

'''监听端口，获取QQ信息'''

@app.route('/post_data', methods=['POST'])
def post_data():
    '下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
    if request.get_json().get('message_type') == 'private':  # 如果是私聊信息
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        print(message)
        # api.keyword(message, uid)  # 将 Q号和原始信息传到我们的后台
        if uid == 254923340 and message == '核弹密码':
            print('触发条件')
            # nukeCode.sendCode()
            sendCode()

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        # api.keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        print(message)
        if gid == 256615371 and message == '核弹密码':
            print('触发条件')
            sendCodeGroup()
    return "OK"

def sendCode():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        page = context.new_page()
        page.goto("https://nukacrypt.com/")
        time.sleep(1)
        rows = page.query_selector_all('div[id="nuclearcodess"] table[class="contenttable"] tbody tr')
        print(len(rows))
        i = 0
        title = ""
        exp_time = ""
        code_list_str = ""
        code_list = []
        for row in rows:
            if i == 1:
                title = row.inner_text()
            if i == 2:
                exp_time = row.inner_text()
            if i == 3:
                code_list_str = row.inner_text()
                elements = row.query_selector_all('td')
                for item in elements:
                    item.inner_text()
                    code_list.append(item.inner_text())
            i += 1
        print("title=%s" % title)
        print("expTime=%s" % exp_time)
        print("codeListStr=%s" % code_list_str)
        print(code_list)
        page.close()
        context.close()
        browser.close()

        data = {"user_id": "254923340", "message": title + '\n' + exp_time + '\n' + code_list_str}
        response = requests.post("http://127.0.0.1:5900/send_private_msg", data=data)
        print(response)

def sendCodeGroup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        page = context.new_page()
        page.goto("https://nukacrypt.com/")
        time.sleep(1)
        rows = page.query_selector_all('div[id="nuclearcodess"] table[class="contenttable"] tbody tr')
        print(len(rows))
        i = 0
        title = ""
        exp_time = ""
        code_list_str = ""
        code_list = []
        for row in rows:
            if i == 1:
                title = row.inner_text()
            if i == 2:
                exp_time = row.inner_text()
            if i == 3:
                code_list_str = row.inner_text()
                elements = row.query_selector_all('td')
                for item in elements:
                    item.inner_text()
                    code_list.append(item.inner_text())
            i += 1
        print("title=%s" % title)
        print("expTime=%s" % exp_time)
        print("codeListStr=%s" % code_list_str)
        print(code_list)
        page.close()
        context.close()
        browser.close()

        data = {"group_id": "256615371", "message": title + '\n' + exp_time + '\n' + code_list_str}
        response = requests.post("http://127.0.0.1:5900/send_group_msg", data=data)
        # data = {"user_id": "254923340", "message": title + '\n' + exp_time + '\n' + code_list_str}
        # response = requests.post("http://127.0.0.1:5900/send_private_msg", data=data)
        # res = json.loads(response)
        print(response)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)  # 此处的 host和 port对应上面 yml文件的设置