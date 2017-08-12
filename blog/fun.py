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


# class MyError(Exception):
#     # s = 5
#     pass
#
# try:
#     s = None
#     if s is  None:
#         print ("s 是空对象")
#         #如果引发MyError异常，后面的代码将不能执行
#         raise MyError("附加异常信息")
#     print (len(s))
# except MyError as X:
#     print ("空对象没有长度")
#     print(X.args)

#!/usr/bin/python
#with ...as 函数
# class test():
#     def fun(self):
#         print "44444"
#     def __enter__(self):
#         print("enter....")
#         # return "1"
#     def __exit__(self,type,value,traceback):
#         print("exit...")
#         # return "3"
# a = test()
#
#
# with test() as f:
#     print("doing something")
#     print "================="
#     print f
#     a.fun()

# 链表
class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        self.head = None
    def __getitem__(self, key):
        if self.is_empty():
            print("linklist is empty")
            return
        elif key < 0 or key > self.self.getlength():
            print("the given key is error")
            return
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print("linklist is empty")
            return
        elif key < 0 or key > self.self.getlength():
            print("the given key is error")
            return
        else:
            self.delete(key)
            return self.insert(key)

#链表的初始化
    def initlist(self, data):
        self.head = Node(0)
        p = self.head
        for i in data:
            node = node(i)
            p.next = node
            p = p.next
#遍历链表
    def show(self):
        p = self.head.next
        while p != None:
            print(p.val, " ", end == " ")
            p = p.next
        print ("this is show .")

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False
    def clear(self):
        self.head = None

    def append(self, item):  #在链表尾部增加节点
        p = self.head
        q = Node(item)
        while p.next != None:
            p = p.next
        p.next = q

    def getitem(self, index):     #获取某个位置节点的值
        if self.is_empty():
            print("link is empty")
            return
        i = 0
        p = self.head.next
        while p !=  None and j < index :
            j += 1
            p = p.next
        if p == None:
            print("target is not exist.")
        else:
            return p.val

    def insert(sert, index, item):
        if self.is_empty() or index < 0 or index > self.getlength():
            print ("index is error")
            return
        p = self.head
        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1
        q = Node(item, p)
        q.next = p.next
        p.next = q

#删除某个位置的元素
    def delete(self, index):
        if self.is_empty() or index < 0 or index >self.getlength():
            print ("linklist is empty")
            return
        p = self.head
        j = 0
        while p.next != None and j < index:
            p = p.next
            j += 1
        if p.next == None:
            print ("index is error")
        else:
            p.next = p.next.next

    def index(self,value):  #查找操作，返回相应位置
        if self.is_empty():
            print ("linklist is empty")
            return
        p = self.head.next
        i += 1
        while p != None and not (p.val ==value):
            p = p.next
            i += 1
        if p == None:
            return -1
        else:
            return i
show()
'''
#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        self.head = None

    def __getitem__(self,key):
        if self.is_empty():
            print('linklist is empty')
            return
        elif key < 0 or key > self.self.getlength():
            print('the given key is error')
            return
        else:
            return self.getitem(key)

    def __setitem__(self,key,value):
        if self.is_empty():
            print('link is empty')
            return
        elif key < 0 or key > self.self.getlength():
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key)

# 链表的初始化

    def initlist(self,data):
        self.head = Node(0)

        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

#遍历链表
    def show(self):
        p = self.head.next

        while p != None:
            print(p.val,' ',end = '')
            p = p.next
        print()

# 获取链表长度

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next

        return length

# 判断链表是否为空

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

#清空
    def clear(self):
        self.head = None

#在链表尾部增加节点

    def append(self,item):
        p = self.head
        q = Node(item)
        while p.next != None:
            p = p.next
        p.next = q

#获取某个位置节点的值

    def getitem(self,index):
        if self.is_empty():
            print('link is empty')
            return
        j = 0
        p = self.head.next
        while p != None and j < index:
           j += 1
           p = p.next

        if p == None:
            print('target is not exist')
        else:
            return p.val

# 在某个位置插入节点

    def insert(self,index,item):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('index is error')
            return

        p = self.head
        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1

        q = Node(item,p)
        q.next = p.next
        p.next = q

# 删除某个位置的元素

    def delete(self,index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty')
            return

        p = self.head
        j = 0
        while p.next != None and j < index:
            p = p.next
            j += 1

        if p.next == None:
            print('indes is error')
        else:
            p.next = p.next.next

# 查找操作，返回相应位置

    def index(self,value):
        if self.is_empty():
            print('Linklist is empty')
            return
        p = self.head.next
        i = 0
        while p != None and not (p.val == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else :
            return i
'''
