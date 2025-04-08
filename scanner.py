# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:20:27 2025

@author: nsmar
"""

import socket
from datetime import datetime

# Fonction principale
def scan_ports(target_ip, start_port, end_port):
    print(f"Début du scan de {target_ip} de port {start_port} à {end_port}")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # 500ms pour éviter que ça bloque

        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} est ouvert")
        s.close()

    end_time = datetime.now()
    print(f"Scan terminé en : {end_time - start_time}")

# Exemple d’utilisation
if __name__ == "__main__":
    target = input("Entrez l'adresse IP ou le domaine à scanner : ")
    scan_ports(target, 1, 1024)
