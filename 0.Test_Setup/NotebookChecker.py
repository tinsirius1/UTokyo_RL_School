import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interactive

def NotebookChecker():
    w_slider = widgets.IntSlider(value=0, min=0, max=10, step=1, description='Omega',
                                                continuous_update=False)
    def f(change):
        plt.close('all')
        fig = plt.figure(figsize=(5, 5))
        fig.canvas.toolbar_position = 'top'
        ax = plt.gca()

        x = np.linspace(1, 2 * np.pi, 100)
        y = np.sin(x*change)
        ax.plot(x, y)
        if change == 10:
            print('Isaac Asimov')
        plt.show()

    interactive_plot = interactive(f, change=w_slider)
    return interactive_plot