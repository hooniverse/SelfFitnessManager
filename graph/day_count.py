"""
일별 운동 종목별 카운트 수 그려주는 그래프
"""

import pandas as pd
import matplotlib.pyplot as plt
import cv2

def plot_exercise_counts(file_path, selected_date):
    # CSV 파일을 읽어옵니다.
    df = pd.read_csv(file_path)

    # 'Date' 열을 datetime 형식으로 변환합니다.
    df['Date'] = pd.to_datetime(df['Date'])

    # 날짜를 기준으로 데이터를 필터링합니다.
    filtered_data = df[df['Date'].dt.date == pd.to_datetime(selected_date).date()]

    if filtered_data.empty:
        print(f'날짜 {selected_date}에 해당하는 데이터가 없습니다.')
        return

    # 각 운동의 카운트를 계산합니다.
    exercise_counts = {}
    for exercise_type in filtered_data['exercise'].unique():
        count = filtered_data[filtered_data['exercise'] == exercise_type]['Count'].sum()
        exercise_counts[exercise_type] = count

    # 막대 그래프를 그립니다.
    exercise_labels = list(exercise_counts.keys())
    exercise_values = list(exercise_counts.values())

    plt.bar(exercise_labels, exercise_values)
    plt.xlabel('exercise type')
    plt.ylabel('count')
    plt.title(f'{selected_date} exercise count')
    plt.show()

    if cv2.waitKey(1) == ord('q'):
        return

# CSV 파일 경로를 적절히 수정하세요.
file_path = 'exercise_record.csv'

# 년월일을 입력받습니다.
# selected_date = input('조회할 날짜를 입력하세요 (YYYY-MM-DD): ')

# 막대 그래프를 그립니다.
# plot_exercise_counts(file_path, selected_date)
