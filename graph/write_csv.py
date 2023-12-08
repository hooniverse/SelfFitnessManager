import cv2
import mediapipe as mp
import datetime
import time
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

