"""
모든 운동에 대해 날짜 및 시간, 운동 종목, 카운트를 저장하는 코드
"""
import datetime
import csv
import pandas as pd
def write_csv(current_exercise, total_count):

    csv_file_path = "exercise_record.csv"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Current Exercise', 'Total Count'])
        df = pd.DataFrame(columns=['Date', 'Current Exercise', 'Total Count'])

    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, current_exercise, total_count])

