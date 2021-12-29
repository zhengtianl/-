import requests
from typing import List
if __name__ =="__main__":
    #UA伪装：将对应的User-Agent封装搭配一个字典当中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
 
    #处理URL所携带的参数：封装到字典中
    kw = input('enter a word')
    param={
        'query':kw
    }
    #对指定的URL发起的请求时携带参数的，并且请求过程中处理了参数
    response = requests.get(url = url,params = param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')

