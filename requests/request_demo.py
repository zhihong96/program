# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://blog.csdn.net/pleasecallmewhy/article/details/19642329'
URL_GET = 'http://localhost:8000/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>>Response Headers:'
    print response.headers
    print '>>>>>Response Body:'
    print response.text

def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}

    # 发送请求
    response = requests.get(URL_IP, params=params)

    # 处理请求
    print '>>>>>Response Headers:'
    print response.headers
    print '>>>>>Status Code:'
    print response.status_code
    print response.reason
   # print '>>>>>Response Body:'
   # print response.json()

if __name__ == '__main__':
    print '>>>>>Use simple requests:'
    use_simple_requests()
    print 
    print '>>>>>Use params requests:'
    use_params_requests()
