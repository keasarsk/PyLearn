 # 七月十六
 # Django框架
 #
 # -----------------------------笔记：
 # 开源的Web应用框架
 # 采用MVC设计模式
 # 1) 强大的数据库功能：用python的类继承，几行代码就可以拥有一个动态的数据库操作API，如果需要也能执行SQL语句。
 # 2) 自带的强大的后台功能：几行代码就让网站拥有一个强大的后台，轻松管理内容。
 # 3) 优雅的网址：用正则匹配网址，传递到对应函数。
 # 4) 模板系统：强大，易扩展的模板系统，设计简易，代码和样式分开设计，更易管理。
 # 5) 缓存系统：与memcached或其它缓存系统联用，表现更出色，加载速度更快。
 # 6) 国际化：完全支持多语言应用，允许你定义翻译的字符，轻松翻译成不同国家的语言。

 # 安装 pip3 install django

 # 在当前路径下生成django网站
 # django-admin startproject 文件名

 # settings.py  django的配置文件
 # url.py       存URL与函数的对应关系---路由系统
 # wsgi.py      调用python的内置模块wsgiref
 #      wsgi（web服务网关接口）也是一个协议(协议：按照规则实现socket)
 #      wsgiref就是实现wsgi协议的
 # manage.py    对网站的管理,对当前django程序所有的操作： python manage.py 命令名称比如runserver

 # cd 文件名
 # 启动并监听8080端口
 # python manage.py runserver 127.0.0:8080
 # python manage.py runserver  默认监听8000端口
