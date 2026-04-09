"""
Plot PPG signal waveform for Sub 120, Clip 08.

Required files (in the same directory as this script):
  - 120_8.npy    : PPG signal data, e.g., /path/to/mmdataset/ppg/{subject_id}/{subject_id}_{clip_id}.npy

Output (saved to the same directory):
  - ppg_120_08.png

Usage: cd /home/lyc/Lab_Affairs/NPC_Tasks/TEMP/ppg && python plot_ppg.py
"""

import numpy as np
import matplotlib.pyplot as plt

FS = 30        # sampling rate (Hz)
DUR = 30       # duration to plot (seconds)
N = FS * DUR   # total samples = 900

# Load and slice data from 0s
data = np.load("120_8.npy")[:N]

# z-score normalization
data = (data - data.mean()) / data.std()

t = np.arange(len(data)) / FS

fig, ax = plt.subplots(figsize=(6, 2))
ax.plot(t, data, color="#1f77b4", linewidth=0.8)
ax.set_xlim(0, DUR)
ax.axis("off")
fig.tight_layout(pad=0)

# Save to current directory
fig.savefig("ppg_120_08.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved: ppg_120_08.png")
