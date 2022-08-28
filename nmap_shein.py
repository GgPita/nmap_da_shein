#!/usr/bin/python3
# Programa em python com funcionalidade parecida com a do já conhecido nmap
#Copyright (C) 2022 Gustavo Pita#
#Versão: 1.2
#Repositório Git: https://github.com/GgPita/nmap_da_shein
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Public LIcense published by the Free Software Foundation, version 3#
#See <https://www.gnu.org/licenses/>#

import argparse
from socket import socket, AF_INET, SOCK_STREAM
import scapy.all as scapy
import re

#Classe que contém todas as funções do programa
class nmap_shein:
    def __init__(self, alvo, portas, opcao):
        self.alvo = alvo
        self.portas = portas
        self.opcao = opcao
        self.banners = []

#Função para verificar se as portas estão abertas e capturar banners usando socket
    def scan_portas(self, porta):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        banner = ""

        try:
            s.connect((self.alvo, porta))
            try:
                banner = s.recv(1024).decode()
                self.banners.append(banner)
            except:
                pass

            porta = f"{porta}/tcp".ljust(30)
            print(f"{porta}open")

            if banner != "":
                print(f"{banner}\n")
            s.close()

        except:
            pass

#Função para escanear portas
    def scan(self):
        print(f"\nEscaneando o host {self.alvo}\n")
        print(f"Porta".ljust(30) + "STATUS")

        if (isinstance(args.portas, str)):
            inicio = int(self.portas.split("-")[0])
            final = int(self.portas.split("-")[1])
            self.portas = list(range(inicio, final + 1))

        for porta in self.portas:
            self.scan_portas(porta)

#Função para verificar o hostname usando socket
    def nome_host(self):
        nome = socket.gethostname(self.alvo)
        print(nome)
        return nome


#Função para possibilitar o uso de opções via linha de comando usando argparser
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--portas", action="store",  help="Indicar o range de portas a serem verificadas.")
    parser.add_argument("-a", "--alvo", action="store", help="Indicar o IP do host a ser verificado")
    parser.add_argument("-o", "--opcao", action="store", help="Indicar a opção desejada entre 1(scan localhost), 2(scan portas 80 e 443), 3(scan portas 1-65000), 4(scan portas de acesso remoto telnet e ssh) e 5(escanear as 10 portas mais comuns)")
    args = parser.parse_args()

    if not args.alvo and not args.opcao:
        print("Não foi indicado um host para ser escaneado, finalizando programa")
        quit()

    if not args.portas and not args.opcao:
        print("Não foi indicado um range de portas a ser escaneado nem uma das opções predefinidas, finalizando programa")
        quit()

    if args.opcao:
        if args.opcao == "1":
            args.alvo = "127.0.0.1"
        elif args.opcao == "2":
            args.portas = [80, 443]
        elif args.opcao == "3":
            args.portas = "1-65000"
        elif args.opcao == "4":
            args.portas = [22, 23]
        elif args.opcao == "5":
            args.portas = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443]

        else:
            print("Opção invalida")
            quit()

    return args
    
if __name__ == "__main__":
    args = get_arguments()
    nmap = nmap_shein(
            alvo=args.alvo,
            portas=args.portas,
            opcao=args.opcao)

#Chamada da função scan
    nmap.scan()
    
    print(f"\nForam escaneadas {len(nmap.portas)} portas no host {nmap.alvo}")
