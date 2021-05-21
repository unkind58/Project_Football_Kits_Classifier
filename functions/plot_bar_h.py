import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_barh(n_plot: int, data, titles):
    fig, ax = plt.subplots(n_plot, 1, figsize=(18, 12), sharex=True)
    for i in range(n_plot):
        sns.barplot(
            x=data[i][0], y=data[i][1], orient="h", ax=ax[i], edgecolor="mediumseagreen"
        )
        if i == 0:
            ax[i].xaxis.set_tick_params(labelbottom=True)
        ax[i].axvline(int(data[i][0].mean()), zorder=1, linewidth=0.5, color="tomato")
        ax[i].set_xlabel(None)
        [ax[i].spines[loc].set_visible(False) for loc in ["top", "right"]]
        ax[i].spines["left"].set_color("mediumseagreen")
        ax[i].spines["bottom"].set_color("mediumseagreen")
    for i, title in enumerate(titles):
        ax[i].set_title(title, fontsize=15)
        # Make some labels.
        rects = ax[i].patches
        labels = data[i][0].tolist()

        for rect, label in zip(rects, labels):
            width = rect.get_width()
            ax[i].text(
                0.985 * rect.get_width(),
                rect.get_y() + 0.5 * rect.get_height(),
                label,
                ha="center",
                va="center",
                fontsize="small",
            )
    plt.tight_layout(pad=5.0)
