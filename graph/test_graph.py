"""
test 모드를 끝낸 후, 10초 간격으로 카운트 그래프, 총 카운트, 목표 카운트 그래프를 출력 및 저장

"""

import os
import datetime
import matplotlib.pyplot as plt
def test_graph(time_intervals_labels, count_list,exercise, count, goal_number):
        save_directory = "graph_pictures/test_graph"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = f"{current_date}_{exercise}_test.png"
        file_path = os.path.join(save_directory, file_name)

        # 시간대별 운동 횟수를 그래프로 나타냅니다.
        bars = plt.bar(time_intervals_labels, count_list, label=f"{exercise}")

        # 각 막대의 맨 위 가운데에 점 찍기
        for bar in bars:
            height = bar.get_height()
            plt.plot(bar.get_x() + bar.get_width() / 2, height, 'ko')

        # 그래프의 점들을 선으로 이어주기
        plt.plot(time_intervals_labels , count_list , marker='o', color='black')

        # 총 카운트를 그래프에 추가합니다.
        plt.bar(["Total Count", "Goal Count"],
                [int(count), int(goal_number)],
                color=['g', 'r'])

        plt.xlabel("Time Intervals / Total / Goal")
        plt.ylabel('Count')
        plt.title(f"{exercise} test")

        plt.yticks(range(0, int(goal_number) + 5, 5))
        plt.legend()

        plt.savefig(file_path)
        plt.show()