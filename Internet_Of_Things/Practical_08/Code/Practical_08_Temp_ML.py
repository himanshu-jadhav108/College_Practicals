# Practical 8: Real-Time Temperature Data Collection & ML Prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(1)
N = 30
minute = np.arange(N)
temp = 25.0 + 0.12 * minute + np.random.normal(0, 0.25, N)
data = pd.DataFrame({"minute": minute, "temperature": temp.round(2)})

train, test = data.iloc[:24], data.iloc[24:]
model = LinearRegression()
model.fit(train[["minute"]], train["temperature"])

pred = model.predict(test[["minute"]])
future = pd.DataFrame({"minute": np.arange(N, N + 6)})
future["predicted_temp"] = model.predict(future[["minute"]]).round(2)

line_x = pd.DataFrame({"minute": np.arange(0, N + 6)})
plt.figure(figsize=(8, 4.2), dpi=150)
plt.plot(data["minute"], data["temperature"], "o-", color="#2980b9", label="Actual Readings")
plt.plot(line_x["minute"], model.predict(line_x), "r--", label=f"Linear Fit (Slope={model.coef_[0]:.3f})")
plt.scatter(future["minute"], future["predicted_temp"], color="#e74c3c", zorder=4, label="Predicted (Future)")
plt.xlabel("Time (minutes)", fontsize=9, weight='bold')
plt.ylabel("Temperature (°C)", fontsize=9, weight='bold')
plt.title("Actual vs Predicted Temperature (Linear Regression)", fontsize=10, weight='bold')
plt.legend(fontsize=8)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(r"d:\College Practicals\Internet_Of_Things\Practical_08\Output\Practical_08_Plot.png", facecolor="white")
plt.close()
print("Practical 8 script executed and plot saved.")
