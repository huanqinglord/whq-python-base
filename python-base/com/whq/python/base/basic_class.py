#coding:utf-8

#python class
'''
1、单前导下划线
    单个下划线是一个Python命名约定，表示这个名称是供内部使用的。 它通常不由Python解释器强制执行，
    仅仅作为一种对程序员的提示。
2、单末尾下划线
    有时候，一个变量的最合适的名称已经被一个关键字所占用。 因此，像class或def这样的名称不能用作
    Python中的变量名称。 在这种情况下，你可以附加一个下划线来解决命名冲突
3、双前导下划线 __var
    双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。
    这也叫做名称修饰（name mangling） - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
4、双前导和双末尾下划线 _var_
    python特殊用途，平时开发不建议使用
5、单下划线 _
    按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的。
'''
class FirstClass:
    #类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
    #类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
    def __init__(self):
        print("self __init__")
    def print(self, x):
        print(x)

class People:
    name = ""
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __phoneNum = "18710340341"

    #定义构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #定义多个构造函数,通过类方法实现
    @classmethod
    def newPeople(cls):
        c =  cls(cls.name, cls.age)
        c.__phoneNum = "null"
        return c

    def setPhoneNum(self, phoneNum):
        self.__phoneNum = phoneNum
    def getPhoneNum(self):
        return self.__phoneNum

#继承
class Students(People):
    def __init__(self):
        #继承的时候必须调用父类的构造函数
        People.__init__(self, "s", 0)

    def getPhoneNum(self):
        print("我没有电话！")
###################################################
'''
Python同样有限的支持多继承形式。多继承的类定义形如下例:
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''
####################################################

#另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class Sample(Students, Speaker, People):
    #多继承中必须调用所有父类构造函数
    def __init__(self, n, t, a):
        Speaker.__init__(self, n, t)
        People.__init__(self, n, a)
    def getPhoneNumStudent(self):
        super(Students, self).getPhoneNum()

if __name__=="__main__":
    a = FirstClass()
    a.print("a1")

    print("私有属性")
    #与java相同，当定义构造函数的时候，默认的空构造会失效，必须自行定义
    #b = People()
    #print(b.getPhoneNum())

    b1 = People("whq", 1992)
    print(b1.getPhoneNum())

    b2 = People.newPeople()
    print(b2.getPhoneNum())

    s1 = Students()
    print(s1.name)
    #调用子类的方法，子类的方法覆盖了父类的方法
    s1.getPhoneNum()

    c1 = Sample("aa", "tt", 26)
    c1.speak()
    print(1)
    #可以看出在继承中调用父类方法的时候时从左向右的
    print(2)
    print(c1.getPhoneNumStudent())