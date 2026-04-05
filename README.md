📌 Overview
This project implements a real-time Intrusion Detection System (IDS) using Python.  
It captures live network traffic, extracts key features, and uses a Machine Learning model to detect anomalous behavior.

The system improves traditional IDS approaches by integrating:
- Real-time packet sniffing
- Machine Learning-based anomaly detection
- Modular and scalable architecture

---

## 🚀 Features
- 📡 Live packet capture using Scapy
- 🧠 ML-based anomaly detection (Isolation Forest)
- ⚠️ Real-time alert generation
- 🧩 Modular code structure
- 📊 Easy to extend with dashboards or APIs

---

## 🏗️ Project Structure

cyber_ids_project/
│
├── main.py # Entry point
├── sniffer.py # Packet capturing
├── detector.py # Anomaly detection logic
├── model.py # ML model training
├── utils.py # Alerts & logging
├── requirements.txt # Dependencies
└── data/
└── sample_traffic.csv


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd cyber_ids_project
2. Install dependencies
pip install -r requirements.txt
▶️ Usage

Run the IDS system:

python main.py
🧠 How It Works
Captures network packets using Scapy
Extracts features such as protocol type
Passes data to the ML model
Detects anomalies using Isolation Forest
Triggers alerts for suspicious activity
📊 Sample Output
🔍 Starting Intrusion Detection System...

Packet: {'src': '192.168.1.5', 'dst': '8.8.8.8', 'proto': 6}

⚠️ Suspicious Activity Detected!
{'src': '10.0.0.45', 'dst': '192.168.1.1', 'proto': 1}
🛠️ Technologies Used
Python
Scapy
Pandas
Scikit-learn
📈 Future Enhancements
🌐 Web dashboard using Flask
📧 Email/SMS alert system
🧠 Advanced ML models (Deep Learning)
🌍 GeoIP tracking for attackers
🗃️ Database integration for logs
⚠️ Limitations
Uses basic dataset (can be improved)
Limited feature set for ML model
Requires admin privileges for packet sniffing
📚 Learning Outcomes
Understanding of network packet analysis
Hands-on with anomaly detection
Experience with real-time systems
Integration of cybersecurity with ML
