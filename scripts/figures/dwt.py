"""產生《離散小波轉換（DWT）》講義的圖片。

執行：python scripts/figures/dwt.py
輸出：docs/assets/images/dwt/fig-1.svg、fig-2.svg
"""
import matplotlib.pyplot as plt
import numpy as np

from _common import ACCENT, INK, PRIMARY, draw_box, draw_edge, save, wavedec

SLUG = "dwt"

# 圖 1：三層 DWT 分解樹
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.set_axis_off()
ax.grid(False)
nodes = {
    "x": (0.0, 3.0, "x[n]\n0 ~ fs/2"),
    "A1": (-1.4, 2.0, "A1\n0 ~ fs/4"),
    "D1": (1.4, 2.0, "D1\nfs/4 ~ fs/2"),
    "A2": (-2.8, 1.0, "A2\n0 ~ fs/8"),
    "D2": (0.0, 1.0, "D2\nfs/8 ~ fs/4"),
    "A3": (-4.2, 0.0, "A3\n0 ~ fs/16"),
    "D3": (-1.4, 0.0, "D3\nfs/16 ~ fs/8"),
}
for parent, children in {"x": ("A1", "D1"), "A1": ("A2", "D2"), "A2": ("A3", "D3")}.items():
    px, py, _ = nodes[parent]
    for child, lab in zip(children, ("h, ↓2", "g, ↓2")):
        cx, cy, _ = nodes[child]
        draw_edge(ax, px, py, cx, cy, lab)
for key, (x, y, text) in nodes.items():
    is_leaf = key in ("A3", "D3", "D2", "D1")
    draw_box(ax, x, y, text, face="#EEF4F6" if is_leaf else "white")
ax.set_xlim(-5.2, 2.4)
ax.set_ylim(-0.5, 3.5)
ax.text(2.35, -0.35, "shaded = coefficients kept", ha="right", fontsize=8, color=INK)
save(fig, SLUG, "fig-1")

# 圖 2：合成訊號與各層係數
fs = 1024
t = np.arange(fs) / fs
x = np.sin(2 * np.pi * 8 * t)
burst = (t >= 0.6) & (t < 0.64)
x[burst] += 0.8 * np.sin(2 * np.pi * 300 * t[burst])

coeffs = wavedec(x, 3)
names = ["A3", "D3", "D2", "D1"]

fig, axes = plt.subplots(5, 1, figsize=(7.2, 7.0), sharex=False)
axes[0].plot(t, x, color=INK, linewidth=0.8)
axes[0].set_title("x[n]: 8 Hz sine + 300 Hz burst at t = 0.60 s  (fs = 1024 Hz)", loc="left")
axes[0].axvspan(0.6, 0.64, color=ACCENT, alpha=0.18, linewidth=0)
for ax, name, c in zip(axes[1:], names, coeffs):
    tc = (np.arange(len(c)) + 0.5) * len(t) / len(c) / fs
    ax.plot(tc, c, color=PRIMARY if name != "D1" else ACCENT, linewidth=0.9)
    ax.set_title(f"{name}  ({len(c)} coefficients)", loc="left")
    ax.axvspan(0.6, 0.64, color=ACCENT, alpha=0.18, linewidth=0)
for ax in axes:
    ax.set_xlim(0, 1)
axes[-1].set_xlabel("time (s)")
fig.tight_layout(h_pad=0.8)
save(fig, SLUG, "fig-2")
