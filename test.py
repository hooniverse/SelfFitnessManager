import cv2
import mediapipe as mp
from exercise import pullup, pushup, squat
import method
import time
from graph import write_csv, test_graph

import matplotlib.pyplot as plt
import os
import datetime

class Test:
    def __init__(self, type, goal_time, goal_number):
        self.type = type
        self.goal_time = goal_time
        self.goal_number = goal_number


        if self.type == ['Push-Up']:
            self.exercise_type = pushup.Pushup()
        elif self.type == ['Pull-Up']:
            self.exercise_type = pullup.Pullup()
        elif self.type == ['Squat']:
            self.exercise_type = squat.Squat()

    def run(self):
        count = -1
        status = True
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture(0)
        count_list = [0] * (int(self.goal_time) // 10)
        time_intervals_labels = ["{}~{}".format(i*10+1, i*10+10) for i in range(int(self.goal_time) // 10) ]


        with mp_pose.Pose(min_detection_confidence=0.5,
                          min_tracking_confidence=0.5) as pose:

            start_time = time.time()

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


                elapsed_time = time.time() - start_time
                remaining_time = max(0, int(int(self.goal_time) - elapsed_time))

                cv2.putText(image, text='count : {}/{}   Remaining time : {}'
                            .format(count, self.goal_number, int(remaining_time))
                            , org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1, color=(0, 0, 255), thickness=2)

                cv2.imshow('image', image)

                if cv2.waitKey(1) == ord('q'):
                    break

                if count >= int(self.goal_number) and remaining_time <= 0:
                    write_csv.write_csv(self.exercise_type, count)
                    method.speak('test complete!')
                    break
                elif count >= int(self.goal_number) and not remaining_time <= 0:
                    write_csv.write_csv(self.exercise_type, count)
                    method.speak('test complete!')
                    break
                elif count < int(self.goal_number) and remaining_time <= 0:
                    write_csv.write_csv(self.exercise_type, count)
                    method.speak('test failed!')
                    break
                idx = int(elapsed_time)//10

                ten_second_count = count
                for i in range(idx):
                    ten_second_count-=count_list[i]
                count_list[idx] = ten_second_count

            cap.release()
            cv2.destroyAllWindows()



        test_graph.test_graph(time_intervals_labels, count_list,self.type[0], count, self.goal_number)