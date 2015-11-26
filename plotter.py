def plotter(x, funcs):
    fig, axs = plt.subplots(len(funcs), 1)
    for ax, func in zip(axs, funcs):
        ax.scatter(x, func(x))
    return fig, axs
figg = plotter(10*np.random.random(10), [np.sin, lambda arr: [a**2 for a in arr]])
