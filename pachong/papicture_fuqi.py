import requests
import os
from lxml import etree

# 创建文件夹
try:
    os.mkdir('./fuqi图片爬取')
except Exception:
    print('文件已创建！')

for i in range(1, 296):
    i = str(i)
    # 目录页面
    ml_url = 'http://www.69park5.info/category/125-' + i + '.html'
    print(ml_url)
    # UA伪装请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chromeh/81.0.4044.138 Safari/537.36'
    }

    response = requests.get(url=ml_url, headers=header)
   # print(ml_url)
    # 通用处理中文乱码的解决方法
    res = response.text.encode('utf-8')
    treee = etree.HTML(res)
    t = treee.xpath('//div[@class="pink-border content"]')
    for tu in t:
        http = 'http://www.69park5.info/'
        # 标题
        tit = tu.xpath('./div/a/img/@alt')[0]
        print(tit)

        hrefUarl = tu.xpath('./div/a/@href')[0]
        print('hrefUarl is ',hrefUarl)

        # 地址
        tp  = tu.xpath('./div/a/img/@src')[0]
        img = requests.get(url=tp, headers=header).content

        imgpath = './fuqi图片爬取/' + tit + '.jpg'

        with open(imgpath, 'wb') as fp:
            # 传入二进制内容
            fp.write(img)

            print(tit, '下载成功！')

##  http://www.69park5.info/category/125-3.html   // 125-1~296
   ##  http://www.69park5.info/album/126162.html
       ##  http://www.69park5.info/album/126162/6iD75Sob14973e7a1930b949eb9c8f7eeaf553c0.html
       ##  http://www.69park5.info/album/126162/W2PKJc7r8aaddba9ce8493c48f590d462707a8b6.html
       ##  http://www.69park5.info/album/126162/Ejq4UCu8d1099d84031276df0379db767e6ac048.html
   ## http://www.69park5.info/album/126103.html
      ## http://www.69park5.info/album/126103/laULCFGwcefed922d034d2b60935ae9a2c4ea553.html
      ## http://www.69park5.info/album/126103/Vui7hG4bdf9b2c98000f52d9209a59abf85b2cb4.html

    ##首页 >> 会员相册 >> 夫妻相册

