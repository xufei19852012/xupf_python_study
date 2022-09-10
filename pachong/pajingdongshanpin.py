from requests_html import HTMLSession
session = HTMLSession()
page=1
while True:
    res =session.get(f'https://search.jd.com/Search?keyword=苹果8&enc=utf-8&page={page*2-1}')  #keyword搜索内容 #enc编码格式 #8page页数*2-1
    res.html.encoding='utf8'
    info_list=res.html.xpath('//*[@class="gl-i-wrap"]')
    if not info_list:
        print(f'一共爬取{page}页')
        break
    print(f'url={res.url}第{page}页',[info.text for info  in info_list])
    page+=1