# coding: utf-8
"""
Created by Jeeyshe.Ru at 19-3-27 下午2:52, for any more contact me with jeeysie@gmail.com.
Here is the descriptions and some purpose of the file:
    0. 一些工具函数
"""

import os
import json
import datetime
import base64

from django.core.cache import caches

from blog import models as _m
from ishare import settings as _st


def get_value_from_db(key, default):
    # 从extend数据库读取值, 不存在则返回默认值
    obj = _m.Expand.objects.filter(key=key).first()
    return obj.value if obj else default


def today_key():
    # 获取redis中存储的今日日期
    return datetime.datetime.now().strftime('%y%m%d')


class ContextUtil(object):
    """
    关于全局模板上下文的工具
    """

    @classmethod
    def origin_art_cnt(cls) -> int:
        # 获取原创文章数量
        return _m.Blog.objects.filter(source__isnull=True, is_active=True).count()

    @classmethod
    def run_days(cls) -> int:
        # 网站运行天数
        start = datetime.datetime.strptime(get_value_from_db("SITE_START", "2020-03-20"), '%Y-%m-%d')
        now = datetime.datetime.now()
        times = now - start
        return times.days

    @classmethod
    def copy_art_cnt(cls) -> int:
        # 获取原创文章数量
        return _m.Blog.objects.filter(source__isnull=False, is_active=True).count()

    @classmethod
    def visit_cnt(cls) -> int:
        # 总访问次数统计
        visit_cnt = int(get_value_from_db('VISIT_CNT', 753))
        return visit_cnt

    @classmethod
    def today_visit_cnt(cls) -> int:
        # 今日访问次数
        cache = caches['four']
        today = cache.get(today_key(), 0)
        return today

    @classmethod
    def most_read(cls):
        # 阅读次数最多的几条
        num = int(get_value_from_db('MOST_READ_NUM', 10))
        query = _m.Blog.objects.order_by('-read').filter(is_active=True)[:num]
        return query

    @classmethod
    def notice(cls):
        # 网站公告
        num = int(get_value_from_db('NOTICE_SHOW_NUM', 3))
        query = _m.Notice.objects.order_by('-add').filter(is_active=True)[:num]
        return query

    @classmethod
    def recommend(cls):
        # 推荐阅读
        num = int(get_value_from_db('RECOMMEND_NUM', 10))
        query = _m.Blog.objects.order_by('-add').filter(is_active=True, is_fine=True)[:num]
        return query

    @classmethod
    def random_tags(cls):
        # 随机标签云, 数量在百万以下采用这种方法， 很明显个人博客足够了
        num = int(get_value_from_db('TAG_CLOUD_NUM', 20))
        query = _m.Tag.objects.order_by('?').filter(is_active=True)[:num]
        return query

    @classmethod
    def you_may_like(cls, request):
        # 猜你喜欢: 当用户阅读某一文章的详情时，随机取出这篇文章的同类别和同标签文章几篇进行推荐
        raise NotImplementedError()

    @staticmethod
    def cats(pre='A'):
        # 站点除了散文之外的技术博客
        return _m.Category.objects.order_by('-add').filter(is_active=True, pre_cat=pre)

    @classmethod
    def person_links(cls):
        # 个人主页连接
        return _m.Link.objects.order_by('-add').filter(is_active=True, cat=1)


def make_auth_token(obj, salt, join_str='---'):
    # 制作用于标记用户在线的token
    token_string = join_str.join([salt, obj.pk])
    new_string = str(base64.b64encode(bytes(token_string, encoding='utf-8')))
    return new_string.split("'")[1]


def parse_auth_token(token, salt, join_str='---'):
    # 反解token
    obj = object()
    s = base64.b64decode(bytes(token, encoding='utf-8')).decode('utf-8')
    up_salt, up_obj_str = s.split(join_str)
    if not up_salt == salt:
        return obj
    visitor = _m.UserAccount.objects.filter(is_active=True, pk=up_obj_str).first()
    if not visitor:
        return obj
    return visitor


def music_json():
    """
    取出想要的网易云音乐关键信息生成对应的外链信息
    """
    code_base = '<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=100% height=52 src="//music.163.com/outchain/player?type=2&id={}&auto=1&height=32"></iframe>'
    file = open(os.path.join(_st.BASE_DIR, 'docs/music.json'), 'rt', encoding='utf-8')
    musics = json.loads(file.read())['playlist']['tracks']
    new = open(os.path.join(_st.BASE_DIR, 'docs/code.txt'), 'at', encoding='utf-8')
    # 将每一首歌转为正确的格式插入到数据库
    for music in musics:
        name, author, code = music['name'], music['ar'][0]['name'], code_base.format(music['id'])
        new.write('{}-{}||{}\n'.format(author, name, code))
        _m.Music.objects.create(name=name or '未知歌名', author=author or '未知歌手', code=code)
    file.close()
    new.close()
