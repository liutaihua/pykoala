[介绍]
pykoala是一个简单、小巧、快速的“网络爬虫模块”。
虽然真实世界中的“考拉”是一种行动缓慢的可爱生物，但这个pykoala速度很快，同时非常易于使用。
pykoala可以轻松地嵌入到你需要使用爬虫的地方。下面展示一些基本用法：

# 最简单的用法
>>> from pykoala import Koala
>>> koalaBaby = Koala.Koala('http://www.cnbeta.com/')
>>> for url in koalaBaby.go():
...   print url

# 设置爬虫深度，默认为10
>>> from pykoala import Koala
>>> koalaBaby = Koala.Koala('http://www.cnbeta.com/')
>>> for url in koalaBaby.go(maxDepth = 5):
...   print url

# 只允许进入www.cnbeta.com/articles/这样的URL中，并只抓取URL以.htm和.jp(e)g结尾的URL
>>> entryFilter = dict()
>>> entryFilter['Type'] = 'allow'
>>> entryFilter['List'] = [r'www\.cnbeta\.com/articles/', ]
>>> yieldFilter = dict()
>>> yieldFilter['Type'] = 'allow'
>>> yieldFilter['List'] = [r'\.htm$', r'\.jpe?g$']

>>> from pykoala import Koala
>>> koalaBaby = Koala.Koala('http://www.cnbeta.com/', entryFilter, yieldFilter)
>>> for url in koalaBaby.go():
...   print url

# 只允许抓取不以mailto:开头的URL
>>> yFilter = dict()
>>> yFilter['Type'] = 'deny'
>>> yFilter['List'] = [r'^mailto:', ]

>>> from pykoala import Koala
>>> koalaBaby = Koala.Koala('http://www.cnbeta.com/', yieldFilter = yFilter)
>>> for url in koalaBaby.go():
...   print url

更多用法请参见文档。


[最后]
项目主页：http://code.google.com/p/pykoala/
如果你有使用问题、报bug、意见建议、共同开发……请联系我：mail@zhang-chun.org
希望你喜欢这只小考拉！
