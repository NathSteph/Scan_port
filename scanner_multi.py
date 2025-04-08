# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:45:22 2025

@author: nsmar
"""

import socket
import threading
from datetime import datetime

# Verrou pour synchroniser les impressions
print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} est ouvert")
        s.close()
    except Exception as e:
        pass

def main():
    target = input("Entrez l'adresse IP ou le domaine à scanner : ")
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"❌ Adresse invalide : {target}")
        return

    print(f"✅ Lancement du scan sur {ip}")
    start_time = datetime.now()

    # Plage de ports
    start_port = 1
    end_port = 1024

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = datetime.now()
    print(f"⏱️ Scan terminé en : {end_time - start_time}")

if __name__ == "__main__":
    main()
