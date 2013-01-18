#coding: UTF-8


'''
@license: Apache License 2.0
@version: 0.1
@author: 张淳
@contact: mail@zhang-chun.org
@date: 2012-08-16
'''


from __future__ import print_function
from bs4 import UnicodeDammit
import re
import sys
import hashlib
import datetime


# UTF-8字符集标准命名
UTF8_CHARSET_NAME = 'UTF-8'


# 默认换行符
DEFAULT_NEWLINE = '\n'


def hash(text):
	'''
	生成字符串的哈希值（加简单salt）
	哈希值为“字符串的md5+长度值字符串的md5”的md5

	@param text: 要计算哈希值的文本
	@type text: 字符串

	@return: 十六进制形式的哈希值
	@rtype: 字符串
	'''
	textMD5 = hashlib.md5(text).hexdigest()
	textLengthMD5 = hashlib.md5(str(len(text))).hexdigest()

	return hashlib.md5(textMD5 + textLengthMD5).hexdigest()


def to_unicode(byteSequence):
	'''
	转换字节序列到unicode字符串

	@param byteSequence: 字节序列
	@type byteSequence: py3下为字节串，py2下为str字符串

	@return: unicode字符串
	@rtype: 字符串
	'''
	# 如果已经是unicode则直接返回
	if isinstance(byteSequence, unicode):
		return byteSequence
	else:
		# 尝试从中查找charset的html文本，针对html文本的unicode转换可大幅加速
		charsetPattern = r'''charset\s*=\s*['"]?([-\w\d]+)['"]?'''
		find = re.search(charsetPattern, byteSequence, re.I)
		if find:
			if find.group(1):
				try:
					return byteSequence.decode(find.group(1))
				except Exception as e:
					write_stderr(repr(e))
		# 上述方法均不成功，则使用bs4内置的unicode转换装置
		dammit = UnicodeDammit(byteSequence)
		return dammit.unicode_markup


def unicode_to(unicodeString, charset):
	'''
	转换unicode字符串到字节序列

	@param unicodeString: unicode字符串
	@type unicodeString: 字符串
	@param charset: 希望转换到字节序列的字符集
	@type charset: 字符串

	@return: 字节序列
	@rtype: py3下为字节串，py2下为str字符串
	'''
	if not isinstance(unicodeString, unicode):
		raise TypeError('Parameter "unicodeString" is not unicode type')
	else:
		return unicodeString.encode(charset, 'ignore')


def write_stdout(text):
	'''
	写文本到标准输出

	@param text: 文本
	@type text: 字符串

	@return: 无
	'''
	print(text, file = sys.stdout)


def write_stderr(text):
	'''
	写文本到标准错误输出

	@param text: 文本
	@type text: 字符串

	@return: 无
	'''
	print(text, file = sys.stderr)
