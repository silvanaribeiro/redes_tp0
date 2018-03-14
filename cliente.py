#Parametros do Cliente : Enedereco de Ip do servidor, porta do servidor, string texto, inteiro chave

import socket 
import struct

def main(argv):
	HOST = None
	PORT = None
	texto = None
	chave = None
	
	try:
		opts, args = getopt.getopt(argv, "p:")
	except getopt.GetoptError:
		print "cliente.py -i <IP Servdidor> -p <Porto> -t <texto> -c <chave>"
	for opt, arg in opts:
		if opt == '-i':
			HOST = arg # Endereco IP do Servidor 
		elif opt == '-p':
			PORT = arg # Porta que o Servidor esta 
		elif opt == '-t':
			texto = arg
		elif opt == '-c'
			chave = arg
			
HOST = '127.0.0.1'     # Endereco IP do Servidor 
PORT = 5000            # Porta que o Servidor esta 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
dest = (HOST, PORT) 
tcp.connect(dest)
tamanho_string = len(texto.encode('utf-8')*2))
tcp.send(struct.pack('>I', int(tamanho_string))
tcp.send(texto)
tcp.send(struct.pack('>I',int(chave)))
resposta = tcp.recv(tamanho_string)    
print resposta    

def do_cifra_de_cesar(texto, chave):
    return ''.join(chr(ord(c)+chave) for c in texto)
	
if __name__ == "__main__":
	main(sys.argv[1:])
