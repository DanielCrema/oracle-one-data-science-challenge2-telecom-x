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

def pie_plot(title, labels, sizes, palette='pastel'):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    colors = sns.color_palette(palette)[0:len(sizes)]

    wedges, texts, autotexts = ax.pie( # type: ignore
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

def donut_plot(title, labels, sizes, palette='pastel'):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    colors = sns.color_palette(palette)[0:len(labels)]

    wedges, texts, autotexts = ax.pie( # type: ignore
        sizes,
        labels=list(labels),
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=0.5),
    )

    for text in texts + autotexts:
        text.set_color('black')
        text.set_fontsize(12)
    
    for autotext in autotexts:
        x, y = autotext.get_position()
        autotext.set_position((x * 1.2, y * 1.2))

    
    plt.title(title, fontsize=16)

    return fig

def bar_plot(title, legend_title, x, y, xlabel='', ylabel='', palette='pastel'):
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = sns.color_palette(palette)[0:len(y)]

    sns.barplot(x=x, y=y, palette=colors, hue=y, ax=ax)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title=legend_title)
    sns.despine()

    return fig

def barh_plot(title, x, y, xlabel='', ylabel='', xlim=(0, 0), palette='pastel'):
    new_xlim = ((min(x) * 0.9, max(x) * 1.1) if xlim == (0, 0) else (xlim[0], xlim[1]))
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = sns.color_palette(palette)[0:len(x)]

    sns.barplot(x=x, y=y, palette=colors, hue=y, ax=ax, orient='h')

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_xlim(new_xlim[0], new_xlim[1])
    sns.despine()

    for i, v in enumerate(x):
        ax.text(v + (max(x) * 0.01), i, f'{v:,}', va='center', fontsize=10, color='black')

    return fig

def line_plot(title, x, y, xlabel='', ylabel='', palette='pastel'):
    fig, ax = plt.subplots(figsize=(8, 6))
    color = sns.color_palette(palette)[0]

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
    palette='pastel',
    double_color_bar=False  
):
    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    if double_color_bar:
        box = ax1.get_position()
        ax1.set_position([box.x0, box.y0 + 0.2, box.width, box.height])
    
    # pie chart parameters
    pie_colors = sns.color_palette(palette)[:len(pie_sizes)]
    explode = [0.06] + [0] * (len(pie_sizes) - 1)
    # rotate so that first wedge is split by the x-axis
    angle = -67.5 * pie_sizes[0]
    radius = 0.8 if double_color_bar else 1.0
    wedges, *_ = ax1.pie(pie_sizes, autopct='%1.1f%%', startangle=angle,
                        labels=pie_labels, explode=explode, colors=pie_colors, radius=radius)
    if double_color_bar:
        ax1.text(0.5, -0.2, title_pie, fontsize=16, ha='center', transform=ax1.transAxes)
    else:
        ax1.set_title(title_pie, fontsize=16)

    # bar chart parameters
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    bar_colors = ['C1', 'C0']
    for j, (height, label) in enumerate(reversed([*zip(bar_sizes, bar_labels)])):
        bottom -= height
        if double_color_bar:
            bc = ax2.bar(0, height, width, bottom=bottom, color=bar_colors[j], label=label,
                    alpha=0.1 + 0.25)
        else:
            bc = ax2.bar(0, height, width, bottom=bottom, color=bar_colors[0], label=label,
                    alpha=0.1 + 0.25 * j)
        percentage = height / sum(bar_sizes) * 100
        label = f"{percentage:.1f}%" if percentage % 1 != 0 else f"{int(percentage)}%"
        ax2.bar_label(bc, labels=[label], label_type='center')

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
    if double_color_bar:
        con = ConnectionPatch(xyA=(-width / 2, (1 - bar_sizes[1])), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    else:
        con = ConnectionPatch(xyA=(-width / 2, (1 - bar_height)), coordsA=ax2.transData,
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

    return fig

def nested_pie_plot(title, vals, inner_labels, outer_labels, subtitle=""):
    def format_texts(texts, autotexts, fontsize=11, position=1.4):
        for text in texts + autotexts:
            text.set_color('black')
            text.set_fontsize(fontsize)

        for autotext in autotexts:
            x, y = autotext.get_position()
            autotext.set_position((x * position, y * position))
    
    if isinstance(vals, list):
        vals_sum = np.array([float(sum(val)) for val in vals])
        vals_flatten = np.array([float(value) for array in vals for value in array])
    elif isinstance(vals, np.ndarray):
        vals_sum = vals.sum(axis=1)
        vals_flatten = vals.flatten()
    else:
        raise ValueError("vals must be a list or a numpy array")

    fig, ax = plt.subplots(figsize=(6, 6))

    size = 0.3
    # vals = np.array([[60., 32.], [37., 40.], [29., 10.]]) # Example data

    blues = plt.get_cmap('Blues')
    oranges = plt.get_cmap('Oranges')
    outer_colors = [blues(0.55), oranges(0.55)]
    inner_colors = [blues(0.125), blues(0.25), blues(0.375), oranges(0.375), oranges(0.25), oranges(0.125)]

    wedges_outer, texts_outer, autotexts_outer = ax.pie( # type: ignore
        vals_sum,
        radius=1,
        colors=outer_colors,
        labels=outer_labels,
        wedgeprops=dict(width=size, edgecolor='w'),
        autopct='%1.1f%%',
        startangle=-35
        )
    format_texts(texts_outer, autotexts_outer)

    wedges_inner, texts_inner, autotexts_inner = ax.pie( # type: ignore
        vals_flatten, radius=1-size,
        colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor='w'),
        autopct='%1.1f%%',
        startangle=-35
    )
    format_texts(texts_inner, autotexts_inner, fontsize=9, position=1.3)

    # outer_labels = ['a', 'b', 'c'] # Example labels
    # inner_labels = ['d', 'e', 'f', 'g', 'h', 'i'] # Example labels
    # all_wedges = wedges_outer + wedges_inner
    # all_labels = outer_labels + inner_labels
    ax.legend(wedges_inner, inner_labels, loc='center left', bbox_to_anchor=(1, 0.5), title="Legenda")
    plt.title(title, fontsize=16)
    if subtitle != "":
        plt.figtext(0.7, 0.12, subtitle, ha='center', fontsize=12)

    return fig