# log-analysis-threat-detection
I built a Python-based log analysis system using Pandas to detect suspicious activities like brute force attacks and off-hour logins. I used grouping and filtering techniques to identify abnormal patterns and mapped them to potential cybersecurity threats.

#  Advanced Project: Log Analysis & Threat Detection System

# Overview
An enhanced cybersecurity analytics project that processes simulated authentication logs to detect suspicious behavior such as brute-force attacks, off-hours access, and anomalous IP activity. It includes:
- Data processing with **Pandas**
- Rule-based threat detection
- **Visualizations** with Matplotlib
- Optional **Streamlit dashboard** for interactive analysis

---

# Project Structure

```
log-analysis-threat-detection/
│
├── data/
│   └── logs.csv
├── src/
│   ├── main.py
│   ├── detect.py
│   └── visualize.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Dataset (data/logs.csv)

```
timestamp,username,ip,status
2025-04-01 02:30,user1,192.168.1.1,failed
2025-04-01 02:31,user1,192.168.1.1,failed
2025-04-01 02:32,user1,192.168.1.1,failed
2025-04-01 02:33,user1,192.168.1.1,failed
2025-04-01 02:34,user1,192.168.1.1,failed
2025-04-01 02:35,user1,192.168.1.1,failed
2025-04-01 10:00,user2,192.168.1.2,success
2025-04-01 03:00,user3,192.168.1.3,success
2025-04-01 04:00,user4,192.168.1.4,success
2025-04-01 11:00,user2,192.168.1.2,failed
2025-04-01 11:01,user2,192.168.1.2,failed
2025-04-01 11:02,user2,192.168.1.2,failed
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```
pandas
matplotlib
streamlit
```

---

# Detection Logic (src/detect.py)

```python
import pandas as pd


def detect_bruteforce(df):
    failed = df[df['status'] == 'failed']
    counts = failed.groupby('ip').size()
    return counts[counts > 5]


def detect_offhours(df):
    df['hour'] = df['timestamp'].dt.hour
    return df[df['hour'] < 5]
```

---

# Main Script (src/main.py)

```python
import pandas as pd
from detect import detect_bruteforce, detect_offhours

# Load data
df = pd.read_csv("../data/logs.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Run detections
brute = detect_bruteforce(df)
off = detect_offhours(df)

print("=== Threat Report ===")
print("\nBrute Force IPs:")
print(brute)

print("\nOff-hours activity:")
print(off[['timestamp','username','ip']])
```

---

#Visualization (src/visualize.py)

```python
import matplotlib.pyplot as plt


def plot_failed_attempts(df):
    failed = df[df['status'] == 'failed']
    counts = failed['ip'].value_counts()

    counts.plot(kind='bar')
    plt.title("Failed Login Attempts per IP")
    plt.xlabel("IP Address")
    plt.ylabel("Attempts")
    plt.show()
```

---

# Streamlit Dashboard (app.py)

```python
import streamlit as st
import pandas as pd
from src.detect import detect_bruteforce, detect_offhours

st.title("🔐 Log Analysis Dashboard")

# Load data
df = pd.read_csv("data/logs.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

st.subheader("Raw Data")
st.write(df)

# Detection
brute = detect_bruteforce(df)
off = detect_offhours(df)

st.subheader("🚨 Brute Force Alerts")
st.write(brute)

st.subheader("🌙 Off-Hours Activity")
st.write(off[['timestamp','username','ip']])
```

Run it using:
```bash
streamlit run app.py
```

---

## 🎯 Key Features
- Detects brute-force attacks
- Identifies off-hour anomalies
- Visualizes suspicious activity
- Interactive dashboard (Streamlit)

---

# Threat Mapping
| Pattern | Threat |
|--------|--------|
| Multiple failed logins | Brute Force |
| Late-night login | Suspicious Behavior |

---

# Future Enhancements
- Add ML-based anomaly detection
- Integrate real-time logs (API)
- Add IP geolocation tracking

---

# Interview Explanation

“I developed an advanced log analysis system using Python and Pandas to detect cybersecurity threats like brute-force attacks and abnormal login patterns. I modularized detection logic, added visualizations, and built a Streamlit dashboard to make insights interactive, similar to basic SIEM tools.”

---

## 👩‍💻 Author
Ishwari C Badiger
