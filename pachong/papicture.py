from requests_html import HTMLSession
session =HTMLSession()
#拿二傻子为例
headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
response = session.get('http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=二傻子',headers=headers)
#获取我们图片的url的正则匹配格式
img_url_regex = '"thumbURL":"{}",'
#解析并获取图片url_list
img_url_list = response.html.search_all(img_url_regex)
print(img_url_list)
mun=0
for url in img_url_list:
    mun+=1
    #访问图片链接
    response= session.get(url[0])
    #保存二进制并保存至本地
    with open(f'第{mun}张.jpg','wb') as fw:
        fw.write(response.content)


        class BaiDuImg:
            session = HTMLSession()
            img_url_regex = '"thumbURL":"{}",'
            url = ''
            img_url_list = []
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
            }

            def get_search(self):
                search = input('请输入你要搜索的图片')
                self.url = f'http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word={search}'

            def get_img_url_list(self):
                response = self.session.get(self.url, headers=self.headers)
                self.img_url_list = response.html.search_all(self.img_url_regex)

            def save_img(self):
                mun = 0
                for url in self.img_url_list:
                    mun += 1
                    # 访问图片链接
                    response = self.session.get(url[0])
                    # 保存二进制并保存至本地
                    with open(f'第{mun}张.jpg', 'wb') as fw:
                        fw.write(response.content)

            def run(self):
                self.get_search()
                self.get_img_url_list()
                self.save_img()


        if __name__ == '__main__':
            baidu = BaiDuImg()
            baidu.run()