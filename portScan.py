# -*- coding: utf-8 -*-
import argparse
import socket

parser = argparse.ArgumentParser(description="Buscar portas abertas em um host")
parser.add_argument('-a', '--alvo', type=str, help='Endereço do alvo')
parser.add_argument('-p', '--portas', type=str, help='Portas a serem testadas')
parser.add_argument('-f', '--full', type=None, help='Scan em todas as portas possíveis')
args = parser.parse_args()

#Variaveis
arrayPortas = []
x = ''

if (args.portas.find('-') > 0):
    x = args.portas.split('-')
    for n in range(int(x[0]),int(x[1])+1):
        arrayPortas.append(int(n))
else:
    for n in args.portas.split(','):
        arrayPortas.append(int(n))

def testarPortas(alvo, portas):
    portasAbertas = []
    x = []
    for i in portas:
        x.append(i)
    for port in x:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.5)
        codigo = cliente.connect_ex((alvo, port))
        if (codigo == 0):
            print ("Testando "+alvo+" na porta "+str(port)+".................resultado: Online | Código: "+str(codigo))
            portasAbertas.append(port)
        else:
            print ("Testando "+alvo+" na porta "+str(port)+".................resultado: Offline | Código: "+str(codigo))
    print (str(len(portasAbertas))+" porta(s) aberta(s) encontrada(s): "+str(portasAbertas))


def main():
    testarPortas(args.alvo, arrayPortas)

if __name__ == '__main__':
    main()
