import asyncio
import time
import json
import requests
import datetime
from playwright.sync_api import sync_playwright

def main():
    sendCode()

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

        # data = {"group_id": "256615371", "message": title + '\n' + exp_time + '\n' + code_list_str}
        # response = requests.post("http://127.0.0.1:5900/send_group_msg", data=data)
        data = {"user_id": "254923340", "message": title + '\n' + exp_time + '\n' + code_list_str}
        response = requests.post("http://127.0.0.1:5900/send_private_msg", data=data)
        # res = json.loads(response)
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
    main()
