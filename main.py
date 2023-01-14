import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from connector import DataHandler

DataHandler()
#dane źródłowe   
year = ["ADATA","Kingstone","WD","Gigabyte","Intel","Goodram","HyperX","Patriot","Samsung","Odra"]
unemployment_rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#def wyglądu wykresu
def create_bar_graph(year, unemployment_rate):
    plt.figure(figsize =(10, 7))
    plt.bar(year, unemployment_rate, color='red', width=0.4)
    plt.title('Czas zapisu dla poszczególnych pamięci', fontsize=14)
    plt.xlabel('Pamięci', fontsize=14)
    plt.ylabel('Czas zapisu [s]', fontsize=14)
    return plt.gcf()
#layout okna aplikacji
layout = [[sg.Text('Porównanie wyników')],
          [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
          [sg.Exit(button_text="Wyjście")]]
#rysowanie wykresów
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

#nazwa okna
window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center') 

draw_figure(window['-CANVAS-'].TKCanvas, create_bar_graph(year, unemployment_rate))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()