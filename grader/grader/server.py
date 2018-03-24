#Parametros do Servidor : porta do servidor
import socket
import struct
import sys, getopt, threading

def main(argv):
	HOST = None
	if len(argv) == 1:
			PORT = argv[0] # Porta em que o servidor esta 
			HOST = '' # Endereco IP do Servidor  
			        
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
			tcp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, 15)			
			orig = (HOST, int(PORT)) 
			tcp.bind(orig) 
			tcp.listen(5) 
			while 1:
				con, client = tcp.accept() # aceitando a conexao
						
				t=threading.Thread(target=handler, args=(con, client))
				t.start() # iniciando nova thread que recebe dados do cliente
			tcp.close()
			

def handler(con, client):
	s = struct.Struct('>I')
	tamanho_string = s.unpack(con.recv(4))[0] # Recebe tamanho da string como inteiro de 4 bytes (Big endian)
	texto = con.recv(int(tamanho_string)).decode('ascii') # Recebe o texto decodificado
	chave = s.unpack(con.recv(4))[0] # Recebe a chave como inteiro de 4 bytes (Big Endian)
	texto_decodificado = decodifica_cifra_de_cesar(str(texto), int(chave)) # Decodifica o texto
	print(texto_decodificado) 
	con.send(texto_decodificado.encode('ascii')) # Envia o texto decodificado como resposta ao cliente
	con.close()

			
def decodifica_cifra_de_cesar(texto, chave):
    texto_codificado = ''
    range_char = 26
    for c in texto:
        char_codificado = ord(c)-chave
        
        if(char_codificado < 97):
            while char_codificado < 97:
                char_codificado = char_codificado+range_char
        texto_codificado=texto_codificado+chr(char_codificado)
    return texto_codificado
	
if __name__ == "__main__":
	main(sys.argv[1:])
