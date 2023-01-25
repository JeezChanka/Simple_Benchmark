import PySimpleGUI as sg
import mariadb
import connector
import graph
import main_window
import benchmark

# Database data for XAMPP MariaDB
cnx = mariadb.connect(user='server713288_benchmark',
                      password='OeskOesk1!',
                      host='mariadb106.server713288.nazwa.pl',
                      port=3306,
                      database='server713288_benchmark')

connector.CreateTableHandler(cnx)
#connector.InsertDataHandler(cnx, ("test1", 11))
results = connector.GetDataHandler(cnx)
ids, names, times = zip(*results)

layout = main_window.getLayoutMainWindow()
window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center', size=(300, 200))
#graph.draw_figure(window['-CANVAS-'].TKCanvas, graph.create_bar_graph(names, times))

selected_drive = ''
new_result = 1

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Wyjście':
        # window.write_event_value('Zamknij')
        break
    elif event == 'Start':
        window['Start'].update(disabled=True)
        window['-DISKS-'].update(disabled=True)
        window['Wyjście'].update(disabled=True)

        selected_drive = values['-DISKS-']
        selected_block_count = values['-BLOCK_COUNT-']

        new_result = benchmark.start_benchmark(selected_drive, selected_block_count)

        # print(new_result)

        names = names[:-1] + ('Twój wynik',)
        times = times[:-1] + (new_result,)

        print(names)

        graph.show_graph(names, times, cnx)
        results = connector.GetDataHandler(cnx)

        ids, names, times = zip(*results)

        window['Start'].update(disabled=False)
        window['-DISKS-'].update(disabled=False)
        window['Wyjście'].update(disabled=False) 
    elif event == 'Odśwież':
        main_window.main_refresh(window)   
        window.refresh()


window.close()
    
# Close connection

cnx.close()