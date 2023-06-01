from matplotlib import pyplot as plt

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

def my_plot(x_vect, plots_dict, line_widths = [], styles = [], leg_ncol = 1, stem = False):
    if styles == []:
        styles = ['-']*len(plots_dict)
    if line_widths == []:
        line_widths = [1.5]*len(plots_dict)
    plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
    ax = plt.axes()
    ax.set_facecolor("#FAF4F6")
    plt.grid()
    if stem:
        for name in plots_dict:
            plt.stem(x_vect, plots_dict[name], label=name, basefmt = ' ')
    else:
        for name, style, width in zip(plots_dict, styles, line_widths):
            plt.plot(x_vect, plots_dict[name], style, linewidth = width, label=name)
    plt.legend(loc = 'lower center', ncol=leg_ncol , bbox_to_anchor=(0.5, 1))
