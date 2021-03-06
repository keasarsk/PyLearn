# 局部变量 就是在函数内部定义的变量【作用域仅仅局限在函数的内部】
# 不同的函数 可以定义相同的局部变量，但是各自用各自的 不会产生影响
# 局部变量的作用：为了临时的保存数据 需要在函数中定义来进行存储
# ------------全局变量----------------
# pro的定义就是一个全局变量【作用域的范围不同】
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的变量【地头蛇】
#如果在函数的内部要想对全局变量进行修改的话 必须在上一行使用global 关键字对全局变量进行声明

# 以下两个是全部变量
pro='计算机信息管理'
name='吴老师'
def printInfo():
    # name='peter' #局部变量
    print('{}.{}'.format(name,pro))
    pass
def TestMethod():
    name='刘德华'
    print(name,pro)
    pass
def changeGlobal():
    '''
    要修改全局变量
    :return:
    '''
    global pro #声明全局变量 后才可以修改
    pro='市场营销' #局部变量
    pass

changeGlobal()
print(pro) #被修改了吗
TestMethod()
printInfo()