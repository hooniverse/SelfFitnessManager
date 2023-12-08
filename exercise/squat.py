class Squat:
    def __init__(self):
       return

    def __str__(self):
        return "Squat"


    def countUp(self, count, status, pose_landmarks):
        if pose_landmarks.landmark[24].y < pose_landmarks.landmark[26].y and status:
            count += 1
            status = False
        elif pose_landmarks.landmark[24].y > pose_landmarks.landmark[26].y and not (status):
            status = True
        return count, status