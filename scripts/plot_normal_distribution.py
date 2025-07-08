import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "course_materials" / "img"
OUTPUT_FILE = OUTPUT_DIR / "norm.png"


def plot_normal_distribution(ax, x, mu, sigma, **kwargs):
    y = norm.pdf(x, mu, sigma)
    return ax.plot(x, y, **kwargs)


if __name__ == "__main__":
    x = np.linspace(-4, 4, 300)
    f, ax = plt.subplots()
    for sigma in [0.4, 1.0]:
        label = f"$\\sigma = {sigma}$"
        line = plot_normal_distribution(ax, x, 0, sigma, label=label)
    ax.set(
        xlabel="$y_{dep}-\\hat{y}_{dep}$",
        ylabel="$N(y_{dep}\\mid\\hat{y}_{dep},\\sigma)$",
    )
    ax.legend(frameon=False)
    f.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=300)
