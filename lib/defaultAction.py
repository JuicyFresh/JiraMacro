import os
import cgi
def menuList():
    subFiles = os.listdir('subPages')
    menu = ''
    for file in subFiles:
        fileName = file.split('.')[0]
        address = cgi.FieldStorage() # 주소창의 정보를 얻어 온다.
        if 'id' in address:
            if fileName == address['id'].value:
                menu += '<li class="aui-nav-selected"><a href="index.py?id={name}">{name}</a></li>'.format(name=fileName)
                continue
        menu += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=fileName)
    return menu


def initVariables():
    form = cgi.FieldStorage() # 주소창의 정보를 얻어 온다.
    if 'id' in form:
        pageId = form['id'].value
        description = open('subPages/'+pageId+'.html', 'r', encoding='utf-8').read()
    else:
        pageId = 'Welcome'
        description = 'Welcome to Macro World'
    return pageId, description
