import requests
from lxml.html import etree
import os
import re
import json



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36', }
#输出字典形式 歌单名字:url
def musics_name_urls_dict():

    response = requests.get('http://music.taihe.com/',headers= headers)
    response.encoding = 'utf8'
    response_html = etree.HTML(response.text)
    music_xpath = '//*[@id="app"]/div/div[1]/section/section/div/div/div/div/div/h3/a/@href'
    music_name_xpath = '//*[@id="app"]/div/div[1]/section/section/div/div/div/div/div/h3/a/@title'
    music_urls = response_html.xpath(music_xpath)
    music_urls_list = []
    for urls in music_urls:
        music_urls_list.append(f'http://music.taihe.com/{urls}')
    music_name = response_html.xpath(music_name_xpath)
    music_name_urls_zip = zip(music_name,music_urls_list)
    return dict(music_name_urls_zip)

#根据歌单新建歌单名字的文件夹位置放在D:\music\下面,并且把歌单中歌曲的名字和歌曲的url放置在一个txt文本文档中格式为歌名:url
def music_name_urls(musics_name_url_sdict:dict):

    for name,urls in musics_name_url_sdict.items():

        # 创建文件夹music
        if not os.path.exists('D:\\music\\'):
            os.mkdir('D:\\music\\')

        # c创建歌单文件夹
        # 创建歌单时候歌单的名字由字符串,字母,下划线组成
        name = re.sub('\W','',name)
        file_path = os.path.join('D:\\music\\',f'《{name}》')
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        #获取歌单中的歌曲名和url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36', }
        response = requests.get(urls, headers=headers)
        response.encoding = 'utf8'
        response_html = etree.HTML(response.text)
        music_name_xpath = '// *[ @ id = "songList"]/div/ul/li/div[2]/span/a[1]/@title' #歌名
        music_xpath = '// *[ @ id = "songList"]/div/ul/li/div[2]/span/a[1]/@href'  #歌曲链接
        music_singers_xpath  = '//*[@id="songList"]/div/ul/li/div[3]/span/a[1]/@title' #歌手名称
        music_urls = response_html.xpath(music_xpath)
        music_urls_list = []
        for urls in music_urls:
            music_urls_list.append(f'http://music.taihe.com/{urls}')
        music_name = response_html.xpath(music_name_xpath)
        music_singers = response_html.xpath(music_singers_xpath)

        name_url_singers_zip = zip(music_name,music_urls_list,music_singers)
        #写入txt文件
        for name,url,singers in name_url_singers_zip:
            with open(f'{file_path}\\歌名和歌地址.txt','a',encoding='utf8') as fa:
                fa.write(f'{name}-{singers}&{url}\n')
        print(f'{file_path}      歌单生成完毕')

#根据生成的歌单的txt文档我们对TXT文档进行分析,分析后的内容为歌单与其对应的内容歌名+id的一个zip文件
def get_music_name_id():
    catalog = os.listdir('D:\\music\\')
    print(catalog)
    #如果目录没有这个文件
    lis = []   #一个歌单放一个列表中
    for music_lis in catalog:
        music_txt_path = os.path.join('D:\\music\\',music_lis,'歌名和歌地址.txt')

        #读取文件中的歌名+歌手,以及歌曲ID,并组成字典
        with open(music_txt_path,'r',encoding='utf8') as fr:

            dic = {}

            for name_url in fr:
                name_url_list = name_url.strip().split('&')

                #获取歌曲名字,和生成后歌曲的路径

                music_name = name_url_list[0]
                music_file_path = os.path.join('D:\\music\\',music_lis,f'{music_name}.mp3')

                #歌曲的链接
                music_id = name_url_list[1].split('/')[-1]
                dic[music_name] = music_id

            lis.append(dic)
    return zip(catalog,lis)


#歌曲进行下载
def dump_music(zip):
    for music_file,music_name_id_dic in zip:
        file_path = os.path.join('D:\\music\\',music_file)
        for name,id in music_name_id_dic.items():

            url = f'{id}'  #这里是错误滴,正确的在我guilb上,你们自己去瞧瞧哈,好用给颗星星谢谢
            music_file_path = os.path.join(file_path,f'{name}.mp3')

            data = requests.get(url,headers=headers)
            data_text = re.sub('/','',data.text)
            try:
                #获取歌曲URL
                music_url = re.findall('"file_link":(.*?),',data_text)[0]
                music_url = music_url.replace('\\\\','\\')
                music_url = music_url.replace('"','')
                music_url = music_url.replace('http:\\','http:\\\\')
                music_url = music_url.replace('\\','/')


                #下载歌曲
                #获取内容
                response = requests.get(music_url, headers=headers)
                response_data = response.content

                #下载到本地
                with open(music_file_path,'wb') as fw:
                    fw.write(response_data)
                text_path = os.path.join(file_path, '下载成功的歌曲.txt')
                with open(text_path,'a',encoding='utf8') as fa:
                    fa.write(f'歌曲名:{name}\n歌曲ID:{id}\n请求url:{music_url}\n')
                print(name,'下载成功')

            except:
                #可能会存在见状新可以到时候单独进行处理
                print(name,id,'url匹配失败')
                text_path = os.path.join(file_path,'匹配失败歌曲.txt')
                with open(text_path,'a',encoding='utf8') as fa:
                    fa.write(f'歌曲名:{name}\n歌曲ID:{id}\n请求url:{url}\n')


if __name__ == '__main__':
    print('开始')
    #保存文本创建文件夹
    music_name_urls(musics_name_urls_dict())

    #读取文件夹
    dump_music(get_music_name_id())

    #最后文件创建再D盘中