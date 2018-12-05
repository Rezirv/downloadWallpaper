from selenium import webdriver
import re
import time
import requests
import urllib
import socket
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium.webdriver.chrome.options import Options
import random
import sys
from PIL import Image
from io import StringIO
socket.setdefaulttimeout(40)
wallhavenpath="/media/rezirv/hu/spider/wallhaven/NSFW/"
url ="https://alpha.wallhaven.cc/search?q=&categories=111&purity=001&sorting=views&order=desc&page=1"
proxyes=[{'http':'https://proxy.asec.buptnsrc.com:8001'},{'http':'https://proxy3.asec.buptnsrc.com:8001'}]
proxies=['proxy.asec.buptnsrc.com:8001','proxy3.asec.buptnsrc.com:8001']
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
'Cookie': '__cfduid=d869aee3ba3946562429b114a4727e8271536831391; _pk_ref.1.1f04=%5B%22%22%2C%22%22%2C1543845332%2C%22http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%3A%2F%2Falpha.wallhaven.cc%2F%22%5D; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6ImxKTmNiM0t5K2xBK1pZQ0ladzBmVmNTUjY5OUFjYmdGN0RQazhGOUdVSUU9IiwidmFsdWUiOiJHUDhFRG9vbUtvbDRPQjhUYU1jZitnY3JTalpiRXl2M2x0Nkx5RWVTSkJRdTNReEVHQWJzMWlrUWVjYUtRejlvajVMSTFhQnpkeGI3REdHcXl5UDY5b3NDU3FCclR6QTNadTY3ODU5MzhVMVM5ank0aWM1RGtKVnhqRlBRK2w3TCIsIm1hYyI6ImY1MzAwYWMzYzUyOTQ5NDcxMjFlZmYxZWZiN2I2MGE5NDQyMTIyZTgzYTUzM2RhYmRhMzJiYWZmMWYzZjAxM2YifQ%3D%3D; wallhaven_session=eyJpdiI6IktpNjQ5MDlrbmI2VGZsUTQzYVwvblM0ZHBQMUMwdUdBdW0rWGpUeVg0V0d3PSIsInZhbHVlIjoiam00Znh5azAzUnhsNWpCcW5DOXl1N0VraVlncHVTNmVCcWwydDhoY0pLbG5SaFhvNTJcL2dJZUpacmx1TkRUTHNVRExudldxZVV0emZycFN0cUZCNG5RPT0iLCJtYWMiOiI5MGZmNWJkMmY4YzZkZmExYzkwZDdmNDJjOGU2Mjc4MTNlZmU4OTBiYTMwNzA1NmZmYTg4YjRkMDBjMzIxZWYxIn0%3D; _pk_id.1.1f04=3109da2e1065ea6d.1536831395.18.1543845483.1543845332.',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'https://alpha.wallhaven.cc/search',
'Connection':'close'
}
def _progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading  %.0f%%' % (
            (block_num * block_size) / total_size * 100))
    sys.stdout.flush()
if __name__=='__main__':
    for i in range(45,50):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        p1=random.choice(proxies)
        chrome_options.add_argument("--proxy-server=%s"%('http://'+p1))
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get('https://alpha.wallhaven.cc/search')
        time.sleep(random.randint(1,5))
        login = browser.find_element_by_xpath("//a[@class='button']")
        login.click()
        username = browser.find_element_by_id('username')
        password = browser.find_element_by_id('password')
        loginnow = browser.find_element_by_xpath("//button[@class='button green']")
        username.send_keys("rezirv")
        password.send_keys("chenlei2339")
        time.sleep(random.randint(1,5))
        loginnow.click()
        link=re.sub('page=\d','page=%s'%(i),url,re.S)
        print(link)
        browser.get(link)
        imgs=browser.find_elements_by_class_name("preview")
        for img in imgs:
            toimg=img.get_attribute('href')
            print(toimg)
            p2=random.choice(proxyes)
            request = requests.get(toimg, headers=headers,proxies=p2)
            time.sleep(random.randint(1,5))
            be=BeautifulSoup(request.text,'lxml')
            try:
                imgurl=be.find('img',id='wallpaper')['src']
                thisstar=(be.find_all('a',class_='overlay-anchor')[3]).text
                print(imgurl)
                imgname=imgurl.split('-')[1]
                imgpath=wallhavenpath+thisstar+'星'+imgname
                p3=(random.choice(proxyes))['http']
                proxy_handler = urllib.request.ProxyHandler({
                    'http': 'http://'+p3,
                })
                opener = urllib.request.build_opener(proxy_handler)
                opener.addheaders = [('User-Agent',
                                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'),('Cookie',
                                          '_cfduid=d869aee3ba3946562429b114a4727e8271536831391')
                                        ,('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),('Connection','close')
                                     ,('Upgrade-Insecure-Requests','1')
                                     ]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve('https:'+imgurl, imgpath,_progress)
                # response=requests.post('http:'+imgurl,headers=headers,proxyes=p3)
                # myimg = Image.open(StringIO(response.content))
                # myimg.save(imgpath)
                # myimg.close()
                time.sleep(random.randint(1,5))
                print("下载%s成功,这个%s星"%(imgname,str(thisstar)))
            except BaseException as e:
                print("出现异常"+str(e))
        browser.quit()
