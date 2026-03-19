"""Plotting helpers."""
import matplotlib.pyplot as plt


def setup_plot_style():
    """Apply the project's default matplotlib style."""
    try:
        plt.style.use(["science", "no-latex"])
    except Exception:
        pass
    plt.rcParams.update({
        "axes.spines.right": False,
        "axes.spines.top": False,
    })


def save_figure(fig, path, dpi=300, **kwargs):
    """Save a figure to *path*, creating parent directories as needed."""
    from pathlib import Path
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=dpi, bbox_inches="tight", **kwargs)
    print(f"Saved: {p.resolve()}")
