import random
from game_data import data
from art import logo, vs

print(logo)


def rnd_person():
    rnd = random.choice(data)
    return rnd


def compare(guess, winner, competitor):
    if guess == "a":
        return winner["follower_count"] > competitor["follower_count"]
    else:
        return winner["follower_count"] < competitor["follower_count"]


def game():
    winner = rnd_person()
    competitor = rnd_person()
    score = 0
    game_over = False
    while not game_over:
        print(f"Compare A : {winner['name']}, {winner['description']}, from {winner['country']}")
        print(vs)
        print(f"Compare B : {competitor['name']}, {competitor['description']}, from {competitor['country']}")
        print(winner["follower_count"], competitor["follower_count"])
        print(f"Score : {score}")
        guess = input("Who has more followers?").lower()
        if compare(guess, winner, competitor):
            score += 1
            if guess == "b":
                winner = competitor
            print("정답 입니다 !")
            competitor = rnd_person()
            if competitor == winner:
                competitor = rnd_person()
        else:
            print("틀렸습니다.")
            game_over = True

game()