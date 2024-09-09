
import tkinter as tk    
import sqlite3
import pygame 
import os
from tkinter import messagebox 

conn = sqlite3.connect('surviving_nyc.db')

SOUND_FOLDER = '/Users/Marlon/Development/code/surviving_nyc/shade_sound'

def play_button_click_sound(sound_file):
    click_sound_path = os.path.join(SOUND_FOLDER, sound_file)
    pygame.mixer.Sound(click_sound_path).play()

def create_table():
    sql = """   
        CREATE TABLE IF NOT EXISTS citizen (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            health INTEGER NOT NULL
        );
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def delete_table():
    sql = "DROP TABLE IF EXISTS player"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

class Game:
    def start(self):
        print("Game has started!")

class Stats:
    def view(self):
        print("Displaying stats...")


def quit_app(root):
    messagebox.showinfo("Goodbye", "You chose to quit. Goodbye!")
    root.destroy()

def play_sound():
    pygame.mixer.init()
    sound_path = os.path.join(SOUND_FOLDER, '/Users/Marlon/Development/code/surviving_nyc/shade_sound/Survivin_NYC_main_menu.mp3')
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)

def main_menu():
    pygame.mixer.init()
    root = tk.Tk()
    root.title("Surviving NYC")
    root.geometry("900x600")
    root.configure(bg="black")
    create_table()

    play_sound()

    while True:
        prompt = """
        
--------------------------------------------------------------------
--------------------------------------------------------------------
  

  ███████╗██╗   ██╗██████╗ ██╗   ██╗██╗██╗   ██╗██╗███╗   ██╗ ██████╗     
  ██╔════╝██║   ██║██╔══██╗██║   ██║██║██║   ██║██║████╗  ██║██╔════╝     
  ███████╗██║   ██║██████╔╝██║   ██║██║██║   ██║██║██╔██╗ ██║██║  ███╗    
  ╚════██║██║   ██║██╔══██╗╚██╗ ██╔╝██║╚██╗ ██╔╝██║██║╚██╗██║██║   ██║    
  ███████║╚██████╔╝██║  ██║ ╚████╔╝ ██║ ╚████╔╝ ██║██║ ╚████║╚██████╔╝    
  ╚══════╝ ╚═════╝ ╚═╝███╗╝  ██╗██╗ ╚═██╗╚██████╗ ██╗╝  ╚═══╝ ╚═════╝     
                      ████╗  ██║╚██╗ ██╔╝██╔════╝ ██║                      
                      ██╔██╗ ██║ ╚████╔╝ ██║      ██║                      
                      ██║╚██╗██║  ╚██╔╝  ██║      ╚═╝                      
                      ██║ ╚████║   ██║   ╚██████╗ ██╗                      
                      ╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝                      
          __  __                                             
         |. ||. |    .|                                      
         || ||| |    | |                W                    
         |: ||: |    |'|               [ ]         ._____    
         |  ||  |   |  |     .--'|      3   .---"| |.   |'   
     _   |  ||  |-. |  | __  |.  |     /|  _|__  | ||   |__  
  .-'|  _|  ||  | ||   '-  | ||    \|// / |   |' | |    | |' 
  |' | |.|  ||  | ||       '-'    -( )-|  |   |  | |    | |  
__|  '-' '  ''  ' ""       '       J V |  `   -  |_'    ' |__
                             ___  '    /                     
                             \  \/    |                  
--------------------------------------------------------------------
--------------------------------------------------------------------
"""

        label = tk.Label(root, text=prompt, font=("Courier", 10), fg="orange", bg="black")
        label.pack(pady=20)

        button1 = tk.Button(root, text="Start Your Journey", command=lambda: [play_button_click_sound('CGA_sound.mp3'), start_game()])
        button1.pack(pady=10)

        button2 = tk.Button(root, text="View Stats", command=lambda: [play_button_click_sound('CGA_sound_02.mp3'), view_stats()])
        button2.pack(pady=10)

        button3 = tk.Button(root, text="Quit", command=lambda: [play_button_click_sound('gun_shot.mp3'), quit_app(root)]) 
        button3.pack(pady=10)

        root.mainloop()


def start_game():
    game = Game()
    game.start()

def view_stats():
    stats = Stats()
    stats.view()    


if __name__ == '__main__': 
    main_menu()  




