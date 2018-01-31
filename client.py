#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 17:56
# @Author  : caelansar
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
import multiprocessing

def clients(datalist):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # build connection:
    s.connect(('127.0.0.1', 8888))
    # receive "welcome" message from server:
    print(s.recv(1024).decode('utf-8'))
    for data in datalist:
        # send data:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=clients, args=([b'caelansar',b'pdd',b'lbw'],))
    p2 = multiprocessing.Process(target=clients, args=([b'cortana',b'light',b'anthoy'],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('connect close')