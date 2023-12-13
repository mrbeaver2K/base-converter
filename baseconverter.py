import PySimpleGUI as sg

symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def to_quantity(value, radix):
    radix = int(radix)
    quantity = 0
    for i in tuple(value):
        quantity = quantity * radix + symbols.index(i) 
    return quantity

def to_value(quantity, radix):
    radix = int(radix)
    remainder = []
    place = 0
    while quantity != 0:
        remainder.append(quantity % radix)
        quantity //= radix
        place += 1
    out = []
    for i in range(1, place + 1):
        out.append(symbols[remainder[place - i]])
    return "".join(out)

sg.theme("Gray Gray Gray")
layout = [[sg.Text("Base Converter Program (DON'T INPUT FLOATS)"), sg.Push(), sg.Text("Base Input V    ")],
        [sg.Text("Input:"), sg.Input(key="input", pad=(11, 0)), sg.Input(key="frombasein", size=2)],
        [sg.Text("Output:"), sg.Input(key="output", disabled=True, pad=0), sg.Input(key="tobasein", size=2, pad=(16, 0))],
        [sg.Button("60"), sg.Button("Close"), sg.Button("Dump"), sg.Button("Swap")],
        [sg.Text("Loading Bay for Symbols:")],
        [sg.Multiline(key="symbolsin", size=(32, 6), default_text="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")]]
window = sg.Window("Base Converter", layout)

while True:
    event, values = window.read()
    if event in ("Close", sg.WIN_CLOSED):
        break
    if event == "60":
        value = to_value(to_quantity(values["input"], values["frombasein"]), values["tobasein"])
        window["output"].update(value)
    if event == "Dump":
        symbols = values["symbolsin"]
        print(symbols)
    if event == "Swap":
        window["input"].update(value)
        temp = values["frombasein"]
        window["frombasein"].update(values["tobasein"])
        window["tobasein"].update(temp)
        window["output"].update("Press 60 to recalulate")
        del temp
window.close()
