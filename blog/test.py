# coding: utf-8
"""
Created by Jeeyshe.Ru at 19-3-27 下午3:10, for any more contact me with jeeyshe@gmail.com.
Here is the descriptions and some purpose of the file:
    0. 测试里子
"""

import time, datetime

import requests

from lxml import etree


class TestView(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        print(self.__dict__)


if __name__ == '__main__':
    # start = datetime.datetime.strptime('2018-01-01', '%Y-%m-%d')
    #
    # end = datetime.datetime.now()
    #
    # t = end - start
    #
    # print(t, type(t), t.days, type(t.days))

    # url = 'http://127.0.0.1:8000/x/art/pTyQeGEUJi3BTPuTY348LS5'
    #
    # res = requests.patch(url, data={'name': '123', 'xyz': '2344'})
    #
    # try:
    #     print(res.json())
    # except:
    #     print(res.status_code)
    #     print(res.text)

    # html = """
    # <p>
    # <span style="font-family: 宋体; font-size: 18px; font-weight: bold;">废话不多，直接说正事， 列表解析式真神奇。<br/>有这样一个数据类型，列表嵌套元组<br/> </span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">users&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">= [(</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">&#39;wangwu5&#39;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">,&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">&#39;123&#39;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">), (</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">&#39;zhaoliu5&#39;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">,&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">&#39;123&#39;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">)]<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">us = [ ]<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">for user in users:<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">account,pwd = user<br/> </span><span style="font-family: Arial; font-size: 14px; color: rgb(128, 128, 128); font-style: italic;"><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">us.append(User(account=account,pwd=pwd))</span><br/> </span><span style="font-family: 宋体; font-size: 18px; font-weight: bold;">本来我用了这种最常见的for循环来遍历他，取得每一项的值，生成模型类的实例来传给sqlalchemy引擎&nbsp;写入数据库，实现后，我觉得这样写太普通，能不能写个高端大气上档次（装13）的写法呢？自然就想到了列表解析式这东西，这不写不要紧，一写就引发了一桩惊天大案。<span style="color: rgb(0, 176, 80);"></span><br/>来吧，列表解析式：<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold;"><span style="color: rgb(0, 176, 80);"># us = [User(account=user[0], pwd=user[1]) for user in users]</span><br/>试验了一下，果然可以，我python牛x！！！<br/>不过，我上边可是带着#注释符的，这是干嘛呢，我又想到了另外一种装13的东西，生成器，没错就是他<br/> </span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">us = (User(</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">account</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">=user[</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">0</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">],&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">pwd</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">=user[</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">1</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">])&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">for&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">user&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);">in&nbsp;</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold;"><span style="color: rgb(0, 176, 80);">users)</span><br/> </span><span style="font-family: 宋体; font-size: 18px; font-weight: bold;">拿过去一测试，我的天也可以，，再次高呼 python 666!<br/>完了呢，我又开始不消停了，我想到了另一种方法，列表解析式能不能嵌套呢，我去试试看，这一试果不其然又让我猜中了：<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);"># us = [User(account=account, pwd=pwd) for account, pwd in [user for user in users]]</span><span style="font-family: 宋体; font-size: 18px; font-weight: bold;"><span style="color: rgb(0, 176, 80);">&nbsp;</span><br/>口号走起，人生苦短，我用python!!!<br/>然而事情还没完，既然列表解析式能嵌套，那么生成器能不能嵌套呢？俺去试试看，。。。我只想说，我联想能力还是很强的（自吹一波）！<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold;"><span style="color: rgb(0, 176, 80);"># us = (User(a</span><span style="color: rgb(0, 176, 80);"></span><span style="color: rgb(0, 176, 80);">ccount=account, pwd=pwd) for account, pwd in (user for user in users))</span><br/>我的个天，来吧，换个口号喊一波，人生几何，python当歌！！<br/>嗯，原本觉得这样事情就算完了，但是呢，我突然有一个大胆的想法，既然生成器和列表解析式这么牛x，让他俩结合一下行不行呢！啊， 这次我不吹了，直接告诉你们，竟然也可以！<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold; color: rgb(0, 176, 80);"># us = [User(account=account, pwd=pwd) for account, pwd in (user for user in users)]<br/> </span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold;"><span style="color: rgb(0, 176, 80);"># us = (User(account=account, pwd=pwd) for account, pwd in [user for user in users])</span><br/> <br/>嗯，我的个天，咱python不是吹，是真的牛x啊！最后把这几个写法全部罗列出来，python威武霸气！<br/> <br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);">#&nbsp;</span><span style="font-size: 14px; font-style: italic; font-family: 宋体; color: rgb(0, 176, 240);">遍历</span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);">users,7</span><span style="font-size: 14px; font-style: italic; font-family: 宋体; color: rgb(0, 176, 240);">种方法都可以<br/> </span><span style="font-size: 14px; color: rgb(128, 128, 128); font-style: italic; font-family: 宋体;"><br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = [User(account=user[0], pwd=user[1]) for user in users]<br/> </span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">us = (User(</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">account</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">=user[</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">0</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">],&nbsp;</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">pwd</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">=user[</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">1</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">])&nbsp;</span><span style="font-family: Arial; font-size: 14px; font-weight: bold; color: rgb(0, 176, 240);">for&nbsp;</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">user&nbsp;</span><span style="font-family: Arial; font-size: 14px; font-weight: bold; color: rgb(0, 176, 240);">in&nbsp;</span><span style="font-family: Arial; font-size: 14px; color: rgb(0, 176, 240);">users)<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = [User(account=account, pwd=pwd) for account, pwd in [user for user in users]]<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = [User(account=account, pwd=pwd) for account, pwd in (user for user in users)]<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = (User(account=account, pwd=pwd) for account, pwd in [user for user in users])<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = (User(account=account, pwd=pwd) for account, pwd in (user for user in users))<br/> </span><span style="font-family: Arial; font-size: 14px; color: rgb(128, 128, 128); font-style: italic;"><br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us = []<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># for user in users:<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># account,pwd = user<br/> </span><span style="font-family: Arial; font-size: 14px; font-style: italic; color: rgb(0, 176, 240);"># us.append(User(account=account,pwd=pwd))</span><span style="font-style: italic; font-family: 宋体; font-size: 18px; font-weight: bold;"><br/>就是这么一个for循环，惹出一桩惊天血案！来吧,<span style="color: rgb(255, 0, 0);">life is short , we need python!</span></span>
    # </p>
    # """
    # tree = etree.HTML(html)
    # # s = tree.string()
    #
    # print(tree.xpath('string(.)'))

    # a = TestView(1, 2, 3, a=5, b=6)
    #
    # print(a)
    from django.contrib.admin import register


    pass


