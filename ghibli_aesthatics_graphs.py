import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
from PIL import Image

# === STYLE SETUP ===
def set_ghibli_style():
    mpl.rcParams.update({
        'figure.facecolor': '#e8f1e7',
        'axes.facecolor': 'none',
        'savefig.facecolor': '#e8f1e7',

        'axes.edgecolor': '#282011',
        'axes.linewidth': 0.8,
        'axes.prop_cycle': mpl.cycler('color', ['#3c1e1e']),

        'grid.color': '#d8c3a5',
        'grid.linestyle': '-',
        'grid.linewidth': 0.5,
        'axes.grid': False,

        'font.family': 'EB Garamond',
        'font.size': 22,

        'xtick.color': '#020124',
        'ytick.color': '#3a2e1e',
        'xtick.major.size': 6,
        'ytick.major.size': 6,
        'xtick.major.width': 1.5,
        'ytick.major.width': 1.5,

        'legend.frameon': True,
        'legend.facecolor': '#fef1d1',
        'legend.edgecolor': '#3a2e1e',
        'legend.fancybox': True,
        'legend.fontsize': 15,
    })

# === BACKGROUND IMAGE ===
def add_watercolor_background(fig, image_path="watercolor_bg.png", alpha=1.0):
    if not os.path.exists(image_path):
        print(f"Background image not found: {image_path}")
        return

    img = Image.open(image_path)
    width, height = fig.canvas.get_width_height()
    img = img.resize((width, height))
    img_array = np.asarray(img)
    fig.figimage(img_array, xo=0, yo=0, alpha=alpha, zorder=-100)

# === PLOT FUNCTION ===
def plot_ghibli_bar_chart():
    # Load font if available
    font_path = "EBGaramond-Regular.ttf"
    if os.path.exists(font_path):
        fm.fontManager.addfont(font_path)
        plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()

    set_ghibli_style()
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    # Data
    categories = [
    'Operational\nEfficiency',
    'Market\nPenetration',
    'Customer\nSatisfaction',
    'Revenue\nGrowth',
    'Employee\nEngagement'
      ]

    values = [7.5, 6.2, 8.1, 5.9, 6.8]

    colors = ['#974228', '#4a8a96', '#5a515d', '#d1901d', '#68756a']
    edge_colors = ['#282011', '#282011', '#282011', '#282011', '#282011']

    # Bar chart
    bars = ax.bar(categories, values, width=0.6, color=colors, edgecolor=edge_colors, linewidth=2.5)

    # Add grainy white noise to each bar
    for bar in bars:
        x, width, height = bar.get_x(), bar.get_width(), bar.get_height()
        x_noise = np.random.uniform(x, x + width, 3000)
        y_noise = np.random.uniform(0, height, 3000)
        alpha_noise = np.random.uniform(0.03, 0.02, 3000)
        ax.scatter(x_noise, y_noise, color='white', s=1, alpha=alpha_noise, zorder=3)

    # Value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{height}',
                ha='center', va='bottom', fontsize=21, color='#3a2e1e')

    # Labels and title
    #ax.set_title("Spirits of the Emotion", fontsize=30, pad=20)
    #ax.set_xlabel("Emotion", fontsize=18, labelpad=10)
    #ax.set_ylabel("Intensity", fontsize=18, labelpad=10)
    ax.set_title("Impact Assessment of Strategic Initiatives", fontsize=28, pad=20)
    ax.set_xlabel("Strategic Pillar", fontsize=18, labelpad=10)
    ax.set_ylabel("Impact Score", fontsize=18, labelpad=10)


    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Background image
    add_watercolor_background(fig)

    plt.tight_layout()
    plt.show()

# === RUN SCRIPT ===
if __name__ == "__main__":
    plot_ghibli_bar_chart()
