#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 20:14
# @Author  : caelansar
# @Site    : 
# @File    : selectors_server.py
# @Software: PyCharm

import selectors
import socket

sel = selectors.DefaultSelector()


def read(sock):
    data = sock.recv(1024)
    if data:
        print('client message: ', data)
        sock.send(b'hello client')
    else:
        # sock.send(b'')
        print('close', sock)
        sel.unregister(sock)
        sock.close()

def accept(sock):
    conn,addr = sock.accept()
    print('accept', conn)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

sock = socket.socket()
sock.bind(('127.0.0.1', 9999))
sock.listen(5)
sel.register(sock, selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for event, _ in events:
        callback = event.data
        callback(event.fileobj)
