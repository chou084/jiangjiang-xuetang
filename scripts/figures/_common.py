"""講義圖片共用設定與工具函式。

所有圖片腳本都從這裡匯入樣式，確保全站圖片風格一致。
只依賴 numpy 與 matplotlib，不需要安裝 PyWavelets。
"""
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = ROOT / "docs" / "assets" / "images"

# 全站配色（與 docs/assets/stylesheets/extra.css 一致）
INK = "#1F2A33"
PRIMARY = "#1E4D5C"
ACCENT = "#B0782A"
MUTED = "#8A9AA3"
GRID = "#E3E8EB"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.titlecolor": INK,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": INK,
        "ytick.color": INK,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "svg.fonttype": "path",
    }
)


def save(fig, slug: str, name: str) -> Path:
    """將圖片存成 docs/assets/images/<slug>/<name>.svg。"""
    out_dir = IMAGE_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    if os.environ.get("PREVIEW_DIR"):  # 選用：另存 PNG 預覽
        fig.savefig(Path(os.environ["PREVIEW_DIR"]) / f"{slug}_{name}.png", dpi=90, bbox_inches="tight")
    plt.close(fig)
    print(f"saved {path.relative_to(ROOT)}")
    return path


# ---------- 小波工具（週期延伸、Daubechies 4） ----------

DB4_LO = np.array(
    [
        -0.010597401784997278,
        0.032883011666982945,
        0.030841381835986965,
        -0.18703481171888114,
        -0.02798376941698385,
        0.6308807679295904,
        0.7148465705525415,
        0.23037781330885523,
    ]
)
DB4_HI = np.array([(-1) ** (k + 1) * DB4_LO[len(DB4_LO) - 1 - k] for k in range(len(DB4_LO))])


def _analysis(x, filt):
    """週期延伸的濾波加降取樣：y[n] = sum_k f[k] x[(2n + k) mod N]。"""
    n = len(x)
    idx = (2 * np.arange(n // 2)[:, None] + np.arange(len(filt))[None, :]) % n
    return x[idx] @ filt[::-1]


def dwt_step(x):
    return _analysis(x, DB4_LO), _analysis(x, DB4_HI)


def wavedec(x, level):
    """回傳 [A_level, D_level, ..., D_1]，與 pywt.wavedec 的排列相同。"""
    details = []
    a = np.asarray(x, dtype=float)
    for _ in range(level):
        a, d = dwt_step(a)
        details.append(d)
    return [a] + details[::-1]


def wpd_level(x, level):
    """回傳第 level 層所有節點，依頻率由低到高排序。"""
    nodes = [np.asarray(x, dtype=float)]  # 自然順序
    for _ in range(level):
        nxt = []
        for node in nodes:
            a, d = dwt_step(node)
            nxt.extend([a, d])
        nodes = nxt
    return [nodes[k ^ (k >> 1)] for k in range(len(nodes))]


def natural_path(n, level):
    """自然順序索引 n 對應的路徑字串，a = 低通、d = 高通。"""
    return "".join("d" if (n >> (level - 1 - i)) & 1 else "a" for i in range(level))


# ---------- 樹狀圖工具 ----------


def draw_box(ax, x, y, text, w=1.6, h=0.62, face="white", edge=PRIMARY, color=INK, size=9):
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=1.2,
        facecolor=face,
        edgecolor=edge,
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=color, linespacing=1.35)


def draw_edge(ax, x0, y0, x1, y1, label=None, h=0.62):
    ax.plot([x0, x1], [y0 - h / 2, y1 + h / 2], color=MUTED, linewidth=1.0, zorder=0)
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, label, ha="center", va="center", fontsize=8,
                color=ACCENT, backgroundcolor="white")
