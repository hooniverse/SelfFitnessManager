import PySimpleGUI as sg


class Interface:
    sg.theme('DarkAmber')


    def main_page(self):
        layout = [[sg.Graph((250, 280), (0, 0), (250, 280), key='logo')],
                  [sg.Text('모드선택', font=("Arial Bold", 10, "bold")), sg.Radio('트레이닝', key="training", group_id=1),
                   sg.Radio('테스트', key="test", group_id=1)],
                  [sg.Column(layout=[[sg.Button('확인')]], justification='center')]
                  ]

        window = sg.Window('모드 선택', layout, finalize=True)
        window['logo'].draw_image(filename='logo1.png', location=(6.5, 270))

        return window

    def training_page(self):
        layout = [[sg.Text('운동 종목 선택'), sg.Listbox(['Pull-Up', 'Push-Up'], no_scrollbar=True, s=(15, 2), key='type')],
                  [sg.Text('세트 개수(자연수 입력)'), sg.Input(s=15, key='set')],
                  [sg.Text('세트 당 개수(자연수 입력)'), sg.Input(s=15, key='reps_per_set')],
                  [sg.Text('쉬는 시간(초 단위 입력)'), sg.Input(s=15, key='break_time')],
                  [sg.Column(layout=[[sg.Button('확인')]], justification='center')],
                  ]

        return sg.Window('training_page', layout)

    def test_page(self):
        layout = [[sg.Text('테스트 종목 선택'), sg.Listbox(['Pull-Up', 'Push-Up'], no_scrollbar=True, s=(15, 2), key='type')],
                  [sg.Text('목표 시간(초 단위 입력)'), sg.Input(s=15, key='goal_time')],
                  [sg.Text('목표 개수(자연수 입력)'), sg.Input(s=15, key='goal_number')],
                  [sg.Column(layout=[[sg.Button('확인')]], justification='center')],
                  ]

        return sg.Window('test_page', layout)

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

        window.close()
        return user_input


