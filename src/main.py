from capture import capture_packets
from analysis import analyze_packets
from visualization import visualize_protocol_distribution

def main():
    packets = capture_packets(count=100)
    analyze_packets(packets)
    visualize_protocol_distribution(packets)

if __name__ == "__main__":
    main()
