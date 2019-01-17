#!/usr/bin/python3.5
#-*- coding: utf-8 -*-
# HTTP 헤더 규격

print("content-type:text/html; charset=UTF-8\n")
print()

#아래는 브라우저에서 한글을 표기하기 위한 코드
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로, cgitb.enable()
# 할 경우 런타임 에러를 웹브라우저로 전송한다
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우
# 웹서버는 클라이언트에게 HTTP 응답코드 500을 전송한다
import cgi
import cgitb
cgitb.enable()



sys.path.append('/home/bi-part/BSP/macro/lib')
import requests
import json
from requests.auth import HTTPBasicAuth
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
id = form.getvalue('id')
password  = form.getvalue('password')

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
dataSet = {
    "jql": "assignee = 'sangwoo.ahn' AND resolution = Unresolved",
    "startAt": 0,
    "maxResults": 15,
    "fields": [
        "summary",
        "status",
        "assignee"
    ]
}
r = requests.post('https://harmony.lge.com:8443/issue/rest/api/2/search',
    data=json.dumps(dataSet),
    auth=HTTPBasicAuth('sangwoo.ahn', '@435dkstkddn'),
    headers=headers)
# print(dir(r.text))
print(dir(r))

print('''
    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script type="text/javascript">
        jQuery( document ).ready(function(){

          });
    </script>
''')
