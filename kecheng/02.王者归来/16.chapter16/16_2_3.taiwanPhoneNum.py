import re
msg1 = 'please call me secrtary using 027-81698323'
msg2 = '请明天和我一起参加明志教师晚餐'
msg3 = '请明天和我一起参加明志教师晚餐，电话号码是027-81698334和13260682152'
def parsestring(string):
    phoneRule = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d')
    phoneNum =  phoneRule.search(string)
    if phoneNum != None:
        print("电话号码是：%s" % phoneNum.group())
    else:
        print("%s字符串不含电话号码为：" % string)

parsestring(msg1)
parsestring(msg2)
parsestring(msg3)