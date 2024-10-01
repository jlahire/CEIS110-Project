###### This whole project has been pretty fun. I've had to 
###### look up a lot of it and theres a ton of copy&paste here.


# These are imports that I've never used before
import subprocess
import sys
import platform

# GUI imports
import tkinter as tk
from tkinter import messagebox

# Game import
from random import randint

# Audio import
from gtts import gTTS
import pygame
import os

# Another import I'm not familiar with but it 
# was part of the overstack article for interacting
# with the host device. Not really sure why its here.
import pkg_resources


# All of this is copy and paste from overstack
def install_package(package):
    """Install a Python package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_on_windows():
    """Install packages on Windows."""
    try:
        import pip
        install_package("pygame")
        install_package("gTTS")
        print("Packages installed successfully on Windows.")
    except ImportError:
        print("Pip is not installed. Please install pip and run the script again.")

def install_on_mac():
    """Install packages on macOS."""
    try:
        import pip
        install_package("pygame")
        install_package("gTTS")
        print("Packages installed successfully on macOS.")
    except ImportError:
        print("Pip is not installed. Please install pip and run the script again.")

def install_on_linux():
    """Install packages on Linux."""
    try:
        import pip
        install_package("pygame")
        install_package("gTTS")
        print("Packages installed successfully on Linux.")
    except ImportError:
        print("Pip is not installed. Please install pip and run the script again.")

def check_and_install_packages():
    """Check OS and install required packages."""
    os_type = platform.system().lower()
    if os_type == 'windows':
        install_on_windows()
    elif os_type == 'darwin':
        install_on_mac()
    elif os_type == 'linux':
        install_on_linux()
    else:
        print("Unsupported operating system.")
        sys.exit(1)


# Audio stuff
pygame.mixer.init()

language = 'en'
audio_files = {
    "title": "title.mp3",
    "instructions": "instructions.mp3",
    "prompt_guess": "prompt_guess.mp3",
    "prompt_success": "prompt_success.mp3",
    "prompt_low": "prompt_low.mp3",
    "prompt_high": "prompt_high.mp3",
    "prompt_end": "prompt_end.mp3"
}

## I have a little experience with object based programming but most of the 
## code came from geeksforgeeks and I just editing it to match my variables.
def create_audio_file(text, filename):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)

# Create audio
for key, file in audio_files.items():
    if not os.path.exists(file):
        create_audio_file({
            "title": "Guess The Number!",
            "instructions": "A random number between 1 and 21 has been selected.",
            "prompt_guess": "Make a Guess",
            "prompt_success": "You guessed right!",
            "prompt_low": "Close! But your guess is too low! Guess again!",
            "prompt_high": "Close! But your guess is too high! Try again!",
            "prompt_end": "It took you {} times to guess right!"
        }[key], file)

# Play audio
def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# GUI
## I've used tkinter for other projects so this was half from memory 
## and half from having to visit the tkinter page for instructions.
class GuessNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        
        self.random_number = randint(1, 21)
        self.count = 0
        
        self.title_label = tk.Label(root, text="Guess The Number!", font=("Arial", 16))
        self.title_label.pack(pady=10)
        
        self.instruction_label = tk.Label(root, text="A random number between 1 and 21 has been selected.", font=("Arial", 12))
        self.instruction_label.pack(pady=5)
        
        self.guess_label = tk.Label(root, text="Make a Guess:", font=("Arial", 12))
        self.guess_label.pack(pady=5)
        
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack(pady=5)
        
        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)
        
        self.play_audio(audio_files["title"])
        self.play_audio(audio_files["instructions"])
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def play_audio(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        
        self.count += 1
        
        if guess == self.random_number:
            self.play_audio(audio_files["prompt_success"])
            messagebox.showinfo("Success", f"You guessed right! It took you {self.count} tries.")
            self.reset_game()
        elif guess < self.random_number:
            self.play_audio(audio_files["prompt_low"])
            messagebox.showinfo("Try Again", "Close! But your guess is too low! Guess again!")
        else:
            self.play_audio(audio_files["prompt_high"])
            messagebox.showinfo("Try Again", "Close! But your guess is too high! Try again!")

    def reset_game(self):
        self.random_number = randint(1, 21)
        self.count = 0
        self.guess_entry.delete(0, tk.END)

    def cleanup(self):
        for file in audio_files.values():
            if os.path.exists(file):
                os.remove(file)

    def on_closing(self):
        self.cleanup()  # Delete Audio
        self.root.destroy()  # Close

# Main stuff
if __name__ == "__main__":
    check_and_install_packages()
    root = tk.Tk()
    app = GuessNumberApp(root)
    root.mainloop()
