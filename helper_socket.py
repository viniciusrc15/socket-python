# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:06:39 2020

@author: vinicius
"""
import socket

def startSocketServer(ip, port):
    print("---- starting server -----")
    address = (ip, port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen(5)
    print("---- awaiting connections -----")
    con, client = server_socket.accept()
    print("---- connect -----")

    return con

def startSocketClient(ip, port):
    print("----- starting connection client -----")
    address = (ip, port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    print("----- connection client up -----")
    return client_socket

def receivedMessage(con):
    received = con.recv(1024)
    message = received.decode("utf-8")
    print("---- received message ----")
    return message