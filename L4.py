import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the CSV file exported from LTspice
# (Ensure L4.csv is in the same directory as this script)
df = pd.read_csv("L4.csv")

# Display basic statistics of the dataset
print(df.describe())

# 2. Plotting the Voltage Transfer Curve (VTC)
plt.figure(figsize=(7, 5))
plt.plot(
    df["VIN"],
    df["V(vout)"],
    color="green",
    linewidth=2,
    label="V(vout) vs VIN",
)

# 3. Graph formatting and labels
plt.title("CMOS Inverter Voltage Transfer Curve (VTC)", fontsize=12, pad=12)
plt.xlabel("Input Voltage $V_{IN}$ (V)", fontsize=11)
plt.ylabel("Output Voltage $V_{OUT}$ (V)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlim(-0.1, 5.1)
plt.ylim(-0.2, 5.2)
plt.legend(loc="upper right")

# 4. Save the plot as an image and display
plt.savefig("L4_plot.png", dpi=300)
plt.show()