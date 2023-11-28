import exercise as ex
import cv2
import mediapipe as mp
import pullup
import pushup

class Training(ex.Exercise):
    def __init__(self, type, set, count_per_set, break_time):
        super().__init__(type)
        self.set = set
        self.count_per_set = count_per_set
        self.break_time = break_time
        if self.type == ['Push-Up']:
            self.exercise_type = pushup.Pushup()
        # elif self.type == ['Pull-Up']:
        #     self.exercise_type = pullup.Pullup()

    def run(self):
        count = -1
        status = True
        set_count = 0
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



                if count >= int(self.count_per_set):
                    set_count += 1
                    count = 0
                    if set_count >= int(self.set):
                        self.speak('exercise complete!')  ###음성으로
                        break
                    self.speak('set complete!')  ###음성으로
                    self.time_count(int(self.break_time))




                cv2.putText(image, text='count : {}/{}      set : {}/{}'.format(count, self.count_per_set,
                                                                                set_count, self.set)
                            , org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1, color=(0, 0, 255), thickness=2)

                cv2.imshow('image', image)

                if cv2.waitKey(1) == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

