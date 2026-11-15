import matplotlib.pyplot as plt
import pandas as pd

# 1. Load both CSV files
# L4.csv: Discrete CMOS Inverter (VIN vs V(vout))
df_discrete = pd.read_csv("L4.csv")  # Tab or comma separated depending on export

# S7.csv: 65nm Reference Inverter (VIN vs V(n003))
df_65nm = pd.read_csv("S7.csv", sep="\t")

# 2. Extract raw voltage columns
vin_disc = df_discrete["VIN"]
vout_disc = df_discrete["V(vout)"]

vin_65 = df_65nm["VIN"]
vout_65 = df_65nm["V(n003)"]

# 3. Normalize voltages to their respective supply rails (0 to 1 scale)
# Discrete supply VDD = 5V, 65nm supply VDD ≈ 1.1V (or max value)
vdd_disc = vin_disc.max()
vdd_65 = vin_65.max()

vin_disc_norm = vin_disc / vdd_disc
vout_disc_norm = vout_disc / vdd_disc

vin_65_norm = vin_65 / vdd_65
vout_65_norm = vout_65 / vdd_65

# 4. Plot Normalized VTC Comparison
plt.figure(figsize=(8, 6))
plt.plot(
    vin_disc_norm,
    vout_disc_norm,
    color="green",
    linewidth=2,
    label="Discrete CMOS Inverter (5V)",
)
plt.plot(
    vin_65_norm,
    vout_65_norm,
    color="blue",
    linewidth=2,
    label="65nm Inverter (1.1V)",
)

# 5. Graph Formatting & Labels
plt.title(
    "Voltage Transfer Curve (VTC) Comparison", fontsize=13, pad=12
)
plt.xlabel("Input Voltage ($V_{IN} / V_{DD}$)", fontsize=11)
plt.ylabel("Output Voltage ($V_{OUT} / V_{DD}$)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.legend(loc="upper right", fontsize=10)

# Save and show the plot
plt.savefig("L5.png", dpi=300, bbox_inches="tight")
plt.show()