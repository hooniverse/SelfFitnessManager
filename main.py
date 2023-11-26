import interface
from training import Training

# interface = interface.Interface() ##인터페이스 객체 생성
#
# user_input = interface.run() ##인터페이스 run함수 -- return으로 리스트
#[training, 종목, set, set당 개수, 쉬는시간] / [test, 종목, 목표시간, 목표개수]
user_input = [0, 0, 1, 1, 2]

if user_input[0] == 0:#training인 경우
    exercise = Training(user_input[1], user_input[2], user_input[3], user_input[4])#(set, set당 개수, 쉬는시간)
else:
    exercise = Test(user_input[1], user_input[2],user_input[3])#(목표시간, 목표개수)


exercise.run() #미디어파이프 실행

interface.end() #운동이 종료되었다는 메세지
