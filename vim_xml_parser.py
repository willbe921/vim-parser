from xml.etree import ElementTree
import requests
from xml.etree.ElementTree import parse
import configparser
import json
import socket
import threading

import time
# from requests_oauthlib import OAuth1
from requests.auth import HTTPDigestAuth
# from Logger import Logger
import os

class Vmix_Parser:


    def __init__(self):
        self.ini_filename='setting.ini'
        self.preview_id = -1
        self.active_id = -1
        self.return_dic = {}
        self.load_ini_file()

    def get_query_freq(self):
        conf = configparser.ConfigParser()
        conf.read(self.ini_filename)
        # print(conf.sections())
        self.q_time  = float(conf.get('vmix','time'))
        return self.q_time




    def socket_send(self,send_dic):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.connect((self.socket_server_ip, self.socket_server_port))

        try:       
            #Send
            sock.connect((self.socket_server_ip, self.socket_server_port))    
            # print('send:',send_dic)    
            sock.sendall(json.dumps(send_dic).encode())            
                                 
        except:           
            print('[ERROR]Unix socket send error msg=')
            # self.logger.error('Socket send error msg=' +  str(sys.exc_info()[1]))
        sock.close()


    



    def load_ini_file(self):
        # ini_filename = 'setting.ini'
        conf = configparser.ConfigParser()
        conf.read(self.ini_filename)
        # print(conf.sections())
        self.url  = conf.get('vmix','url')
        self.socket_server_ip = conf.get('socket','ip')
        self.socket_server_port = int(conf.get('socket','port'))
        self.username = conf.get('vmix','username')
        self.password = conf.get('vmix','password')

       
        # print(self.url)



    def get_url_info(self):

        
        
        response = requests.get(self.url, params={"cmd": "getpower"}, auth=(self.username, self.password))
        # print(response)
        xml = response.content
        # print(xml)
        # print(response.content)

        root = ElementTree.fromstring(xml)
        input_video_list = []
        # return_dic  = {}
        



        
        for child in root:
            
            if child.tag =='inputs':
                for i in range(len(child)):
                    # print('name',child[i].text)
                    input_video_list.append(child[i].text)
            if child.tag =='preview':
                self.preview_id= int(child.text)
                # print('preview:',child.text)
            if child.tag =='active':
                self.active_id= int(child.text)
                # print('active:',child.text)


        
        self.return_dic['preview_id']=self.preview_id
        self.return_dic['active_id']=self.active_id
        self.return_dic['video_list']=input_video_list

        socket_thread=threading.Thread(target=self.socket_send(self.return_dic))
        socket_thread.start()
        

        json_rtn = json.dumps(self.return_dic)
        print(json_rtn)
        with open('vmix_id.json','w') as outfile:
            json.dump(self.return_dic,outfile)

        return json_rtn




            
            
    # load_url()


if __name__ == '__main__':
    Vmix_Parser = Vmix_Parser()
    q_time = Vmix_Parser.get_query_freq()
    count = 0
    while True:
        json_rtn=Vmix_Parser.get_url_info()
        print(count)
        
        
        time.sleep(q_time)
        count=count+1
    # print(json_rtn)