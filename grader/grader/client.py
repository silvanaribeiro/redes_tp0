#Parametros do Cliente : Enedereco de Ip do servidor, porta do servidor, string texto, inteiro chave

import socket 
import struct
import sys


def main(argv):
	HOST = None
	PORT = None
	texto = None
	chave = None
	# Deve receber os 4 parametros para iniciar conexao
	if len(argv) == 4:
		HOST = argv[0] # Endereco IP do Servidor 
		PORT = argv[1] # Porta em que o Servidor esta 
		texto = argv[2] # Texto a ser codificado e enviado ao servidor
		chave = argv[3] # Chave para codificar o texto
		
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criando socket)
		tcp.setsockopt(socket.SOL_SOCKET,  socket.SO_RCVTIMEO, 15)	
		dest = (str(HOST), int(PORT)) 
		tcp.connect(dest) # Conectando
		tamanho_string = len(texto)
		s = struct.Struct('>I')
		tcp.send(s.pack(int(tamanho_string))) # Enviando tamanho da string ao servidor como inteiro de 4 bytes (Big Endian)
		tcp.send(codifica_cifra_de_cesar(texto, int(chave)).encode('ascii')) # Enviando texto ao servidor codificado pela cifra de Cesar
		tcp.send(s.pack(int(chave))) # Enviando chave ao servidor como inteiro de 4 bytes (Big Endian)
		resposta = tcp.recv(int(tamanho_string)).decode('ascii')    # Recebendo resposta do servidor
		print(resposta)
		tcp.close()	

def codifica_cifra_de_cesar(texto, chave):
    texto_codificado = ''
    range_char = 26
    for c in texto:
        char_codificado = ord(c)+chave
        if(char_codificado > 122):
            while char_codificado > 122:
                char_codificado = char_codificado-range_char
        texto_codificado=texto_codificado+chr(char_codificado)
    return texto_codificado
	

	
if __name__ == "__main__":
	main(sys.argv[1:])
