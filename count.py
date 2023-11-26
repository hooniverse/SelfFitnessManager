"""
운동별 카운트 함수 모음
"""

"""
팔굽혀펴기 카운트 함수
팔꿈치(14)가 어깨(12)보다 아래로 내려가면 카운트
어깨(12)보다 팔꿈치(14)가 올라가면 true 상태로 돌아감
"""
def pushup_countup(count, status):
    pose_landmarks = result.pose_landmarks
    if pose_landmarks.landmark[12].y < pose_landmarks.landmark[14].y and status:
        count += 1
        status = False
    elif pose_landmarks.landmark[12].y > pose_landmarks.landmark[14].y and not (status):
        status = True
    return count, status

"""
턱걸이 카운트 함수
손목(16)이 어깨(12)보다 아래로 내려가면 카운트
어깨(12)보다 팔꿈치(14)가 올라 가야 true 상태로 돌아감
"""
def pullup_countup(count, status):
    pose_landmarks = result.pose_landmarks
    if pose_landmarks.landmark[12].y < pose_landmarks.landmark[16].y and status:
        count += 1
        status = False
    elif pose_landmarks.landmark[12].y > pose_landmarks.landmark[16].y and not (status):
        status = True
    return count, status