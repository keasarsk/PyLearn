# Http: 连接 无状态，短链接
#
# 浏览器（socket 客户端）
# 网站（socket服务端）

# 自己写网站
#   a。socket服务器
#   b。根据URL不同返回不同的内容
#       路由系统：
#           URL->函数
#   c。字符串返回给用户
#       模板引擎渲染：
#           HTML充当模板（特殊字符）
#           自己创造任意数据
#       字符串

# Web框架
#   框架种类：
#       - a,b,c                    -->！Tornado！
#       - [第三方a],b,c            -->oython的wsgiref模块-->！Django！
#       - [第三方a],b,[第三方c]    -->flask

#   分类：
#       Django框架
#       其他框架