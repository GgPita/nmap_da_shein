#!/usr/bin/python3

import argparse
import scapy.all as scapy
from socket import socket, AF_INET, SOCK_STREAM
import re
import time

class nmap_shein:
    def __init__(self, alvo, portas, opcao):
        self.alvo = alvo
        self.portas = portas
        self.opcao = ocpao
        self.banners = []

    def scan_portas(self, porta):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        banner = ""

        try:
            s.connect((self.alvo, porta))
            try:
                banner = s.recv(1024).decode().strip()
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


    def scan(self):
        print(f"Escaneando o host {self.alvo}\n")
        print(f"Porta".ljust(30) + "STATUS")

        if (isinstance(args.portas, str)):
            inicio = int(self.portas.split("-")[0])
            final = int(self.portas.split("-")[1])
            self.portas = list(range(inicio, final + 1))

        for porta in self.portas:
            self.scan_portas(porta)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--portas", action="store",  help="Indicar o range de portas a serem verificadas. Caso não seja indicado um range, o programa ira escannear 10 portas comuns")
    parser.add_argument("-a", "--alvo", action="store", help="Indicar o IP do host a ser verificado")
    parser.add_argument("-o", "--opcao", action="store", help="Indicar a opção desejada entre 1(scan localhost), 2(scan portas 80 e 443), 3(scan portas 1-65000)")
    args = parser.parse_args()

    if not args.portas and not args.opcao:
        print("Não foi indicado um range de portas, escaneando as 10 portas mais comuns")
        args.portas = [20, 21, 80, 443, 22, 23, 53, 110, 25, 143]

    if args.opcao:
        if args.opcao == "1":
            args.alvo = "127.0.0.1"
        elif args.opcao == "2":
            args.portas = [80, 443]
        elif args.opcao == "3":
            args.portas = "1-65000"
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

    nmap.scan()
