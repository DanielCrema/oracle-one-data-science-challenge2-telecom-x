# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

def pie_plot(title, labels, sizes):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    colors = sns.color_palette('pastel')[0:len(labels)]

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=list(labels),
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=1.0)  # Full pie (unlike donut)
    )

    for text in texts + autotexts:
        text.set_color('black')
        text.set_fontsize(12)

    plt.title(title, fontsize=16)

    return fig

def donut_plot(title, labels, sizes):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    colors = sns.color_palette('pastel')[0:len(labels)]

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=list(labels),
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=0.4),
    )

    for text in texts + autotexts:
        text.set_color('black')
        text.set_fontsize(12)

    plt.title(title, fontsize=16)

    return fig

def bar_plot(title, x, y, xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = sns.color_palette('pastel')

    sns.barplot(x=x, y=y, palette=colors, ax=ax)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    sns.despine()

    return fig

def barh_plot(title, x, y, xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = sns.color_palette('pastel')

    sns.barplot(x=x, y=y, palette=colors, ax=ax, orient='h')

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    sns.despine()

    return fig

def line_plot(title, x, y, xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(8, 6))
    color = sns.color_palette('pastel')[0]

    sns.lineplot(x=x, y=y, ax=ax, color=color, marker='o')

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    sns.despine()

    return fig

def bar_of_pie_plot(
    title_pie,
    title_bar,
    pie_sizes,
    pie_labels,
    bar_sizes,
    bar_labels,      
):
    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    # Style
    colors = sns.color_palette('pastel')
    pie_colors = colors[:len(pie_sizes)]
    bar_colors = colors[:len(bar_sizes)]

    # pie chart parameters
    explode = [0.1] + [0] * (len(pie_sizes) - 1)
    # rotate so that first wedge is split by the x-axis
    angle = -67.5 * pie_sizes[0]
    wedges, *_ = ax1.pie(pie_sizes, autopct='%1.1f%%', startangle=angle,
                        labels=pie_labels, explode=explode, colors=pie_colors)
    ax1.set_title(title_pie)

    # bar chart parameters
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(bar_sizes, bar_labels)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C1', label=label,
                    alpha=0.1 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height / sum(bar_sizes):.0%}"], label_type='center')

    ax2.set_title(title_bar)
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(bar_sizes)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, (1 - sum(bar_sizes))), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color((0, 0, 0))
    con.set_linewidth(2)
    ax2.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 1), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color((0, 0, 0))
    ax2.add_artist(con)
    con.set_linewidth(2)