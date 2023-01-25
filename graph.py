import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import connector

#def wyglądu wykresu
def create_bar_graph(name, result):
    helper = np.arange(len(name))
    plt.figure(figsize =(10, 7))
    plt.bar(helper, result, color="red", width=0.4)
    plt.xticks(ticks=helper, labels=name, rotation=15)
    plt.title('Porównanie prędkości zapisu (więcej = lepiej)', fontsize=14)
    plt.xlabel('Pamięci', fontsize=14)
    plt.ylabel('Prędkość zapisu [MB/s]', fontsize=14)
    return plt.gcf()


#layout okna aplikacji
def getLayoutGraph():
    return [[sg.Text('Porównanie wyników')], 
            [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
            [sg.Input(key='-NAME-', size=(20,60)),sg.Button(key='-SAVE-',button_text="Zapisz wynik", pad=(10,10)),sg.Exit(button_text='Zamknij')]]


#rysowanie wykresów
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
    
    
def save_handler(cnx, name, final_result, window):
    connector.InsertDataHandler(cnx, (name, final_result))
    window['-SAVE-'].update(disabled=True)
    window['-NAME-'].update(disabled=True)


def show_graph(names, times, cnx):
    layout = getLayoutGraph()
    window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center') 
    draw_figure(window['-CANVAS-'].TKCanvas, create_bar_graph(names, times))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Zamknij':
            break
        elif event == '-SAVE-':
            save_handler(cnx, values['-NAME-'], times[9], window)
    
    window['-SAVE-'].update(disabled=False)
    window['-NAME-'].update(disabled=False)    
    window.close()
    