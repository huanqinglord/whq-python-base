#encoding:utf-8

'''
python中对文件的操作通过open方法实现
open(filename, mode)
filename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：
r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
b   以二进制格式打开一个文件
+    open a disk file for updating (reading and writing)
'''
import os
import pickle

from basic_util import getProjectPath

if __name__=="__main__":
    filePath = getProjectPath() + "\\resources\\"
    print("准备测试的文件路径：", filePath)
    fileName = "test.txt"
    print("测试文件名：", fileName)

    openFilePath = filePath + fileName
    #r模式不会新建文件，出现异常
    #No such file or directory
    #file1 = open(openFilePath, "r")

    #print(str(file1))
    print("文件写入")
    file2 = open(openFilePath, "w")
    str1 = "Hello World!"
    file2.write(str1)
    file2.close()

    print("读入文件,read方法")
    file3 = open(openFilePath, "r")
    print(file3.read())
    file3.close()

    print("文件追加")
    file4 = open(openFilePath, "a")
    str2 = '''《登金陵凤凰台》
.[唐].李白.
凤凰台上凤凰游，凤去台空江自流。
吴宫花草埋幽径，晋代衣冠成古丘。
三山半落青天外，二水中分白鹭洲。
总为浮云能蔽日，长安不见使人愁。'''
    file4.write(str2)
    file4.close()

    print("按行读取文件readline方法")
    file5 = open(openFilePath, "r")
    while 1:
        temp = file5.readline()
        print(temp)
        if temp == "" :
            break

    print("返回文件中的所有行，readlines方法")
    #此时光标在文件末尾
    #移动光标到文件头
    #如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
    #from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
    file5.seek(0)
    list1 = file5.readlines()
    for i in list1:
        print(i)

    file5.seek(0)
    print("迭代一个文件对象然后读取每行")
    for line in file5:
        print(line, end="")
    file5.close()

    print("")

    print("文件操作时光标的位置")
    print("查看当前光标的位置tell方法")
    file6 = open(openFilePath, "r")
    print("当前光标位置：", file6.tell())

    print("改变光标的位置")
    #seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    #seek(x,1) ： 表示从当前位置往后移动x个字符
    #seek(-x,2)：表示从文件的结尾往前移动x个字符
    file6.seek(30, 0)
    print("当前光标位置：", file6.tell())
    print(file6.read())
    print(file6.closed)
    file6.close()
    print(file6.closed)
    print("当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件")
    with open(openFilePath, "r") as file7:
        pass
    print(file7.closed)

    '''
    pickle 模块
        python的pickle模块实现了基本的数据序列和反序列化。
        通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
        通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
        基本接口：
        pickle.dump(obj, file, [,protocol])
    '''
    print("pickle 模块")

    dict1 = {"a":1, "b":2}

    openFilePath2 = filePath + "testfunction.py"
    print(openFilePath2)
    file8 = open(openFilePath2, "wb")
    pickle.dump(dict1, file8)
    file8.close()

    print("程序中运行的对象信息保存到文件中去，永久存储成功！")
    print("反序列化")
    file9 = open(openFilePath2, "rb")
    x = pickle.load(file9)
    print(x)
    file9.close()
