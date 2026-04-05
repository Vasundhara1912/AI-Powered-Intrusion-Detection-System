from scapy.all import sniff

def process_packet(packet):
    try:
        if packet.haslayer('IP'):
            ip_src = packet['IP'].src
            ip_dst = packet['IP'].dst
            proto = packet['IP'].proto

            return {
                "src": ip_src,
                "dst": ip_dst,
                "proto": proto
            }
    except:
        return None

def start_sniffing(callback):
    sniff(prn=lambda pkt: callback(process_packet(pkt)), store=0)
