from matplotlib import pyplot as plt
from collections.abc import Iterable

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

def my_plot(x_vect, plots_dict, line_widths = [], styles = [], leg_ncol = 1, stem = False, res = 150):
    if styles == []:
        styles = ['']*len(plots_dict)
    if line_widths == []:
        line_widths = [1.5]*len(plots_dict)
    plt.figure(figsize = [6.4,1], dpi=res, facecolor='#FAF4F6')
    ax = plt.axes()
    ax.set_facecolor("#FAF4F6")
    plt.grid()
    if stem:
        for name, style in zip(plots_dict, styles):
            plt.stem(x_vect, plots_dict[name], linefmt = style, markerfmt = style + 'o', label=name, basefmt = ' ')
    else:
        if isinstance(x_vect[0], Iterable):
            for x_axs, name, style, width in zip(x_vect, plots_dict, styles, line_widths):
                plt.plot(x_axs, plots_dict[name], style, linewidth = width, label=name)
        else:
            for name, style, width in zip(plots_dict, styles, line_widths):
                plt.plot(x_vect, plots_dict[name], style, linewidth = width, label=name)
    if (len(plots_dict)>1):
        plt.legend(loc = 'lower center', ncol=leg_ncol , bbox_to_anchor=(0.5, 1))
    else:
        plt.title(list(plots_dict.keys())[0])
