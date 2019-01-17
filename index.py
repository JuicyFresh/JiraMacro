#!/usr/bin/python3
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



import sys
sys.path.append('./lib')
import defaultAction

defaultLink = open('include/defaultLink', 'r').read()
pageId, description = defaultAction.initVariables()
Home = 'http://10.186.117.221/JiraMacroOnWeb/index.py'
print('''
{defaultLink}

<meta charset="UTF-8" />

<body class="aui-page-focused aui-page-notification">
    <header id="header" role="banner">
      <nav class="aui-header" role="navigation">
          <div class="aui-header-primary">
              <h3 id="logo" class="aui-header-logo aui-header-logo-textonly"><a href="index.py"><span class="aui-header-logo-device">SW Integration</span></a></h3>
          </div>
          <div class="aui-header-secondary">
              <ul class="aui-nav">
                 <li><a class="aui-button aui-button-primary">LOG IN</a></li>
                 <h1 id="logo" class="aui-header-logo aui-header-logo-aui"><img src="http://webostv.developer.lge.com/application/files/1114/7512/5378/webOSIDE.png"></img></h1>
              </ul>
          </div>
      </nav>
    </header>

    <section id="content" role="main">

        <nav class="aui-navgroup aui-navgroup-horizontal">
            <div class="aui-navgroup-inner">
                <div class="aui-navgroup-primary">
                    <ul class="aui-nav">
                        {listStr}
                    </ul>
                </nav>
            </div>
        </div>

        <nav class="aui-navgroup aui-navgroup-horizontal"></nav> <!-- 줄 긋기 위해 -->
        <div class="aui-page-panel">
            <div class="aui-page-panel-inner">
              <section class="aui-page-panel-content">
                {description}
              </section>
            </div>
        </div>
    </section>
</body>

'''.format(Home=Home, listStr=defaultAction.menuList(), defaultLink=defaultLink, description=description))
