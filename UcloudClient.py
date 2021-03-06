#!/usr/bin/env python3

import sys
#import make_signature_2 
import urllib.parse
import credit_configure
import server.server_tools as server_tools 
import art
UCLOUD_API_URLS={
    'server' : 'https://api.ucloudbiz.olleh.com/server/v1/client/api',
    'loadbalancer'     : 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api',
    'waf'    : 'https://api.ucloudbiz.olleh.com/waf/v1/client/api',
    'watch'  : 'https://api.ucloudbiz.olleh.com/watch/v1/client/api',
    'package': 'https://api.ucloudbiz.olleh.com/packaging/v1/client/api',
    'autoscaling'     : 'https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api',
    'cdn'    : 'https://api.ucloudbiz.olleh.com/cdn/v1/client/api',
    'msg'    : 'https://api.ucloudbiz.olleh.com/messaging/v1/client/api',
    'nas'    : 'https://api.ucloudbiz.olleh.com/nas/v1/client/api',
    'db'     : 'https://api.ucloudbiz.olleh.com/db/v1/client/api',
}
    # try:
    #         file = open("credit.txt","r")
    # except:
    #         print("no credit file detected \nplease type 'ucloud configure init' to create credit files")
    #         exit(-1)
#Command_List = ["configure","ListAvailableProductTypes","delpoyVirtualMachine","startVirtualMachine","listVirtualMachines","listVirtualMachineForCharge"]
Ctype_List = ["help","configure","server"]
ctype = ""
command = ""
def main():
    cnt = 0
    parameters = []
   # print(sys.argv[1])
   
    if len(sys.argv) < 3 :

##        if(sys.argv[1] == Command_List[0]):
##            configure()
##            ctype = sys.argv[1]
##        elif(sys.argv[1] == Command_List[1]):
##            ListAvailableProductTypes()
##        else:
        if(len(sys.argv) == 1):
            Art  = art.text2art("KT",font="black")
            print(Art)
            Art  = art.text2art("UCLOUD",font="black")
            print(Art)
            print(" ")
            print ("usage: ucloud [type] [command] [parameters] \nor type 'ucloud help'")

        elif(len(sys.argv) == 2):
            if(sys.argv[1] == "help"):
                ctype_process("help","",parameters)
            else:
                print ("usage: ucloud [type] [command] [parameters] \nor type 'ucloud help'")
                exit(-1)
        else:
            print ("usage: ucloud [type] [command] [parameters] \nor type 'ucloud help'")
            exit(-1)
    else:
        ctype = sys.argv[1]
        command = ""
        if(ctype != "help"):
            command = sys.argv[2]
        for c in Ctype_List:
            if (c == sys.argv[1]):
                ctype = c
                cnt+=1
                break
        if(cnt == 0):
            print("unable to process type: ",ctype,"\n type 'ucloud help' to view supported type")
            exit(-1)
        for i in range(3,len(sys.argv)):
            parameters.append(sys.argv[i])
            
        ctype_process(ctype,command,parameters)      


    #signature = sig.sign_request_url(ZONE)

def ctype_process(ctype,command,parameters):
    
    if ctype == "configure":
        c = credit_configure.configure(command)
        c.command_process_configure()
    elif ctype == "server":
        s = server_tools.server(command,parameters)
        s.execute()        
    elif ctype =="help":
        print("============[type] list============ ")
        for i in Ctype_List:
            print(i)
        
        
main()
