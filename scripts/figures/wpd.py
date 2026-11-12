"""產生《小波封包分解（WPD）》講義的圖片。

執行：python scripts/figures/wpd.py
輸出：docs/assets/images/wpd/fig-1.svg、fig-2.svg
"""
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np

from _common import ACCENT, INK, MUTED, PRIMARY, draw_box, draw_edge, natural_path, save, wpd_level

SLUG = "wpd"


def frac(num, den):
    """以 fs 為單位的分數字串，例如 frac(3, 8) -> '3fs/8'。"""
    f = Fraction(num, den)
    if f == 0:
        return "0"
    top = "fs" if f.numerator == 1 else f"{f.numerator}fs"
    return top if f.denominator == 1 else f"{top}/{f.denominator}"
LEVEL = 3

# 圖 1：三層完整封包樹（每層依頻率排序，框內為 PyWavelets 路徑）
fig, ax = plt.subplots(figsize=(8.6, 3.9))
ax.set_axis_off()
ax.grid(False)
xs = {}
for j in range(LEVEL + 1):
    count = 2 ** j
    for k in range(count):
        x = (k + 0.5) / count * 16 - 8
        y = (LEVEL - j) * 1.15
        xs[(j, k)] = (x, y)
for j in range(LEVEL):
    for k in range(2 ** j):
        px, py = xs[(j, k)]
        for c in (2 * k, 2 * k + 1):
            cx, cy = xs[(j + 1, c)]
            draw_edge(ax, px, py, cx, cy)
for (j, k), (x, y) in xs.items():
    if j == 0:
        draw_box(ax, x, y, "x[n]\n0 ~ fs/2", w=1.8)
        continue
    path = natural_path(k ^ (k >> 1), j)
    swapped = k != (k ^ (k >> 1))
    den = 2 ** (j + 1)
    band = f"{frac(k, den)} ~ {frac(k + 1, den)}" if j < LEVEL else f"{k} ~ {k + 1}"
    draw_box(
        ax, x, y, f"{path}\n{band}", w=2.1 if j < LEVEL else 1.7,
        face="#F7EFE2" if swapped else ("#EEF4F6" if j == LEVEL else "white"),
        edge=ACCENT if swapped else PRIMARY, size=8.5,
    )
ax.text(8.0, -0.72, "bottom row: band k ~ k+1 in units of fs/16   |   orange: frequency order differs from natural order",
        ha="right", fontsize=8, color=INK)
ax.set_xlim(-8.3, 8.3)
ax.set_ylim(-0.95, LEVEL * 1.15 + 0.5)
save(fig, SLUG, "fig-1")

# 圖 2：兩組合成訊號的相對能量分布
rng = np.random.default_rng(7)
fs = 1000
n = 1024
t = np.arange(n) / fs


def signal(amp_high):
    x = 1.0 * np.sin(2 * np.pi * 90 * t) + 0.6 * np.sin(2 * np.pi * 210 * t)
    x += amp_high * np.sin(2 * np.pi * 400 * t)
    return x + 0.15 * rng.standard_normal(n)


def rel_energy(x):
    e = np.array([np.sum(c ** 2) for c in wpd_level(x, LEVEL)])
    return e / e.sum()


p_ref = rel_energy(signal(0.2))
p_new = rel_energy(signal(0.9))
band = fs / 2 ** (LEVEL + 1)
labels = [f"{k * band:.1f}–\n{(k + 1) * band:.1f}" for k in range(2 ** LEVEL)]
pos = np.arange(2 ** LEVEL)

fig, ax = plt.subplots(figsize=(7.6, 3.4))
ax.bar(pos - 0.2, p_ref, width=0.4, color=PRIMARY, label="signal A (reference)")
ax.bar(pos + 0.2, p_new, width=0.4, color=ACCENT, label="signal B (more 400 Hz energy)")
ax.set_xticks(pos, labels, fontsize=8)
ax.set_xlabel("frequency band (Hz), level-3 nodes in frequency order, fs = 1000 Hz")
ax.set_ylabel("relative energy $p_{3,k}$")
ax.grid(axis="x", visible=False)
ax.legend(loc="upper right")
ax.tick_params(axis="x", colors=INK)
ax.spines["bottom"].set_color(MUTED)
save(fig, SLUG, "fig-2")

np.set_printoptions(precision=3, suppress=True)
print("p_ref =", p_ref)
print("p_new =", p_new)
