This is the environment created for showing the dhcp-starvation attack, which is a type of Denial-of-Service attack.
It is based on DHCP protocol, which relies on a server which dinamically assigns an IP address (and the necessary config parameters) 
to each client in its network.

1.	We have 3 entities: - the server which provides the DHCP service
						- the attacker which does the DoS attack 
						- the client which tries but fails connecting to the network
	Each of them are VMs in the same network. In my setup, the network is 192.168.56.0/24, the server has the IP 192.168.56.102

2. On the server machine, I installed a DHCP server (isc-dhcp-server).
	In its config file (/etc/dhcp/dhcpd.conf), I set a subnet (range 192.168.56.100-200), available IPs which can be allocated,
	and another additional parameters like lease-time and so on.
	
3. Started the deamon and enabling the dhcp server.

4. Each client in the network (honest client and the attacker) have to get their ip from the dhcp server, which is why I set the /etc/network/interfaces:
	auto enp0s3
	iface enp0s3 inet dhcp
	
5.	Restarted network for the attacker in order to get the ip from the server.

6. Attacker runs the dhcp_starvation.py, which sends dhcp query requests with random fake MAC addresses, until the server 
	exhaust all the IPs in the specified subnet.

7. Restart the network service on the honest client. It can't get an ip from the dhcp server and it can't use the network, which means the 
	attack was successful.