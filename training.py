import exercise as ex
import cv2
import mediapipe as mp
import pushup

class Training(ex.Exercise):
    def __init__(self, type, set, count_per_set, break_time):
        super().__init__(type)
        self.set = set
        self.count_per_set = count_per_set
        self.break_time = break_time
        if self.type == 0:
            self.exercise_type = pushup.Pushup()

    def run(self):
        count = -1
        status = True
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture(0)

        with mp_pose.Pose(min_detection_confidence=0.5,
                          min_tracking_confidence=0.5) as pose:

            while cap.isOpened():

                success, image = cap.read()

                if not success:
                    continue

                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                result = pose.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                pose_landmarks = result.pose_landmarks

                if pose_landmarks:
                    count, status = self.exercise_type.countUp(count, status, pose_landmarks)
                    mp_drawing.draw_landmarks(
                        image,
                        result.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS)

                cv2.putText(image, text='count : {}'.format(count)
                            , org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1, color=(0, 0, 255), thickness=2)

                cv2.imshow('image', image)

                if cv2.waitKey(1) == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

