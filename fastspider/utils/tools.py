# encoding=utf-8

import time

from fastspider.settings import common


def key_to_hump(key):
	"""
		将变量转化为驼峰命名
	:return: 返回驼峰命名变量
	"""
	return key.lower().title().replace("_", "")


def check_class_method(obj, name):
	"""
		检查对象是否有某个属性
	:return:
	"""
	try:
		return getattr(obj, str(name))
	except Exception as e:
		print(f"对象{obj} 没有方法{str(name)}")
		return None


def get_tunnel_proxy():
	try:
		if common.PROXY_ENABLE:
			proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
				"host": common.PROXY_TUNNEL_HOST,
				"port": common.PROXY_TUNNEL_PORT,
				"user": common.PROXY_TUNNEL_USER,
				"pass": common.PROXY_TUNNEL_PASSWORD,
			}
			proxies = {
				"http": proxy_meta,
				"https": proxy_meta,
			}
			return proxies
		return None
	except Exception as e:
		return None


def sleep_time(times):
	"""
		休眠指定时间
	:param times: 秒
	"""
	time.sleep(times)


class Singleton(object):
	def __init__(self, cls):
		self._cls = cls
		self._instance = {}

	def __call__(self, *args, **kwargs):
		if self._cls not in self._instance:
			self._instance[self._cls] = self._cls(*args, **kwargs)
		return self._instance[self._cls]


def cookies2dict(cookies):
	cookie_dict = {}
	for i in cookies.split(";"):
		cookie = i.split("=")
		cookie_dict[cookie[0]] = cookie[1]
	return cookie_dict
