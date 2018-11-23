#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import argparse
import clr.clr as clr
import pysmb

#======CLR IMPORT=====================
cg = clr.colors.fg.green
cr = clr.colors.fg.red
cw = clr.colors.fg.lightgrey
tt = clr.colors.fg.purple + clr.colors.bold
cb = clr.colors.bold
c = clr.colors.reset
ok = cw+"["+cg+cb+"+"+c+cw+"]"+cw
err = cw+"["+cr+cb+"-"+c+cw+"]"+cw
ast = cw+"["+tt+"*"+c+cw+"]"+cw
#========CLR IMPORT CLOSED==================

# Constantes

parser = argparse.ArgumentParser(description='Test access to samba server')
parser.add_argument('--port', type=int, default='445', help='Port to connect. Default is 445')
parser.add_argument('-u', '--Username', type=str, default='Guest', help='Username. Default is Guest')
parser.add_argument('-p', '--Password', type=str, default='passwd', help='Password. Default is "passwd"')
parser.add_argument('-i', '--Ip', type=str, required=True, help='server ip. example: 192.168.0.1')
parser.add_argument('-n', '--Name', type=str, required=True, help='server name. example: 192.168.0.1//NAME')
parser.add_argument('-f', '--Sharename', type=str, help='Set the folders to test.')
args = parser.parse_args()
smbsrv = "smb//"+Ip+"//"+Name
# Clases
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def smb_folders():
	if Sharename:
		try:
			print ok+" Connecting to "+smbsrv+"..."+c
			f = open(filetmp, 'w')
		#conectar al servidor
		#Guardar en archivo	
		#optener Folders
			for line in f.readlines():
				folder = line.strip(columna) #fixme
		#guardar en lista 
				Sharename.append(folder)
			print ok+" List of Folders in "+cg+smbsrv+cw+" updated"+c
			print ok= "Folders: "+cg+Sharename+c
			f.close()
		except Exception, e:
			print err+" Error " +str(e)
	else:
		print ok+" Using only assigned Folders Names: "+Sharename+c
	except Exception, e:
		print err+" Folders Names invalid?"+c
		
def smb_server_test():
	smb_folders()
	print ok+" Running"+tt+" smb server test..."+c
	print (ok+" Connecting to "+cg+"{f}".format(f=args.Sharename)+cw+" at server "+cg+"{s}".format(s=args.Name)+cw+", port "+cg+"{p}".format(p=args.Port)+"..."+c)
	try:
		conn = SMBConnection(username, password, 'client_machine_name', server, use_ntlm_v2 = True)
		assert conn.connect(ip, port)
	except Exception, e:
			print err+" Error " +str(e)
			print('### can not access the server')

# ---------------------------------------------------------------------
def main():
		smb_server_test()

if __name__ == '__main__':
	main()
