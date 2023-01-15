import PySimpleGUI as sg
import mariadb
from connector import CreateTableHandler, GetDataHandler, InsertDataHandler
import graph

# Database data for XAMPP MariaDB
cnx = mariadb.connect(user='root', 
                    password='',
                    host='localhost',
                    port=3306,
                    database='benchmark')

CreateTableHandler(cnx)
results = GetDataHandler(cnx)
#InsertDataHandler(cnx, ("test1", 11))
results = GetDataHandler(cnx)
ids, names, times = zip(*results)

layout = graph.getLayoutGraph()
window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center') 
graph.draw_figure(window['-CANVAS-'].TKCanvas, graph.create_bar_graph(names, times))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Wyjście':
        break

window.close()
    
# Close connection

cnx.close()