"""
test 모드 시간, 목표 카운트 수 입력받고 테스트 종료 후 10초 구간별 카운트, 총카운트, 목표카운트를
막대그래프로 그려줌
"""
import cv2
import mediapipe as mp
import datetime
import time
import matplotlib.pyplot as plt

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    model_complexity=2
)

cap = cv2.VideoCapture(0)

total_chin_up_count = 0
is_chin_up = False



# 사용자로부터 운동 시간과 목표 개수를 입력 받습니다.
exercise_duration = int(input("Enter the total exercise duration in seconds: "))
goal_chin_up_count = int(input("Enter the goal for Chin Up count: "))

# 10초 간격으로 나뉜 각 시간대별 카운트를 저장할 리스트를 초기화합니다.
time_intervals = exercise_duration // 10
chin_up_counts_by_time = [0] * time_intervals

start_time = time.time()

while True:
    ret, img = cap.read()
    if not ret:
        break

    img_h, img_w, _ = img.shape

    img_result = img.copy()

    results = pose.process(img)

    if results.pose_landmarks:
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]

        if left_shoulder.y < left_elbow.y and right_shoulder.y < right_elbow.y:
            if not is_chin_up:
                is_chin_up = True
                total_chin_up_count += 1
                current_second = int(time.time() - start_time)
                time_index = min(current_second // 10, time_intervals - 1)
                chin_up_counts_by_time[time_index] += 1
        else:
            is_chin_up = False

        mp_drawing.draw_landmarks(
            img_result,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

    cv2.putText(img_result, f"Chin Up Count: {total_chin_up_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    remaining_time = max(0, exercise_duration - int(time.time() - start_time))
    cv2.putText(img_result, f"Remaining Time: {remaining_time} seconds", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow('Chin Up Counter', img_result)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    if int(time.time() - start_time) >= exercise_duration:
        break

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Total Chin Up Count: {total_chin_up_count}")

# 시간대별 운동 횟수를 그래프로 나타냅니다.
time_intervals_labels = [f"{i*10+1}-{(i+1)*10}" for i in range(time_intervals)]
plt.bar(time_intervals_labels, chin_up_counts_by_time, label='Chin Up')

# 목표 개수를 그래프에 추가합니다.
plt.axhline(y=goal_chin_up_count, color='r', linestyle='--', label=f'Goal Chin Up: {goal_chin_up_count}')

# 총 카운트를 그래프에 추가합니다.
plt.bar(["Total Chin Up", "Goal Chin Up"],
        [total_chin_up_count, goal_chin_up_count],
        color=['g', 'r'])

plt.xlabel('Time Intervals / Count Types')
plt.ylabel('Count')
plt.title('Chin Up Counts by Time Intervals')
plt.legend()
plt.show()
