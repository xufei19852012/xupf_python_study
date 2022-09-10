'''
import re
import requests
response = requests.get('http://baijiahao.baidu.com/s?id=1598724756013298998&wfr=spider&for=pc')
data = response.text
#print(data)


new_list = re.findall('<spanclass="bjh-p">(.*?)</span></p> <p>', data)
print(new_list)
for a in new_list:

    with open(r'D:\text\duanzi.txt','a') as fw:

        fw.write(a)
        fw.flush()
'''
# http://baijiahao.baidu.com/s?id=1598724756013298998&wfr=spider&for=pc  段子所在的网址
import re
import requests  # 如果没这模块运行CMD pip  install requests

# UA伪装请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chromeh/81.0.4044.138 Safari/537.36'
}
URL_addr = 'https://blog.csdn.net/m0_47419053/article/details/126119390?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-126119390-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-126119390-null-null.nonecase'

#URL_addr = 'https://blog.csdn.net/csdnnews/article/details/126416530?spm=1000.2115.3001.5927'
response = requests.get(url= URL_addr,headers= header )  # 这个编辑器的长度关系没法放一行
'''
playfile  = open('xufei.txt','wb')
for chunk in response.iter_content(20000):
    playfile.write(chunk)
'''




# 按F12选择自己想要的内容所在的位置copy出来
#res = response.text.encode('utf-8')
data = response.text
new_list = re.findall('<p>(.*?)</p>', data)  # (.*?)是我们要的内容

print(new_list[0:1500])

for a in new_list:
    with open(r'D:\text\duanzi.txt', 'a') as fw:
        fw.write(a)
        fw.flush()

