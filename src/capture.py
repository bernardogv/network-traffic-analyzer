from scapy.all import sniff

def capture_packets(interface=None, count=0, filter=None):
    """
    Capture packets from the network.
    """
    packets = sniff(iface=interface, count=count, filter=filter)
    return packets
