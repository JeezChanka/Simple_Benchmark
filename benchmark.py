import PySimpleGUI as sg
import time

def start_benchmark():
    #do some stuff
    layout = [[sg.Text('Testowanie urządznia')], 
              [sg.Canvas(size=(1000, 1000), key='-SPINNER-')]]
    
    window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center',size=(300, 150)) 
    return_result = 0
    
    calculate(window)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-BENCHAMRK-END-':
            return_result = values['-BENCHAMRK-END-'] #getting result from benchmark
            break
    
    window.close()
    return return_result


def calculate(window):
    time.sleep(5)
    benchmark_result = 10
    #do calculation here
    window.write_event_value('-BENCHAMRK-END-', benchmark_result) #benchmark_result is result time form benchmark