
##################################################################################################
#########################################第18章 GUI自动化控制######################################
##################################################################################################
'''
import pyautogui,time
time.sleep(5)
pyautogui.click()
distance = 200
while distance>0:
    pyautogui.dragRel(distance,0,duration=0.2)
    distance = distance -5
    pyautogui.dragRel(0,distance,duration=0.2)
    pyautogui.dragRel(-distance,0,duration=0.2)
    distance=distance-5
    pyautogui.dragRel(0,-distance,duration=0.2)
'''
'''
S = 
exam:18.5
import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())
w,h=pyautogui.size()
print(w)
print(h)

mm='w:'+ str(w)+'\n'+''+'h:'+str(h).rjust(4)
#print(mm)

w,h=pyautogui.position()S
print(w)S
print(h)
pyautogui.click(1893,6)
'''
##################################################################################################
#########################################第11章 从web抓取信息#######################################
##################################################################################################
'''
#example 11.3
import requests
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
#print(res.text[:98660000])
'''
'''
#example 11.2.1
res=requests.get('http://e.xstt5.com/e/DownSys/doaction.php?enews=DownSoft&classid=4&id=889&pathid=0&pass=ef534c12904aba4acd8f618960738593&p=:::')
res.raise_for_status()
print(res.raise_for_status())
type(res)
print(len(res.text))
playFile = open('shediaoyinxiongzhuang.txt','wb')
import webbrowser,sys, = pyperclip.paste()
webbrowser.open(address)
'''
'''
#example 11.1
import webbrowser,sys
if len(sys.argv) >1:pyperclip
address
    address = ''.join(sys.argv[1:])
    webbrowser.open(address)
#webbrowser.open('www.baidu.com')

'''

##################################################################################################

#############################################第10章 调试##########################################
##################################################################################################

'''
print('first')

first = input()
print('second')
second = input()

print('third')
third=input()
print('the sum is'+first+second+third)
'''
'''
#10.4.3:调试当中日志文件的使用方法
import logging
logging.basicConfig(filename='xufei.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
#logging.disable(logging.DEBUG)
logging.debug('\n some debugging details')
logging.info('some info details')
logging.warning('some waring')
logging.error('some error info')
logging.critical('some critical info')
'''
'''
#文件的相关操作内容
import os
mm = os.getcwd()
print(mm)
os.chdir('d:\\')
mm = os.getcwd()
print(mm)
#os.mkdir('xufei\weiwen')
os.chdir('d:\\xufei\\weiwen')
print(os.path.abspath('.'))
print(os.path.isabs('.'))
#print(os.path.isabs(os.path.isabs('.')))

path = 'D:\\xufei\\weiwen\\xu.txt'
path2 = 'D:\\ANHUI\\NANLING\\JIAFA'
#print(os.path.basename(path))
#print(os.path.dirname(path))
#print(os.path.split(path))
print(os.path.split(os.path.sep))
print(os.path.getsize(path))
totalsize = 0
for filename in os.listdir('c:\\windows\\system32'):
    totalsize = totalsize + os.path.getsize(os.path.join('c:\\windows\\system32',filename))
print(totalsize)
print(os.path.exists(path))
print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.getcwd())
os.chdir('d:\\')
if (os.path.exists(path2) == 'True'):
    os.mkdir(path2)
else:
    print('you already make this dir')
print('01------------------------------------------------')
filename = 'D:\\xufei\\weiwen\\xu.txt'
fileC= open(filename,'a')
xx = fileC.write('\nbao bao s name')
fileC.close()
'''
#yy = fileC.readlines()
#print(xx)
#print(yy)
'''
#目录的相关的操作
import os
myFile=['xu.txt','fei.txt','wei.txt']
pathVal = os.path.join('xu','wei','yang')
print(pathVal)
print(os.path.join('xu','wei','yang'))
for item in myFile:
   print(os.path.join('C:\\',item)) 
'''
'''
#类及对象的使用方法
class myClass:
    def __init__(self,name,age):
p1 = myClass("xufei",23)

        self.name = name
p1.myFun()
'''
'''
        self.age=age

    def myFun(self):
        print("hello my nmae is "+self.name)

print(p1.name)
print(p1.age)
'''
'''
#数组的使用方法
cars = ['xufei','weiwen','xuzhi']
print(cars[1])
cars[0]='baobao'
print(cars[0])
print(len(cars))
cars.append("huihui")
cars.pop(0)
for x in cars:
    print(x)
'''
'''
#lambda函数的使用
x = lambda a:a+10
y= lambda a,b,c:a*b*c
print(x(5))
print(y(2,3,4))
'''
'''
#写一个文件并显示，或删除相关的文件
import os
f = open('xufei.txt',"a")
f.write("xufei 's four line")
f.close()

f = open('xufei.txt',"r")
for x in f:
    print(x)
f.close()
if os.path.exists("xufei.txt"):
    print("the directory have a txt file")
#os.remove("xufei.txt")
'''
'''
#读取所有行的内容
f = open('xufei.txt',"r")
for x in f:
    print(x)
'''
'''
#读取一txt文件里的内容
f = open('xufei.txt',"r")
print(f.read())
'''

'''
#压缩一个文件到一个压缩的文件当中
import zipfile,os
os.chdir('D:\\')
newzip = zipfile.ZipFile('xu.zip','w')
newzip.write('weiwen.txt',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()
'''

'''
#解压一个压缩文件
import zipfile,os
os.chdir('D:\\')
examplefile = zipfile.ZipFile('xufei.zip')
examplefile.extractall()
examplefile.close()
'''


'''
#获取一个压缩文件，并获取相关的信息
import zipfile,os
os.chdir('D:\\')
examplezip = zipfile.ZipFile('xufei.zip')
print(examplezip.namelist())
xinfo = examplezip.getinfo('xufei/clr.txt')
print(xinfo.file_size)
print(xinfo.compress_size)
examplezip.close()
'''

'''
复制/移动一个文件及相关目录
import shutil , os
os.chdir('C:\\')
#shutil.copy('xufei1.txt','C:\\xufei')
#shutil.copy('xufei1.txt','C:\\xufei\\xufei1.txt')
#shutil.copytree('C:\\xufei','C:\\weiwenback')
#shutil.move('C:\\xufei1.txt','C:\\weiwen')
#shutil.rmtree('C:\\weiwen')
shutil.rmtree('C:\\xufei')
'''

'''
#未通过
#上述代码可以获取当前目录下的所有文件
import glob
for file in glob.glob('C:\Cadence\SPB_16.6\*',recursive=True):
	print(file)
'''

'''
#未通过
#用于拷贝一个文件从一个目录到另一个目录
import shutil
shutil.move(r' .\exam01.py' , r'.\c:\')
'''
'''
#通过
#打开当前绝对路径下的所有文件及其文件夹
import os
path = 'C:\Cadence\SPB_16.6'
for filename in os.listdir(path):
    print(filename)
'''
'''
#通过
#通过搜索可以查轮寻查到所有文件的名称及其路径
import os
path = 'C:\Cadence\SPB_16.6'
for filename in os.scandir(path):
    print(filename.name,filename.path)
'''
'''
#通过
#通过下面的函数可以重命名文件名或文件夹的方式 
import os
os.rename('exam01.py','exam01_rename.py')
#os.rename('文件夹1','文件夹2')
'''
'''
#通过
#在当前目录下判断没有如下目录，就自动创建一个
import os
#通过
#在当前路径下加一个文件夹，并打印出整个文件路径
import os
desktop_path = os.path.join(os.path.expanduser("~"),'desktop')
print(desktop_path)
'''
''' dirname:
        print(dirname)
    if dirpath:
        print(dirpath)
pathdir='xufei'
if not os.path.exists(pathdir):
    os.makedirs(pathdir)
'''
'''
#通过
#遍历当前目录下所有文件夹及文件的名称，并全部打印出来；
import os
for dirname,dirpath,filename in 机备份\C300\driver'):
    if filename:os.walk(r'F:\自建虚拟
        print(filename)
    print('-'*100)
'''
'''
import os
print("xufei")
'''

