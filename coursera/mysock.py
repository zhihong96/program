# -*- coding: utf-8 -*-

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.github.com',80))
cmd = 'GET https://gist.github.com/kevinkindom/108ffd675cb9253f8f71\n\n' # p3 add .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        break
    print data   #python3 add .decode()

mysock.close()
