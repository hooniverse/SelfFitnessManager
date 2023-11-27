import interface
from training import Training

interface = interface.Interface() ##인터페이스 객체 생성
#
user_input = interface.run() ##인터페이스 run함수 -- return으로 리스트
# [training, 종목, set, set당 개수, 쉬는시간] / [test, 종목, 목표시간, 목표개수]
print(user_input)

if user_input['mode'] == 'training':#training인 경우
    exercise = Training(user_input['type'], user_input['set_count'], user_input['reps_per_set'], user_input['break_time'])#(set, set당 개수, 쉬는시간)
elif user_input['mode'] == 'test':
    exercise = Test(user_input['type'], user_input['goal_time'],user_input['goal_number'])#(목표시간, 목표개수)


exercise.run() #미디어파이프 실행

# interface.end() #운동이 종료되었다는 메세지
print("운동 종료")###인터페이스로