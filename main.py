from sniffer import start_sniffing
from model import train_model
from detector import detect_anomaly
from utils import alert

model = train_model()

def handle_packet(packet):
    if packet:
        is_attack = detect_anomaly(model, packet)
        if is_attack:
            alert(packet)

if __name__ == "__main__":
    print("🔍 Starting Intrusion Detection System...")
    start_sniffing(handle_packet)
