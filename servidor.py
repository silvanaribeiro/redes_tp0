#Parametros do Servidor : porta do servidor
import socket
import sys, getopt 

def main(argv):
	HOST = None
	try:
		opts, args = getopt.getopt(argv, "p:")
	except getopt.GetoptError:
		print "servidor.py -p <Porto>"
	for opt, arg in opts:
		if opt == '-p':
			PORT = arg # Porta que o Servidor esta 
			
	HOST = ''              # Endereco IP do Servidor        
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	orig = (HOST, PORT) 
	tcp.bind(orig) 
	tcp.listen(1) 
	con, cliente = tcp.accept() 
	tamanho_string = struct.unpack('>I', con.recv(8))
	texto = con.recv(tamanho_string)
	chave = struct.unpack('>I', con.recv(8))
	texto_decodificado = undo_cifra_de_cesar(texto, chave)
	print texto_decodificado   
	con.send(texto_decodificado) 
	con.close()
	
def undo_cifra_de_cesar(texto, chave):
    return ''.join(chr(ord(c)-chave) for c in texto)
	
if __name__ == "__main__":
	main(sys.argv[1:])
