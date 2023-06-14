import PySimpleGUI as sg
import pyttsx3
def gui():
    sg.theme("DarkPurple4")
    result = ""

    layout = [
        [sg.Multiline(result, key='-OUTPUT-', size=(34, 2), expand_y=True, disabled=True)],
        [sg.Button("C", size=(4,1)), sg.Button("PLAY", size=(4,1)), sg.Button("<=", size=(4,1)), sg.Push(), sg.Button("=", size=(4,1))],
        [sg.Button("7", size=(4,1)), sg.Button("8", size=(4,1)), sg.Button("9", size=(4,1)), sg.Push(),sg.Button("*", size=(4,1))],
        [sg.Button("4", size=(4,1)), sg.Button("5", size=(4,1)), sg.Button("6", size=(4,1)), sg.Push(),sg.Button("-", size=(4,1))],
        [sg.Button("1", size=(4,1)), sg.Button("2", size=(4,1)), sg.Button("3", size=(4,1)), sg.Push(),sg.Button("+", size=(4,1))],
        [sg.Push(), sg.Button("0", size=(4,1)), sg.Push(), sg.Button("/", size=(4,1))]
    ]

    window = sg.Window("Calculator", layout)

    while True:
        event, values = window.read()
        print(event, values)

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event in "123456789":
            result += event
            window["-OUTPUT-"].update(result)

        if event == "0":
            if len(result) > 0 and result[-1] not in "+-*/":
                result += event
                window["-OUTPUT-"].update(result)

        if event in "*-+/":
            if len(result) == 0 and event in "+-":
                result += event
            if len(result) > 0 and result[-1] not in "*+-/":
                result += event

            window["-OUTPUT-"].update(result)

        if event == "C":
            result = ""
            window["-OUTPUT-"].update(result)

        if event == "<=":
            result = result[:len(result) - 1]
            window["-OUTPUT-"].update(result)

        if event == "PLAY" and len(result) > 0:
            engine = pyttsx3.init()
            if result[-1] not in "*-+/":
                result = str(eval(result))
                window["-OUTPUT-"].update(result)

            engine.say(result)
            engine.runAndWait()

        if event == "=" and len(result) > 0:
            if result[-1] not in "*-+/":
                result = str(eval(result))
                window["-OUTPUT-"].update(result)

    window.close()


if __name__ == '__main__':
    gui()

