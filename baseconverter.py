import PySimpleGUI as sg

def to_quantity(value, radix):
    print(f"to_quantity({value=}, {radix=})")
    return 42

def to_value(quantity, radix):
    print(f"to_value({quantity=}, {radix=}")
    return 42

sg.theme("Gray Gray Gray")
layout = [[sg.Text("Base Converter Program (DON'T INPUT FLOATS)"), sg.Push(), sg.Text("Base Input V    ")],
        [sg.Text("Input:"), sg.Input(key="input", pad=(11, 0)), sg.Input(key="frombasein", size=2)],
        [sg.Text("Output:"), sg.Input(key="output", disabled=True, pad=0), sg.Input(key="tobasein", size=2, pad=(16, 0))],
        [sg.Button("60"), sg.Button("Close")],
        [sg.Text("Loading Bay for Symbols:")],
        [sg.Multiline(key="symbolsin", size=(32, 6), default_text=str(list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")))]]
window = sg.Window("Base Converter", layout)

while True:
    event, values = window.read()
    if event in ("Close", sg.WIN_CLOSED):
        break
    if event == "60":
        value = to_value(to_quantity(values["input"], values["frombasein"]), values["tobasein"])
        window["output"].update(value)
window.close()
