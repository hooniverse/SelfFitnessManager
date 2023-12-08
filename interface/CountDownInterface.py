import PySimpleGUI as sg
import time


class CountDownInterface:

    def __init__(self):
        pass

    def countdown(self, duration):
        layout = [
            [sg.Text("", key="second", font=('Helvetica', 200), justification='center', size=(10,1))],
        ]

        window_size = (400, 300)

        self.window = sg.Window("카운트다운 타이머", layout, size=window_size)

        while True:
            event, values = self.window.read(timeout=1000)

            if event == sg.WINDOW_CLOSED:
                break

            if self.break_time_countDown(duration):
                break

        self.window.close()

    def break_time_countDown(self, duration):
        time_text = self.window["second"]

        for i in range(duration, -1, -1):
            time_text.update(str(i))
            self.window.refresh()
            time.sleep(1)


        return True

