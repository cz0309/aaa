def jiagongneng(hahahah):  # 这是装饰器名字，，，，，参数是用户，就是给谁装饰，搞个 形参
    def cazuo():  # 这是装饰器真正要干的函数
        print(11111111)
        hahahah()   # 这是用户
        print(22222222)  # 装饰器的功能就   你再这个程序执行前增加打印-----功能
    return cazuo  # 把功能返回出去让它生效，注意和装饰器里面的函数平级调用

# 这种def 包着def的写法又称之为闭包，以后别人家提起来不知道闭包是啥
# 装饰器又称之为语法糖
# @装饰器名  一般这么用，放在函数上生效