# Practical 10: Data Minimization Using Smart Threshold Alert (Privacy-by-Design)
import random
import matplotlib.pyplot as plt

random.seed(7)
THRESHOLD = 33.0  # Celsius
readings = [round(random.gauss(30, 3), 1) for _ in range(30)]
sent = []

for i, value in enumerate(readings, 1):
    if value > THRESHOLD:
        sent.append((i, value))

total = len(readings)
reduction = 100 * (total - len(sent)) / total

plt.figure(figsize=(8, 4.2), dpi=150)
plt.plot(range(1, total + 1), readings, "o-", color="#7f8c8d", lw=1.2, label="Sensor Reading (Kept on Device)")
plt.axhline(THRESHOLD, color="#c0392b", linestyle="--", lw=1.5, label=f"Threshold = {THRESHOLD}°C")
if sent:
    plt.scatter([s[0] for s in sent], [s[1] for s in sent], color="#e74c3c", s=70, zorder=5, label="Transmitted Alert")
plt.xlabel("Reading Index", fontsize=9, weight='bold')
plt.ylabel("Temperature (°C)", fontsize=9, weight='bold')
plt.title(f"Smart Threshold Alert - Data Minimization ({reduction:.1f}% Reduction)", fontsize=10, weight='bold')
plt.legend(fontsize=8)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(r"d:\College Practicals\Internet_Of_Things\Practical_10\Output\Practical_10_Plot.png", facecolor="white")
plt.close()
print("Practical 10 script executed and plot saved.")
