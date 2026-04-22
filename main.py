# Detection Logic (src/detect.py)

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




# Visualization (src/visualize.py)

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

# Key Features
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
