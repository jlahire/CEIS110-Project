# Import Libraries
from random import randint
from gtts import gTTS
import pygame
import os

# Start
rN = randint(1, 21)
count = 0

# Audio stuff
language = 'en'
title = "Guess The Number!"
instructions = "A random number between 1 and 21 has been selected."
prompt_guess = "Make a Guess"
prompt_success = "You guessed right!"
prompt_low = "Close! But your guess is too low! Guess again!"
prompt_high = "Close! But your guess is too high! Try again!"

# Create audio
def create_audio_file(text, filename):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)

create_audio_file(title, "title.mp3")
create_audio_file(instructions, "instructions.mp3")
create_audio_file(prompt_guess, "prompt_guess.mp3")
create_audio_file(prompt_success, "prompt_success.mp3")
create_audio_file(prompt_low, "prompt_low.mp3")
create_audio_file(prompt_high, "prompt_high.mp3")

pygame.mixer.init()

# More audio stuff
def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


play_audio("title.mp3")
print(title)
play_audio("instructions.mp3")
print(instructions)

# Game
while True:
    play_audio("prompt_guess.mp3")
    try:
        guess = int(input("Make a Guess >> "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    count += 1

    if guess == rN:
        play_audio("prompt_success.mp3")
        print("You guessed right!")
        break
    elif guess < rN:
        play_audio("prompt_low.mp3")
        print("Close! But your guess is too low! Guess again!")
    elif guess > rN:
        play_audio("prompt_high.mp3")
        print("Close! But your guess is too high! Try again!")

# End
end_message = f"It took you {count} times to guess right!"
create_audio_file(end_message, "prompt_end.mp3")
play_audio("prompt_end.mp3")
print(end_message)

# Delete audio
for file in ["title.mp3", "instructions.mp3", "prompt_guess.mp3", "prompt_success.mp3",
             "prompt_low.mp3", "prompt_high.mp3", "prompt_end.mp3"]:
    os.remove(file)
