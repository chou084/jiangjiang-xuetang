"""產生《Akaike 資訊準則（AIC）》講義的圖片。

執行：python scripts/figures/aic.py
輸出：docs/assets/images/aic/fig-1.svg
"""
import matplotlib.pyplot as plt
import numpy as np

from _common import ACCENT, INK, MUTED, PRIMARY, save

SLUG = "aic"

rng = np.random.default_rng(42)
n = 40
x = np.sort(rng.uniform(-1, 1, n))
y_true = 1 - 2 * x + 0.5 * x ** 2 + 1.5 * x ** 3
y = y_true + 0.3 * rng.standard_normal(n)

degrees = np.arange(0, 11)
rss, aic, aicc = [], [], []
for p in degrees:
    coef = np.polyfit(x, y, p)
    r = np.sum((y - np.polyval(coef, x)) ** 2)
    k = p + 2  # p+1 個多項式係數，加上雜訊變異數
    a = n * np.log(r / n) + 2 * k
    rss.append(r)
    aic.append(a)
    aicc.append(a + 2 * k * (k + 1) / (n - k - 1))
rss, aic, aicc = map(np.array, (rss, aic, aicc))
best = int(degrees[np.argmin(aic)])
best_c = int(degrees[np.argmin(aicc)])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5))

xx = np.linspace(-1, 1, 300)
ax1.scatter(x, y, s=14, color=INK, zorder=3, label="data (n = 40)")
for p, color, style in ((1, MUTED, "--"), (best, PRIMARY, "-"), (10, ACCENT, ":")):
    ax1.plot(xx, np.polyval(np.polyfit(x, y, p), xx), color=color, linestyle=style,
             linewidth=1.6, label=f"degree {p}")
ax1.set_ylim(y.min() - 1, y.max() + 1)
ax1.set_title("(a) polynomial fits", loc="left")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend(fontsize=8, loc="upper right")

ax2.plot(degrees, aic, "o-", color=PRIMARY, markersize=4, label="AIC")
ax2.plot(degrees, aicc, "s--", color=ACCENT, markersize=4, label="AICc")
ax2.axvline(best, color=PRIMARY, linewidth=0.8, alpha=0.5)
ax2b = ax2.twinx()
ax2b.plot(degrees, rss, "^:", color=MUTED, markersize=4, label="RSS (right axis)")
ax2b.set_ylabel("RSS", color=MUTED)
ax2b.tick_params(axis="y", colors=MUTED)
ax2b.grid(False)
ax2b.spines["right"].set_visible(True)
ax2.set_title("(b) criterion vs. polynomial degree", loc="left")
ax2.set_xlabel("polynomial degree p")
ax2.set_ylabel("criterion value")
ax2.set_xticks(degrees)
h1, l1 = ax2.get_legend_handles_labels()
h2, l2 = ax2b.get_legend_handles_labels()
ax2.legend(h1 + h2, l1 + l2, fontsize=8, loc="center right")
fig.tight_layout(w_pad=2.0)
save(fig, SLUG, "fig-1")

print("best degree by AIC  =", best)
print("best degree by AICc =", best_c)
for p, a, c, r in zip(degrees, aic, aicc, rss):
    print(f"p={p:2d}  RSS={r:8.3f}  AIC={a:8.2f}  AICc={c:8.2f}")
