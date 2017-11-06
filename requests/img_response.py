# -*- coding: utf-8 -*-

import requests

def download_image():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36'}
    url = 'https://siliconangle.com/files/2012/03/github_logo.jpg'
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpg', 'wb') as f:
       # chunk = response.content
        for chunk in response.iter_content(128):
            f.write(chunk)
            f.close()

def download_image_improved():
    # headers 
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36'}
    url = 'https://siliconangle.com/files/2012/03/github_logo.jpg'
    response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__=='__main__':
    download_image_improved()
