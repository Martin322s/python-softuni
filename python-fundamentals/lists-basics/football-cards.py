cards = input()
cards_list = cards.split(" ")
team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for card in cards_list:
    given_card = card.split("-")
    number = int(given_card[1])

    if given_card[0] == "A" and number in team_A:
        team_A.remove(number)
    elif given_card[0] == "B" and number in team_B:
        team_B.remove(number)

    if len(team_A) < 7 or len(team_B) < 7:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print("Game was terminated")
        exit()

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
