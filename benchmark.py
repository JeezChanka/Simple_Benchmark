import PySimpleGUI as sg
import time

import benchmark_run


def start_benchmark(selected_drive, selected_block_count):
    #do some stuff
    layout = [[sg.Text('Testowanie urządzenia')],
              [sg.Canvas(size=(1000, 1000), key='-SPINNER-')]]
    
    window = sg.Window('OESK Benchmark', layout, finalize=True, element_justification='center',size=(300, 150)) 
    return_result = 0
    
    calculate(window, selected_drive, selected_block_count)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-BENCHAMRK-END-':
            return_result = values['-BENCHAMRK-END-'] #getting result from benchmark
            break
    
    window.close()
    return return_result


def calculate(window, selected_drive, selected_block_count):
    # time.sleep(5)
    # benchmark_result = 10

    selected_block_count = int(selected_block_count)

    total_test_size = 1024 * 1024 * 1024  # 1GB
    block_size_bytes = total_test_size // selected_block_count

    write_speed_MB = benchmark_run.write_test(selected_drive + 'testy', block_size_bytes, selected_block_count)

    # do calculation here
    window.write_event_value('-BENCHAMRK-END-', write_speed_MB)  # benchmark_result is result time form benchmark
