#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import argparse
import clr
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
parser.add_argument('-u', '--username', type=str, default='Guest', help='Username. Default is Guest')
parser.add_argument('-p', '--password', type=str, default='passwd', help='Password. Default is "passwd"')
parser.add_argument('-i', '--ip', type=str, required=True, help='server ip. example: 192.168.0.1')
parser.add_argument('-s', '--server', type=str, required=True, help='server name. example: 192.168.0.1//sharename')
parser.add_argument('-f', '--sharename', type=str, required=True, help='Set the folders to test.')
args = parser.parse_args()
# Clases
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def smb_server_test():
	print ok+cw+"Running"+tt+" smb server test"+c
	print (cw+ok+"connecting to "+cg+"{f}".format(f=args.sharename)+cw+" at server "+cg+"{s}".format(s=args.server)+cw+", port "+cg+"{p}".format(p=args.port)+c)
	try:
		conn = SMBConnection(username, password, 'client_machine_name', server_name, use_ntlm_v2 = True)
		assert conn.connect(ip, port)
	except Exception, e:
			print err+" Error " +str(e)
			print('### can not access the server')

# ---------------------------------------------------------------------
def main():
		smb_server_test()

if __name__ == '__main__':
	main()
