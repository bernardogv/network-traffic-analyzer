import unittest
from src.analysis import analyze_packets
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Packet


class TestAnalysis(unittest.TestCase):

    def test_analyze_ip_packet(self):
        # Create a mock IP packet
        packet = IP(src='192.168.1.1', dst='192.168.1.2')
        packets = [packet]

        # Capture the output using StringIO
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        analyze_packets(packets)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn('IP Packet: 192.168.1.1 -> 192.168.1.2', output)

    def test_analyze_tcp_segment(self):
        # Create a mock TCP packet
        packet = IP(src='192.168.1.1', dst='192.168.1.2') / TCP(sport=12345, dport=80)
        packets = [packet]

        # Capture the output
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        analyze_packets(packets)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn('TCP Segment: Port 12345 -> 80', output)

    # Additional tests for UDP, HTTP, etc.

if __name__ == '__main__':
    unittest.main()
