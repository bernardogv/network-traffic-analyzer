from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.http import HTTPRequest, HTTPResponse

def analyze_packets(packets):
    for packet in packets:
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"TCP Segment: Port {tcp_layer.sport} -> {tcp_layer.dport}")

        if packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"UDP Datagram: Port {udp_layer.sport} -> {udp_layer.dport}")

        if packet.haslayer(HTTPRequest):
            http_layer = packet.getlayer(HTTPRequest)
            print(f"HTTP Request: {http_layer.Host}{http_layer.Path}")
