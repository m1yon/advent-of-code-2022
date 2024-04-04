shape_value = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def calculate_player_score(player, opponent):
    player_score = 0
    player_score += shape_value[player]

    if player == chr(ord(opponent) + 23):
        return player_score + 3

    if (
        (player == "X" and opponent == "C")
        or (player == "Y" and opponent == "A")
        or (player == "Z" and opponent == "B")
    ):
        return player_score + 6

    return player_score


with open("input.txt") as f:
    games = f.read().split("\n")

    scores = [
        calculate_player_score(game.split()[1], game.split()[0]) for game in games
    ]

    print(sum(scores))
