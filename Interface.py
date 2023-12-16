import PySimpleGUI as sg
import datetime
from graph import day_count

class Interface:
    sg.theme('DarkAmber')

    def main_page(self):
        layout = [
            [sg.Graph((250, 280), (0, 0), (250, 280), key='logo')],
            [sg.Text('모드선택', font=("Arial Bold", 10, "bold")), sg.Radio('트레이닝', key="training", group_id=1),
             sg.Radio('테스트', key="test", group_id=1)],
            [sg.Column(layout=[[sg.Button('기록보기')]], justification='center'), sg.Text('', size=(5, 1)),
             sg.Button('확인')],
        ]

        window = sg.Window('모드 선택', layout, finalize=True)
        window['logo'].draw_image(filename='logo1.png', location=(6.5, 270))

        return window

    def training_page(self):
        layout = [[sg.Text('운동 종목 선택'),
                   sg.Listbox(['Push-Up', 'Pull-Up', 'Squat'], no_scrollbar=True, s=(15, 3), key='type')],
                  [sg.Text('세트 개수(자연수 입력)'), sg.Input(s=15, key='set')],
                  [sg.Text('세트 당 개수(자연수 입력)'), sg.Input(s=15, key='reps_per_set')],
                  [sg.Text('쉬는 시간(초 단위 입력)'), sg.Input(s=15, key='break_time')],
                  [sg.Column(layout=[[sg.Button('이전으로')]], justification='center'), sg.Text('', size=(7, 1)),
                   sg.Button('확인')],
                  ]

        return sg.Window('training_page', layout)

    def test_page(self):
        layout = [[sg.Text('테스트 종목 선택'),
                   sg.Listbox(['Push-Up', 'Pull-Up', 'Squat'], no_scrollbar=True, s=(15, 3), key='type')],
                  [sg.Text('목표 시간(초 단위 입력)'), sg.Input(s=15, key='goal_time')],
                  [sg.Text('목표 개수(자연수 입력)'), sg.Input(s=15, key='goal_number')],
                  [sg.Column(layout=[[sg.Button('이전으로')]], justification='center'), sg.Text('', size=(7, 1)),
                   sg.Button('확인')],
                  ]

        return sg.Window('test_page', layout)

    def report_choose_page(self):
        layout = [[sg.Button("트레이닝 기록 보기"), sg.Button("테스트 기록 보기")],
                  [sg.Column(layout=[[sg.Button('이전으로')]], justification='right')],
                  ]

        return sg.Window('report_choose_page', layout)

    def training_report_page(self):
        layout = [[sg.Text("날짜를 선택하세요:"), sg.InputText(key="date", size=(20, 2), enable_events=True),
                   sg.CalendarButton("날짜 선택", target="date", format="%Y-%m-%d")],
                  [sg.Image(key='output')],
                  [sg.Column(layout=[[sg.Button('이전으로')]], justification='right')],
                  ]

        return sg.Window('training_report_page', size=(600, 600)).Layout(layout)

    def test_report_page(self):
        layout = [[sg.Text("날짜를 선택하세요:"), sg.InputText(key="date", size=(20, 2), enable_events=True),
                   sg.CalendarButton("날짜 선택", target="date", format="%Y-%m-%d")],
                  [sg.Image(key='output_test')],
                  [sg.Column(layout=[[sg.Button('이전으로')]], justification='right')],
                  ]

        return sg.Window('test_report_page', size=(1800, 500), location=(0, 0)).Layout(layout)

    def run(self):
        user_input = {}

        window = self.main_page()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            elif event == '확인':
                if values['training']:
                    user_input['mode'] = 'training'
                    window.close()

                    window = self.training_page()
                    event, values = window.read()

                    if event == '확인':
                        user_input['type'] = values['type']
                        user_input['set_count'] = values['set']
                        user_input['reps_per_set'] = values['reps_per_set']
                        user_input['break_time'] = values['break_time']
                        window.close()

                    elif event == '이전으로':
                        window.close()
                        window = self.main_page()
                        event, values = window.read()


                elif values['test']:
                    user_input['mode'] = 'test'
                    window.close()
                    window = self.test_page()
                    event, values = window.read()

                    if event == '확인':
                        user_input['type'] = values['type']
                        user_input['goal_time'] = values['goal_time']
                        user_input['goal_number'] = values['goal_number']
                        window.close()

                    elif event == '이전으로':
                        window.close()
                        window = self.main_page()
                        event, values = window.read()

            elif event == '기록보기':
                window.close()
                window = self.report_choose_page()

                while True:
                    event, values = window.read()

                    if event == sg.WIN_CLOSED or event == 'Cancel':
                        break

                    if event == '트레이닝 기록 보기':
                        window.close()
                        window = self.training_report_page()
                        event, values = window.read()

                        while True:
                            event, values = window.read()

                            if event == sg.WIN_CLOSED:
                                break

                            if event == '이전으로':
                                window.close()
                                window = self.report_choose_page()
                                event, values = window.read()
                                break

                            elif event == "date":
                                selected_date_str = values["date"]
                                try:
                                    selected_date = datetime.datetime.strptime(selected_date_str, "%Y-%m-%d").date()

                                    day_count.plot_exercise_counts("exercise_record.csv", selected_date)
                                    path = f"graph_pictures\{selected_date}_exercise_count.png"
                                    window["output"].update(filename=path)

                                except ValueError:
                                    sg.popup_error("올바르지 않은 날짜 형식입니다. 날짜를 다시 입력하세요.")


                    elif event == '테스트 기록 보기':
                        window.close()
                        window = self.test_report_page()
                        event, values = window.read()

                        while True:
                            event, values = window.read()

                            if event == sg.WIN_CLOSED:
                                break

                            if event == '이전으로':
                                window.close()
                                window = self.report_choose_page()
                                event, values = window.read()
                                break

                            elif event == "date":
                                selected_date_str = values["date"]
                                try:
                                    selected_date = datetime.datetime.strptime(selected_date_str, "%Y-%m-%d").date()

                                    # day_count.plot_exercise_counts("exercise_record.csv", selected_date)
                                    path = f"graph_pictures\\test_graph\\{selected_date}_Merged_Image.png"
                                    window["output_test"].update(filename=path)

                                except ValueError:
                                    sg.popup_error("올바르지 않은 날짜 형식입니다. 날짜를 다시 입력하세요.")

                    elif event == '이전으로':
                        window.close()
                        window = self.main_page()
                        event, values = window()
                        break

        window.close()
        return user_input

    def end(self):
        layout = [[sg.Text("운동이 종료되었습니다.", font=("Arial Bold", 13, "bold"))],
                  ]

        window = sg.Window('end_page', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
        window.close()