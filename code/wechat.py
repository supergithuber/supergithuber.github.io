#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itchat, time
from itchat.content import *
import sys
import requests

KEY = '1fea22b738dd433da9316b991dc0f87c'

reload(sys)  
sys.setdefaultencoding('utf-8') 

#@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
#def text_reply(msg):
#    if cmp(msg.text, "你好") == 0:
#        msg.user.send('%s: %s' % (msg.type, msg.text))

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : '274076',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send("很高兴认识你，稍后会回复你消息。@sivanWu's robot")

itchat.auto_login(enableCmdQR=2)
itchat.run()


