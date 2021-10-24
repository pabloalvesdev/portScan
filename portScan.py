# -*- coding: utf-8 -*-
import sys
import argparse
import socket

#variáveis
portas = []
alvo = sys.argv[1]
arg = sys.argv[2:]

for p in arg:
    x = int(p)
    portas.append(x)

portasAbertas = []
for port in portas:
#for port in range(100):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.2)
        codigo = cliente.connect_ex((alvo, port))
        if (codigo == 0):
                print "Porta", port, "-> On"
                portasAbertas.append(port)
        else:
                print "Porta", port, "-> Off"
print "Foram encontradas", len(portasAbertas), "porta(s) aberta(s):", portasAbertas
