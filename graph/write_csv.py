"""
운동 모드 입력받아서 csv 파일에 기록
( 시간 초도 기록 받아야 하는데 그건 원래 버전에 있어서 사용 xx)
"""
import cv2
import mediapipe as mp
import datetime
import time
import csv
import pandas as pd

# Mediapipe를 사용하여 포즈 추적을 위한 초기화
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    model_complexity=2
)

# 웹캠 연결
cap = cv2.VideoCapture(0)

# 총 카운트 및 운동 중 여부 변수 초기화
total_chin_up_count = 0

is_chin_up = False

current_exercise = "pull up"    # 인터페이스에서 입력 받기

# CSV 파일 경로
csv_file_path = "exercise_record.csv"

# CSV 파일이 없으면 생성하고 헤더 작성
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Current Exercise' ,'Total Chin Up Count' ])
    df = pd.DataFrame(columns=['Date','Current Exercise' ,'Total Chin Up Count' ])

# 시작 시간 및 운동 기간 설정
start_time = time.time()
exercise_duration = 60  # 인터 페이스에서 입력 받은 카운트

while True:
    ret, img = cap.read()
    if not ret:
        break

    img_h, img_w, _ = img.shape

    img_result = img.copy()

    # Mediapipe를 사용하여 포즈 추적
    results = pose.process(img)

    if results.pose_landmarks:
        # 이전 코드 부분
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]

        if left_shoulder.y < left_elbow.y and right_shoulder.y < right_elbow.y:
            if not is_chin_up:
                is_chin_up = True
                total_chin_up_count += 1

        else:
            is_chin_up = False


        mp_drawing.draw_landmarks(
            img_result,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )
        # 여기까지 이전 코드 부분

    # 화면에 총 카운트 표시
    cv2.putText(img_result, f"Total Chin Up Count: {total_chin_up_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)


    cv2.imshow('Chin Up & ', img_result)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) == ord('q'):
        break

    elapsed_time = int(time.time() - start_time)
    # 1분이 지나면
    if elapsed_time >= exercise_duration:
        # 종료 전에 총 카운트 및 현재 하는 운동을 CSV 파일에 저장
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, current_exercise, total_chin_up_count])
        break

# 웹캠 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
