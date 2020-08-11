# coding: utf-8
"""
    此模块仅用于定义数据库文件, xadmin配置
"""
from random import choice

from shortuuid import ShortUUID

default_app_config = 'blog.apps.DbConfig'


class NewUUID(ShortUUID):
    """
    固定长度为12, 使用时instance.random
    """

    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        super().__init__(alphabet)

    @property
    def _length(self):
        return 12


def random_prefix(length=3, string=None):
    """
    随机生成n位数前缀以避免图片名字重复
    :param length: 后缀长度
    :param string: 备选元素
    :return: 后缀字符串
    """
    if string is None:
        string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(choice(string, k=length))


class BookId(NewUUID):
    """
    专题id
    """

    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        super().__init__(alphabet)

    @property
    def _length(self):
        return 4


class ChapterId(BookId):
    """
    章节id
    """

    @property
    def _length(self):
        return 6
