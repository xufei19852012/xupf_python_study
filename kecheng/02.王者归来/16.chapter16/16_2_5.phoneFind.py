import re
msg1 = 'please call me secrtary using 027-81698323'
msg2 = '请明天和我一起参加明志教师晚餐'
msg3 = '请明天和我一起参加明志教师晚餐，电话号码是027-81698334和13260682152'
def findPhoneNum(string):
    pattern=r'\d{3}-\d{8}'
    phoneNum=re.findall(pattern,string)
    print(" 电话号码为：%s" %phoneNum)
findPhoneNum(msg1)
findPhoneNum(msg2)
findPhoneNum(msg3)