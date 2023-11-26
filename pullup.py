class Pullup:
    def __init__(self):
        return
    """
        턱걸이 카운트 함수
        손목(16)이 어깨(12)보다 아래로 내려가면 카운트
        어깨(12)보다 팔꿈치(14)가 올라 가야 true 상태로 돌아감
        """

    def countUp(self, count, status, pose_landmarks):

        if pose_landmarks.landmark[12].y < pose_landmarks.landmark[16].y and status:
            count += 1
            status = False
        elif pose_landmarks.landmark[12].y > pose_landmarks.landmark[16].y and not (status):
            status = True
        return count, status