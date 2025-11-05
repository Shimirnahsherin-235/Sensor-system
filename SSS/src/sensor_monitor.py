import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read sensor data
data = pd.read_csv("sensor_data.csv")

# Convert timestamp column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

# Sort by time (to keep data in order)
data = data.sort_values('Timestamp')

# Common date formatting for clear time display
time_fmt = mdates.DateFormatter('%H:%M:%S')

# ======== TEMPERATURE ========
plt.figure(figsize=(10, 5))
plt.plot(
    data['Timestamp'], data['Temperature'],
    color='#FF4C4C', marker='o', markersize=6,
    linewidth=2.5, label='Temperature'
)
plt.title("Temperature Monitor", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Time", fontsize=13)
plt.ylabel("Temperature (°C)", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='best')
plt.gcf().autofmt_xdate(rotation=45)
plt.gca().xaxis.set_major_formatter(time_fmt)
plt.tight_layout()
plt.savefig("temperature_chart.png", dpi=400)
plt.show()

# ======== HUMIDITY ========
plt.figure(figsize=(10, 5))
plt.plot(
    data['Timestamp'], data['Humidity'],
    color='#1E90FF', marker='o', markersize=6,
    linewidth=2.5, label='Humidity'
)
plt.title("Humidity Monitor", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Time", fontsize=13)
plt.ylabel("Humidity (%)", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='best')
plt.gcf().autofmt_xdate(rotation=45)
plt.gca().xaxis.set_major_formatter(time_fmt)
plt.tight_layout()
plt.savefig("humidity_chart.png", dpi=400)
plt.show()

# ======== GAS LEVEL ========
plt.figure(figsize=(10, 5))
plt.plot(
    data['Timestamp'], data['GasLevel'],
    color='#32CD32', marker='o', markersize=6,
    linewidth=2.5, label='Gas Level'
)
plt.title("Gas Level Monitor", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Time", fontsize=13)
plt.ylabel("Gas Level (ppm)", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='best')
plt.gcf().autofmt_xdate(rotation=45)
plt.gca().xaxis.set_major_formatter(time_fmt)
plt.tight_layout()
plt.savefig("gaslevel_chart.png", dpi=400)
plt.show()
