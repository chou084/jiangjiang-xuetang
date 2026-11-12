"""產生《餘弦相似性》講義的圖片。

執行：python scripts/figures/cosine-similarity.py
輸出：docs/assets/images/cosine-similarity/fig-1.svg
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

from _common import ACCENT, INK, MUTED, PRIMARY, save

SLUG = "cosine-similarity"

a = np.array([3.0, 1.0])
b = np.array([1.0, 2.5])
c = 1.8 * a
cos_ab = a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
theta = np.degrees(np.arccos(cos_ab))

fig, ax = plt.subplots(figsize=(5.6, 4.0))
for vec, color, name, offset in (
    (c, MUTED, r"$\mathbf{c} = 1.8\,\mathbf{a}$", (0.1, 0.15)),
    (a, PRIMARY, r"$\mathbf{a}$", (0.1, -0.35)),
    (b, ACCENT, r"$\mathbf{b}$", (-0.35, 0.1)),
):
    ax.annotate("", xy=vec, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=2.0, mutation_scale=14))
    ax.text(vec[0] + offset[0], vec[1] + offset[1], name, color=color, fontsize=12)

ang_a = np.degrees(np.arctan2(a[1], a[0]))
ang_b = np.degrees(np.arctan2(b[1], b[0]))
ax.add_patch(Arc((0, 0), 2.0, 2.0, theta1=ang_a, theta2=ang_b, color=INK, linewidth=1.0))
mid = np.radians((ang_a + ang_b) / 2)
ax.text(1.2 * np.cos(mid), 1.2 * np.sin(mid), r"$\theta$", fontsize=12, color=INK)

ax.text(0.2, 3.35, rf"$\cos\theta(\mathbf{{a}},\mathbf{{b}}) = {cos_ab:.3f}$  ($\theta \approx {theta:.1f}^\circ$)",
        fontsize=10, color=INK)
ax.text(0.2, 3.0, r"$\cos\theta(\mathbf{a},\mathbf{c}) = 1$  (same direction, different length)",
        fontsize=10, color=INK)
ax.set_xlim(-0.3, 6.0)
ax.set_ylim(-0.3, 3.7)
ax.set_aspect("equal")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
save(fig, SLUG, "fig-1")

print(f"cos(a,b) = {cos_ab:.4f}, theta = {theta:.2f} deg")
