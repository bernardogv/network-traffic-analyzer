import matplotlib.pyplot as plt
from scapy.layers.inet import TCP, UDP, ICMP

def visualize_protocol_distribution(packets):
    protocol_counts = {'TCP': 0, 'UDP': 0, 'ICMP': 0}

    for packet in packets:
        if packet.haslayer(TCP):
            protocol_counts['TCP'] += 1
        elif packet.haslayer(UDP):
            protocol_counts['UDP'] += 1
        elif packet.haslayer(ICMP):
            protocol_counts['ICMP'] += 1

    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.bar(protocols, counts)
    plt.xlabel('Protocol')
    plt.ylabel('Number of Packets')
    plt.title('Protocol Distribution')
    plt.show()
