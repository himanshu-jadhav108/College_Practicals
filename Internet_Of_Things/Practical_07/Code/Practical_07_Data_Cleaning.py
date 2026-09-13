# Practical 7: Data cleaning, normalization and visualization of IoT sensor data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create dataset
np.random.seed(42)
n = 60
df = pd.DataFrame({
    "time": pd.date_range("2025-01-01 08:00", periods=n, freq="min"),
    "temperature": np.random.normal(28, 1.5, n).round(1),
    "humidity": np.random.normal(60, 5, n).round(1),
    "light": np.random.normal(450, 40, n).round(0),
})
df.loc[[5, 17, 33, 48], "temperature"] = np.nan
df.loc[[10, 41], "humidity"] = np.nan
df.loc[25, "temperature"] = 85.0  # outlier

# 2. Data Cleaning
df = df.drop_duplicates()
df["temperature"] = df["temperature"].fillna(df["temperature"].median())
df["humidity"] = df["humidity"].fillna(df["humidity"].mean())

q1 = df["temperature"].quantile(0.25)
q3 = df["temperature"].quantile(0.75)
iqr = q3 - q1
outlier = (df["temperature"] < q1 - 1.5 * iqr) | (df["temperature"] > q3 + 1.5 * iqr)
df = df[~outlier].reset_index(drop=True)

# 3. Normalization (Min-Max)
cols = ["temperature", "humidity", "light"]
norm = df.copy()
norm[cols] = (df[cols] - df[cols].min()) / (df[cols].max() - df[cols].min())

# 4. Visualization
fig, ax = plt.subplots(2, 2, figsize=(10, 6), dpi=150)
ax[0, 0].plot(df["time"], df["temperature"], color="#e74c3c", lw=1.5)
ax[0, 0].set_title("Temperature vs Time (cleaned)", fontsize=10, weight='bold')

ax[0, 1].hist(df["humidity"], bins=10, color="#3498db", edgecolor="#2c3e50")
ax[0, 1].set_title("Humidity Distribution", fontsize=10, weight='bold')

for col, clr in zip(cols, ["#e74c3c", "#3498db", "#2ecc71"]):
    ax[1, 0].plot(norm["time"], norm[col], label=col, color=clr, lw=1.2)
ax[1, 0].legend(fontsize=8)
ax[1, 0].set_title("Normalized Sensor Data (0-1)", fontsize=10, weight='bold')

ax[1, 1].scatter(df["temperature"], df["humidity"], color="#27ae60", alpha=0.8)
ax[1, 1].set_title("Temperature vs Humidity", fontsize=10, weight='bold')

for a in ax.flat:
    a.grid(True, linestyle="--", alpha=0.4)
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig(r"d:\College Practicals\Internet_Of_Things\Practical_07\Output\Practical_07_Plot.png", facecolor="white")
plt.close()
print("Practical 7 script executed and plot saved.")
