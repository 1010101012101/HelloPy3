import os

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/Users/mc', 'testdir'))
# 然后创建一个目录:
#os.mkdir('/Users/mc/testdir')
# 删掉一个目录:
#os.rmdir('/Users/mc/testdir')

#把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))
#得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))
# 对文件重命名:
#os.rename('test.txt', 'test.py')
# 删掉文件:
#os.remove('test.py')

'''比如我们要列出当前目录下的所有目录'''
print([x for x in os.listdir('.') if os.path.isdir(x)])
'''要列出所有的.py文件，也只需一行代码：'''
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

