# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:57:06 2020

@author: vinicius
"""

import os
import helper_socket

def readFile(path):
    text = ""
    try:
        f = open(path,'r')
        for line in f:
            text += line
        f.close()
    except FileNotFoundError as e:
        text = "File not found"
    return text

def main():
    con = helper_socket.startSocketServer("127.0.0.1", 50000)    
    nameFile = helper_socket.receivedMessage(con)
    path = "/home/vinicius/"
    print("File: " + nameFile + " search in path -> " + path)

    response = readFile(path + nameFile)
    client = helper_socket.startSocketClient("127.0.0.2", 50000)
    client.send(response.encode())
    print("---- message send to client ----")
    client.close()  
    con.close()    

if __name__ == '__main__':
    main()