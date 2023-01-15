import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#def wyglądu wykresu
def create_bar_graph(name, result):
    helper = np.arange(len(name))
    plt.figure(figsize =(10, 7))
    plt.bar(helper, result, color="red", width=0.4)
    plt.xticks(ticks=helper, labels=name, rotation=15)
    plt.title('Czas zapisu dla poszczególnych pamięci', fontsize=14)
    plt.xlabel('Pamięci', fontsize=14)
    plt.ylabel('Czas zapisu [s]', fontsize=14)
    return plt.gcf()


#layout okna aplikacji
def getLayoutGraph():
    return [[sg.Text('Porównanie wyników')], 
            [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
            [sg.Exit(button_text='Zamknij')]]


#rysowanie wykresów
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def show_graph(names, times):
    layout = getLayoutGraph()
    window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center') 
    draw_figure(window['-CANVAS-'].TKCanvas, create_bar_graph(names, times))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Zamknij':
            break
        
    window.close()