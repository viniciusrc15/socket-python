# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:06:39 2020

@author: vinicius
"""
import os
import helper_socket

def main():
    clientSocket = helper_socket.startSocketClient("127.0.0.1", 50000)
    nameFile = input("Type name of file: ")
    clientSocket.send(nameFile.encode())
    print("---- message send to client ----")
    
    con = helper_socket.startSocketServer("127.0.0.2", 50000)   
    response = helper_socket.receivedMessage(con)
    file = open("fileWrite.txt", "w")
    file.write(response)
    
    con.close()
    clientSocket.close()

if __name__ == '__main__':
    main()
