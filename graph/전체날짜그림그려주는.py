"""
운동, 날짜별로 카운트 그려주는것
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator

# CSV 파일 경로
csv_file_path = "exercise_record.csv"

# CSV 파일에서 데이터 로드
df = pd.read_csv(csv_file_path)

# 'Date' 열을 datetime 타입으로 변환하여 년, 월, 일만 추출
df['Date'] = pd.to_datetime(df['Date']).dt.date

# 날짜별로 그룹화하고 합계 계산
df_grouped = df.groupby(['Date', 'exercise']).sum().reset_index()

# 날짜를 기준으로 정렬
df_grouped = df_grouped.sort_values(by=['Date', 'exercise'])

# 운동 종류 추출
exercise_types = df['exercise'].unique()

# 그래프 그리기
fig, axs = plt.subplots(len(exercise_types), 1, figsize=(12, 3 * len(exercise_types)), sharex=True)

for i, exercise_type in enumerate(exercise_types):
    # 운동 종류별로 데이터 필터링
    df_filtered = df_grouped[df_grouped['exercise'] == exercise_type]

    # 막대그래프
    axs[i].bar(df_filtered['Date'], df_filtered['Total Chin Up Count'], label=exercise_type, alpha=0.7)

    # 그래프 세부 설정
    axs[i].set_title(f'{exercise_type} Counts by Date')
    axs[i].set_ylabel('Count')
    axs[i].grid(True)

# x축 설정
axs[-1].xaxis.set_major_formatter(DateFormatter('%m-%d'))
axs[-1].xaxis.set_major_locator(DayLocator(interval=1))
plt.xlabel('Date')

plt.tight_layout()
plt.show()
