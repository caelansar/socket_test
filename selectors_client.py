#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 17:23
# @Author  : caelansar
# @Site    : 
# @File    : selectors_client.py
# @Software: PyCharm
import random
import socket
import selectors

sel = selectors.DefaultSelector()  # 整个监控机制


def read(sock):
    recv_data = sock.recv(1024)
    if not recv_data:
        sel.unregister(sock)
        sock.close()
        return
    print(b'received %s' %recv_data)


def write(sock):
    '''
    callback function
    :return:
    '''
    sock.send(str(random.randint(0,66)).encode())
    sel.unregister(sock)  # 取消对可写的注册
    sel.register(sock, selectors.EVENT_READ, read)

for i in range(10):  # 10个客户端
    client = socket.socket()
    sel.register(client, selectors.EVENT_WRITE, write)
    client.connect(('127.0.0.1', 9999))  # 建立连接， 此时还不一定可写

while True: # 检查事件是否发生，发生就回调
    for event, _ in sel.select():
        sock = event.fileobj
        callback = event.data
        callback(sock)


