import math

current_time, score_class_1, score_class_2 = input().split()
current_time = int(current_time)
score_class_1 = int(score_class_1)
score_class_2 = int(score_class_2)

additional_points = (90 - current_time) / 5
additional_points = math.ceil(additional_points)
score_class_1 += additional_points

if(score_class_1 > score_class_2):
    print('win')
elif(score_class_1 < score_class_2):
    print('lose')
else:
    print('same')
