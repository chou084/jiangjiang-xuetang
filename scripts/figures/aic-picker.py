"""產生《AIC picker》講義的圖片。

執行：python scripts/figures/aic-picker.py
輸出：docs/assets/images/aic-picker/fig-1.svg
"""
import matplotlib.pyplot as plt
import numpy as np

from _common import ACCENT, INK, MUTED, PRIMARY, save

SLUG = "aic-picker"

rng = np.random.default_rng(3)
fs = 1_000_000          # 1 MHz，常見聲發射取樣率量級
n = 1000
onset = 400
t_us = np.arange(n) / fs * 1e6
x = 0.05 * rng.standard_normal(n)
tau = np.arange(n - onset)
x[onset:] += np.exp(-tau / 150) * (1 - np.exp(-tau / 8)) * np.sin(2 * np.pi * 150e3 * tau / fs)


def aic_picker(sig):
    sig = np.asarray(sig, dtype=float)
    m = len(sig)
    aic = np.full(m, np.nan)
    for k in range(2, m - 2):
        v1, v2 = np.var(sig[:k]), np.var(sig[k:])
        if v1 > 0 and v2 > 0:
            aic[k] = k * np.log(v1) + (m - k - 1) * np.log(v2)
    return int(np.nanargmin(aic)), aic


k_hat, aic = aic_picker(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.4, 4.6), sharex=True)
ax1.plot(t_us, x, color=INK, linewidth=0.7)
ax1.axvline(t_us[onset], color=MUTED, linestyle="--", linewidth=1.2, label=f"true onset ({t_us[onset]:.0f} µs)")
ax1.axvline(t_us[k_hat], color=ACCENT, linewidth=1.4, label=f"AIC pick ({t_us[k_hat]:.0f} µs)")
ax1.set_title("(a) synthetic AE burst with noise", loc="left")
ax1.set_ylabel("amplitude")
ax1.legend(fontsize=8, loc="upper right")

ax2.plot(t_us, aic, color=PRIMARY, linewidth=1.2)
ax2.plot(t_us[k_hat], aic[k_hat], "o", color=ACCENT, markersize=6)
ax2.set_title("(b) AIC(k) by Maeda's formula", loc="left")
ax2.set_xlabel("time (µs)")
ax2.set_ylabel("AIC(k)")
fig.tight_layout(h_pad=1.0)
save(fig, SLUG, "fig-1")

print("true onset index =", onset, " picked index =", k_hat)
