shape_value = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

shape_to_lose = {"A": "Z", "B": "X", "C": "Y"}
shape_to_win = {"A": "Y", "B": "Z", "C": "X"}


def calculate_player_score(opponent, result):
    if result == "X":
        return shape_value[shape_to_lose[opponent]]
    if result == "Y":
        return shape_value[chr(ord(opponent) + 23)] + 3
    if result == "Z":
        return shape_value[shape_to_win[opponent]] + 6


with open("input.txt") as f:
    games = f.read().split("\n")

    scores = [
        calculate_player_score(game.split()[0], game.split()[1]) for game in games
    ]

    print(sum(scores))
