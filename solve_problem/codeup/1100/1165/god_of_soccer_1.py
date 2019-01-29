
game_time, score = input().split()
game_time = int(game_time)
score = int(score)

if(game_time % 10 == 0):
    final_score = score + int((90 - game_time) / 5)
else:
    final_score = score + int((90 - game_time) / 5) + 1

print(final_score)
