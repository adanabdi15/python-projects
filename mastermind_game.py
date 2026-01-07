"""
    CS5001
    Spring 2025
    Project

    Koshin Mohamed
"""

import turtle
import random
import os
from Marble import Marble
from Point import Point

# Constants
colors = ["red", "blue", "green", "yellow", "purple"]
code_length = 4
max_attempts = 10
LEADERBOARD_FILE = "leaderboard.txt"

# --- Game Logic ---

def generate_secret_code():
    return random.sample(colors, code_length)

def compare_codes(secret_code, guess):
    bulls = sum(1 for s, g in zip(secret_code, guess) if s == g)
    cows = sum(min(secret_code.count(color), guess.count(color)) for color in set(secret_code)) - bulls
    return bulls, cows

def draw_board(guess_history, feedback_history, show_secret=False, secret_code=None):
    turtle.clear()

    for attempt, guess in enumerate(guess_history):
        y = 200 - attempt * 50

        # Draw guess marbles
        for i, color in enumerate(guess):
            pos = Point(-200 + i * 50, y)
            Marble(pos, color).draw()

        # Draw feedback pegs in a 2x2 grid (black = bulls, red = cows)
        bulls, cows = feedback_history[attempt]
        feedback_colors = ["black"] * bulls + ["red"] * cows

        for i, color in enumerate(feedback_colors):
            row = i // 2  # 0 or 1
            col = i % 2   # 0 or 1
            fx = 50 + col * 20
            fy = y - row * 20
            Marble(Point(fx, fy), color).draw()

    # Draw the secret code after the game ends
    if show_secret and secret_code:
        y = -100
        for i, color in enumerate(secret_code):
            Marble(Point(-200 + i * 50, y), color).draw()
        turtle.penup()
        turtle.goto(-200, y - 30)
        turtle.color("black")
        turtle.write("Secret Code", font=("Arial", 12, "bold"))

    turtle.update()

# --- Leaderboard Functions ---

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        lines = f.readlines()
        leaderboard = []
        for line in lines:
            score, name = line.strip().split(" : ")
            leaderboard.append((int(score), name))
        return leaderboard

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as f:
        for score, name in leaderboard:
            f.write(f"{score} : {name}\n")

def draw_leaderboard(leaders):
    turtle.penup()
    turtle.goto(200, 250)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color("blue")
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)

    turtle.penup()
    turtle.goto(220, 220)
    turtle.color("blue")
    turtle.write("Leaders:", font=("Arial", 14, "bold"))

    y = 190
    for rank, (score, name) in enumerate(leaders[:10], start=1):
        turtle.goto(220, y)
        turtle.write(f"{rank} : {name}", font=("Arial", 12, "normal"))
        y -= 30

# --- Main Game Loop ---

def play_mastermind():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title("Mastermind")
    turtle.setup(width=800, height=600)
    turtle.tracer(0)

    player_name = turtle.textinput("Welcome to Mastermind!", "Enter your name:")
    if not player_name:
        return
    player_name = player_name.strip()  # Remove spaces just in case

    leaderboard_data = load_leaderboard()
    secret_code = generate_secret_code()
    attempts = 0
    guess_history = []
    feedback_history = []
    won = False

    draw_leaderboard(leaderboard_data)

    while attempts < max_attempts:
        guess_input = turtle.textinput(
            "Mastermind",
            f"Attempt {attempts+1} of {max_attempts}\nAllowed colors: red, blue, green, yellow, purple\nEnter guess (e.g. red blue green purple):"
        )
        if not guess_input:
            break
        guess = guess_input.lower().split()

        if len(guess) != code_length or any(color not in colors for color in guess):
            turtle.textinput("Error", "Invalid guess! Use only red, blue, green, yellow, or purple.\nPress OK to try again.")
            continue

        bulls, cows = compare_codes(secret_code, guess)
        guess_history.append(guess)
        feedback_history.append((bulls, cows))
        draw_board(guess_history, feedback_history, show_secret=False)
        draw_leaderboard(leaderboard_data)

        if bulls == code_length:
            won = True
            break

        attempts += 1

    draw_board(guess_history, feedback_history, show_secret=True, secret_code=secret_code)

    if won:
        turtle.textinput("You Win!", f"Nice job, {player_name}! You cracked the code in {attempts + 1} attempts.\nPress OK to continue.")
        leaderboard_data.append((attempts + 1, player_name))
        leaderboard_data.sort(key=lambda x: x[0])  # Stable sort by attempts
        save_leaderboard(leaderboard_data)
        draw_leaderboard(leaderboard_data)
    else:
        turtle.textinput("Game Over", f"Sorry, {player_name}. The secret code was: {' '.join(secret_code)}\nPress OK to exit.")

    turtle.done()

# --- Start the Game ---
play_mastermind()
