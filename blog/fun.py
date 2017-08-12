#!/usr/bin/python
#coding=utf-8
#非局部变量

# def fun_out():
#     a = 4
#     def fun_in():
#         nonlocal a     # nonlocal 是Python3中新增的
#         a += 1
#     fun_in()
#     print (a)
# fun_out()


#闭包
# def out():
#     a = 1
#     print a
#     def inner():
#         print a+1
#         print "I'm inner"
#     return inner
#
# f = out()
# f()
#
# def func(name):
#     def inner_func(age):
#         print 'name:', name, 'age:', age
#     return inner_func
#
# b = func('the 5 fire')
# b(26)
# #
# #装饰器
# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
# @makebold
# @makeitalic
#
# def hello():
#     return "hello world"
#
# print hello()
#
# #匿名函数  lambda是一个表达式而不是一个语句，它返回一个函数对象
# L = [lambda x: x ** 2,
#      lambda x: x + 3,
#      lambda x: x * 4]
#
# for f in L:
#     print(f(2))
#==================================
# coding=utf-8

# class TestStaticMethod(object):
#     @staticmethod
#     def foo():
#         print "calling static method foo()"
#
#     # foo = staticmethod(foo)
#
# class Child(TestStaticMethod):
#     pass
#
# static = TestStaticMethod()
#
# static.foo()
# TestStaticMethod.foo()
#
#
# child = Child()
#
# child.foo()
#
# print "==============================================="
# class TestClassMethod(object):
#     @classmethod
#     def foo(cls):
#         print "calling class method foo()"
#         print cls.__name__
#
# class Child1(TestClassMethod):
#     pass
#
# cls = TestClassMethod()
#
# cls.foo()
# TestClassMethod.foo()
#
#
# child = Child1()
#
# child.foo()


#!/usr/bin/python
#
# class TestStaticMethod:
#     def foo():
#         print("calling static method foo()")
#
#     foo = staticmethod(foo)
#
# class TestClassMethod:
#     def foo(cls):
#         print("calling class method foo()")
#         print("class",cls.__name__)
#
#     foo = classmethod(foo)
#
# TestStaticMethod.foo()
# TestClassMethod.foo()
# print "++++++++++++++++++++++++++++++++++++++++"
# #!/usr/bin/python
#
# class Person(object):
#     def __init__(self):
#         self.height = 165
#
#     def about(self,name):
#         print "{} is about {}".format(name,self.height)
#
# class Girl(Person):
#     def __init__(self):
#         self.weight = 98
#         super(Girl,self).__init__()
#
#     def about(self,name):
#         print "{} is a girl,she is about {} and her weight is {}".format(name,self.height,self.weight)
#         super(Girl,self).about(name)
#
#
# Chan = Girl()
# Chan.about("DiaoChan")
#
# super(Girl,Chan).about("Zhenfu")
# #super第一个参数是子类的类名，第二个是self或者子类生成的一个对象，然后是点 . ,然后是父类的方法，括号里加上参数。
# print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#
#
# #!/usr/bin/python
#
# class Parent(object):
#     def __init__(self):
#         self.job = "teacher"
#         self.__name = 'cainiao'
#         self.__score = 60
#
#     def name(self,n):
#         if n == 1:
#             return self.__name,1
#         else:
#             return "sorry",2
#
#     def getName(self):
#         return self.__name,3
#
#     def setName(self,score):
#         print "score is ...",4
#         if score > 100 or score < 0:
#             print "score is ",5
#             self.__score = 0
#             return "score is None",6
#         else:
#             print "score +++",7
#             self.__score = score
#             print self.__score,'aaa',8     # 若直接打印，则由于此处已经向终端输出，则在第194行再次打印时会输出打印None，
#             return self.__score,'aaa',9    # 但若是将该值return，则可以在194行输出打印该字段
# class Child(Parent):
#     pass
# # c = Child()
# #
# # print c.__name
# p = Child()
# print p.job
# print p.name(1)
# print p.getName(),"55555"
# print  "55555555555555555555555"
# print p.setName(70)   #调用的是 8 ，
#
# print "==============================="

# class Protect:
#     def __init__(self):
#         self.job = 'teacher'
#         self.__name = 'cainiao'
#
#     def __python(self):
#         print('I love python')
#
#     def code(self):
#         print("Which language do you like")
#         self.__python()
#
# if __name__ == '__main__':
#     p = Protect()
#     print(p.job)
# #    print(p.__name)
#     p.code()
# #    p.__python()

# #魔法方法和属性
# class A(object):
#     def __getattr__(self,name):
#         print name
#         print("you use getaddr")
#     def __setattr__(self,name,value):
#         print name, value
#         print ("you use setattr")
#         self.__dict__[name] = value
#     pass
#
# a = A()
# print a.x    #  a.x的作用：初始化，这样才能调用__getattr__()函数
# a.x = 7
# print (a.x)
# print (a.__dict__)


#迭代器   range也是一种迭代器

#计算机对一组指令（或一定步骤）进行重复执行，在每次执行这组指令（或这些步骤）时，
#都从变量的原值推出它的一个新值。
# class TestIter:
#     def __iter__(self):
#         print("__iter__")
#         return self
#
#     def __init__(self,a):
#         print ("__init__")
#         self.a = a
#
#     def __next__(self):          # a.__next__() 是Python3才有的魔法方法
#         print("__next__")
#         self.a += 1
#         return self.a ** 2
#
# a = TestIter(2)
# print ("-----------")
# print (next(a))   #输出为 9
# print ("===========")
# print (a.__next__())  #输出为16
#
# #生成器   生成器是一次生成一个值的特殊类型函数。可以将其视为可恢复函数。
# def fib(max):     #斐波那契数列
#     a,b = 0,1
#     while a < max :
#         yield a      # yield返回原数，
#         a,b = b, a + b #a,b交换
# for i in fib(20):
#     print (i)

class MyError(Exception):
    # s = 5
    pass

try:
    s = None
    if s is  None:
        print ("s 是空对象")
        #如果引发MyError异常，后面的代码将不能执行
        raise MyError("附加异常信息")
    print (len(s))
except MyError as X:
    print ("空对象没有长度")
    print(X.args)
