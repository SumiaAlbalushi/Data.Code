def max_game(N):
    time_per_game=20
    hours=N
    minutes = hours * 60
    max_game = minutes / time_per_game
    return max_game
test_case = [1,10,7,3]
for N in test_case:
    result = max_game(N)
    print(f"cheaf has {N} hours to play {result} games")