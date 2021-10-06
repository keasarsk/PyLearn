# tuple1 = ('abcd',89,9.12,'peter',[11,22,33])
# print(id(tuple1))
# print(tuple1)


# import copy
# dictA={"pro":'艺术','shcool':'北京电影学院'}
# dictB=copy.copy(dictA) #浅拷贝
# dictC=copy.deepcopy(dictA) #深拷贝
# print(id(dictA))
# print(dictB)
# print(id(dictB))
# print(dictC)
# print(id(dictC))

# li=[2,45,1,67,23,10] #原始对象
# li.sort() #list的排序方法 直接修改的原始对象
# # print(li)
# varRs=sorted(li,reverse=True)
# print(varRs)

# s1=['a','b','c']
# s2=['你','我','c他','peter']
# s3=['你','我','c他','哈哈','呵呵']
# print(list(zip(s1))) # 压缩一个数据

# dicObj={}
# dicObj['name']='李易峰'
# dicObj['hobby']='唱歌'
# dicObj['pro']='艺术设计'
# print(dicObj)
#
# for item in enumerate(dicObj):
#     print(item)

import psutil# 获取系统信息的第三方模块
import os
import gc# 垃圾回收机制模块

# print(gc.get_threshold())# 返回当前集合阈值。

pid=os.getpid()# 返回当前进程id
p=psutil.Process(pid)
print(p)