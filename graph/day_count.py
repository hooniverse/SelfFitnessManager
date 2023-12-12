"""
일별 운동 기록을 운동 종목 별로 카운트 합을 그래프로 출력 및 저장
운동 기록 보는 인터페이스에서 사용
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_exercise_counts(file_path, selected_date):

    df = pd.read_csv(file_path)


    df['Date'] = pd.to_datetime(df['Date'])


    filtered_data = df[df['Date'].dt.date == pd.to_datetime(selected_date).date()]

    if filtered_data.empty:
        print(f'날짜 {selected_date}에 해당하는 데이터가 없습니다.')
        return


    exercise_counts = {}
    for exercise_type in filtered_data['exercise'].unique():
        count = filtered_data[filtered_data['exercise'] == exercise_type]['Count'].sum()
        exercise_counts[exercise_type] = count


    exercise_labels = list(exercise_counts.keys())
    exercise_values = list(exercise_counts.values())


    output_folder = 'graph_pictures'
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f'{selected_date}_exercise_count.png')

    plt.bar(exercise_labels, exercise_values)
    plt.xlabel('exercise type')
    plt.ylabel('count')
    plt.title(f'{selected_date} exercise count')
    

    plt.savefig(output_path)
    plt.close()