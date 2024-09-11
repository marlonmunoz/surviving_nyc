import sqlite3
import os
import subprocess
import sys
from tabulate import tabulate

######################################################  MAIN MENU PIZAAZZ  ########################################################
SOUND_DIR = "./shade_sound"

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def play_sound(file_path):
    file_path = os.path.join(SOUND_DIR, file_path )
    return subprocess.Popen(["afplay", file_path])

class Menu:
    def __init__(self):
        self.sound_process = None

    def start(self):
        print(color_text("Loading game menu...", 30))
        self.sound_process = play_sound("Survivin_NYC_main_menu.mp3")

    def quit(self):
        if self.sound_process:
            self.sound_process.terminate()
            self.sound_process = None
        print(color_text("Game ending...", 31))

###################################################  DICTIONARY  ##############################################################                    
story = {
    'start': {
        'text': color_text('You wake up in your Manhattan apartment. Your alarm is blaring at 6:30 AM. Do you:', "32"),
        'choices': {
            1: ('Hit snooze and sleep in', 'snooze'),
            2: ('Get up right away and start the day', 'morning_routine'),
        }
    },
    'snooze': {
        'text': color_text("You hit snooze and oversleep. You're now late for work.", "32"),
        'choices': {
            1: ('Take the subway and hope for the best', 'subway_chaos'),
            2: ('Walk to work', 'street_hazards'),
        }
    },
    'morning_routine': {
        'text': color_text("You wake up on time, feeling slightly groggy but ready for the day .  Do You:", "32"),
        'choices': {
            1: ('Take the subway to work', 'subway_chaos'),
            2: ('Call a rideshare', 'rideshare_madness'),
            3: ('Walk to work', 'street_hazards')
        }
    },
    'subway_chaos': {
        'text': color_text("You enter the subway. It's packed, and tensions are high. A fight breaks out. Do you:", "32"),
        'choices': {
            1: ('Try to stop the fight', 'death_subway_fight'),
            2: ('Move to another car', 'rat_encounter'),
            3: ('Ignore it and listen to music', 'death_electrocution')
        }
    },
    'rat_encounter': {
        'text': color_text("You move to another car and find yourself face-to-face with a rat. Do you:", "32"),
        'choices': {
            1: ('Kick the rat', 'death_rat_bite'),
            2: ('Try to catch rat', 'hospital_escape'),
            3: ('Ignore the rat', 'subway_survive')
        }
    },
    'street_hazards': {
        'text': color_text("You decide to walk to work. Midway, you encounter a street performer juggling flaming swords. Do you:", "32"),
        'choices': {
            1: ('Confront the performer', 'death_street_performer_sword'),
            2: ('Try to walk around him', 'death_sewer_fall'),
            3: ('Watch the performance', 'performer_survival')
        }
    },
    'rideshare_madness': {
        'text': color_text("You call a rideshare. The driver is blasting music and speeding recklessly. Do you:", "32"),
        'choices': {
            1: ('Tell the driver to slow down', 'death_rideshare_crash'),
            2: ('Sit quietly and hope for the best', 'rideshare_survive')
        }
    },
    'subway_survive': {
        'text': color_text("You manage to avoid the chaos, and the rat scurries away. You reach work a bit shaken but alive.", "32"),
        'choices': {
            1: ('Go to Workplace Dilemma', 'workplace_dilemma')
        }
    },
    'hospital_escape': {
        'text': color_text("You try to catch the rat, but you trip and knock yourself unconscious. You wake up in the hospital but survive.", "32"),
        'choices': {
            1: ("Go to Workplace Dilemma", 'workplace_dilemma')
        }
    },
    'performer_survival': {
        'text': color_text("You decide to watch the street performance. The performer grabs you for his act, but you narrowly avoid being run over by a car that jumps the curb. You survive and make it to work!", "32"),
        'choices': {
            1: ("Go to Workplace Dilemma", 'workplace_dilemma')
        }
    },
    'rideshare_survive': {
        'text': color_text("You sit quietly while the driver speeds through the streets. You narrowly avoid a crash and arrive at work, alive but late.", "32"),
        'choices': {
            1: ("Go to Workplace Dilemma", 'workplace_dilemma')
        }
    },
    'workplace_dilemma': {
        'text': color_text("You finally make it to your office, but your boss is standing at the entrance looking furious. You're late for an important meeting. Do you:", "32"),
        'choices': {
            1: ('Make up an excuse', 'death_fired_by_boss'),
            2: ('Apologize sincerely', 'office_drama'),
            3: ('Sneak past and pretend nothing happened', 'death_fired_sneak')
        }
    },
    'office_drama': {
        'text': color_text("You overhear a coworker gossiping about you. They say you're on the verge of being fired. Do you:", "32"),
        'choices': {
            1: ('Confront them', 'death_office_fight'),
            2: ('Ignore it and focus on work', 'survive_the_day')
        }
    },
    'unemployment_blues': {
        'text': color_text("After being fired, you're walkling to the unemployment office. You pass a street vendor selling suspiciously cheap hot dogs. Do you:", "32"),
        'choices': {
            1: ('Eat the hot dog', 'death_food_poisoning'),
            2: ('Ignore it and keep walking', 'survive_unemployment')
        }
    },
    'death_subway_fight': {
        'text': color_text("You try to break up the fight but get caught in the crossfire. A guy with a rusty needle stabs you. You die from blood poisoning.", "32"),
        'choices': {}
    },
    'death_electrocution': {
        'text': color_text("While ignoring the fight, you get your headphones caught on a subway pole. A rat bites through the wires, electrocuting you. You are dead.", "32"),
        'choices': {}
    },
    'death_rat_bite': {
        'text': color_text("You kick the rat, but it bites your foot, transmitting a deadly disease. You die shortly after.", "32"),
        'choices': {}
    },
    'death_street_performer_sword': {
        'text': color_text("You confront the street performer, but he throws a flaming sword at you. You get impaled and die instantly.", "32"),
        'choices': {}
    },
    'death_sewer_fall': {
        'text': color_text("While trying to avoid the street performer, you accidentally step into an open sewer grate. You fall to your doom.", "32"),
        'choices': {}
    },
    'death_rideshare_crash': {
        'text': color_text("You tell the driver to slow down, but he gets offended and speeds up. The car crashes, and you die in the wreckage.", "32"),
        'choices': {}
    },
    'death_fired_by_boss': {
        'text': color_text("Your boss doesn't believe your excuse and fires you on the spot. You're escorted out of the building, trip over a sidewalk crack, and get hit by a cyclist. You die.", "32"),
        'choices': {}
    },
    'death_fired_sneak': {
        'text': color_text("You sneak past your boss, but he sees you later and fires you via email. You leave the office, get hit by a taxi, and die.", "32"),
        'choices': {}
    },
    'death_office_fight': {
        'text': color_text("You confront your coworker, but the argument gets heated. Your boss walks in and fires both of you. You slip on a spilled coffee cup, hit your head, and die.", "32"),
        'choices': {}
    },
    'death_food_poisoning': {
        'text': color_text("You eat the suspicious hot dog. It tastes awful. Within minutes, you collapse from food poisoning and die.", "32"),
        'choices': {}
    },
    'survive_the_day': {
        'text': color_text("You wisely ignore the office gossip and make it through the day unscathed. You survive and head home.", "32"),
        'choices': {}
    },
    'survive_unemployment': {
        'text': color_text("You avoid the hot dog and continue to the unemployment office. Not glamourous, but at least you're alive. You survive the day.", "32"),
        'choices': {}
    },
    'loser': {
        'text': color_text("Oh no! Sadly, you met a tragic end.", "32"),
        'choices': {}
    },
    'winner': {
        'text': color_text("Congratulations! You survived.", "32"),
        'choices': {}
    },
    'quit': {
        'text': color_text("Thanks for playing. Goodbye.", "32"),
        'choices': {}
    }
}

#####################################################  DATABASE TABLE STUFF  #####################################################
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

def create_players_table():
    sql = """   
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            username TEXT
        );
    """
    cursor.execute(sql)
    conn.commit()

def create_choices_table():
    sql = """   
        CREATE TABLE IF NOT EXISTS choices (
            id INTEGER PRIMARY KEY,
            player_id INTEGER,
            story_part TEXT,
            choice INTEGER,
            FOREIGN KEY (player_id) REFERENCES players (id)
        );
    """
    cursor.execute(sql)
    conn.commit()


player_stats = {
    'games_played': 0,
    'games_survived': 0
}


def display_choices(choices):
    for key, (choice_text, _) in choices.items():
        print(f"{color_text(key, 34)}: {choice_text}")
    
    while True:
        try:
            choice = int(input("Select an option: ").strip())
            if choice in choices:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def record_choice(player_id, story_part, choice):
    cursor.execute('''
        INSERT INTO choices (player_id, story_part, choice)
        VALUES (?, ?, ?)
    ''', (player_id, story_part, choice))
    conn.commit()


def start_game(menu):

    player_id = cursor.lastrowid  

    current_event = 'start'
    survived = False

    while current_event != 'quit':
        event = story[current_event]
        print(event['text'])
        

        if 'choices' in event and event['choices']:
            choice = display_choices(event['choices'])
            record_choice(player_id, current_event, choice)
            next_event = event['choices'][choice][1]
        else:
             # Handles the scenario where there are no choices >>>
            if current_event == 'loser':
                survived = False
                update_player_stats(survived)
                result = handle_end_game(survived)
                if result == 'quit':
                    return 'quit'
                else:
                    current_event = 'start'
            elif current_event == 'winner':
                survived = True
                update_player_stats(survived)
                result = handle_end_game(survived)
                if result == 'quit':
                    return 'quit'
                else:
                    current_event = 'start'

        if 'death' in next_event:
            print(story[next_event]['text'])
            current_event = next_event
            survived = False
            current_event = 'loser'
        elif 'survive' in next_event:
            if not story[next_event]['choices']:
                current_event = 'winner'
                survived = True
            else:
                current_event = next_event
        elif current_event == 'quit':
            menu.quit()
            return 'quit'
        else:
            current_event = next_event
    
    update_player_stats(survived)
    handle_end_game(survived)


def display_stats():

    if player_stats['games_played'] > 0:
        survival_rate = round((player_stats['games_survived'] / player_stats['games_played']) * 100)
    else:
        survival_rate = 0
    print(f"Your Survival Rate: {survival_rate} %")

    excluded_parts = {'loser', 'winner', 'quit'}
    
    choice_count = {key: {i: 0 for i in range(1, 4)} for key, value in story.items() if value['choices'] and key not in excluded_parts}
    total_count = {key: 0 for key, value in story.items() if value['choices'] and key not in excluded_parts}
    
    cursor.execute('SELECT story_part, choice, COUNT(*) FROM choices WHERE story_part NOT IN (?, ?, ?) GROUP BY story_part, choice', ('loser', 'winner', 'quit'))
    rows = cursor.fetchall()
    
    for story_part, choice, count in rows:
        if story_part in choice_count:
            choice_count[story_part][choice] = count
            total_count[story_part] = total_count.get(story_part, 0) + count

    tabulated_stats = []

    for story_part, counts in choice_count.items():
        total = total_count.get(story_part, 0)
        choice_stats = []
        
        for choice, count in counts.items():
            if total > 0:
                percentage = round((count / total) * 100)
            else:
                percentage = 0
            choice_stats.append(f"{percentage}% of players selected choice {choice}")

        choice_stats_str = "\n".join(choice_stats)
        tabulated_stats.append([story_part, choice_stats_str])
            
    print(tabulate(tabulated_stats, headers=["Scenario", "Choice Stats"], tablefmt="fancy_grid"))
    input(color_text("\nPress Enter to return to the menu...", 34))


def update_player_stats(survived):
    player_stats['games_played'] += 1
    if survived:
        player_stats['games_survived'] += 1


def handle_end_game(survived):
    if survived:
        print(color_text("\nCongratulations! You survived the Big Apple! You are a TRUE New Yorker ;) ", 34))
    else:
        print(color_text("\nSadly, you have met a tragic end in the Big Apple :( You're not cut out for the city life!", 34))
        
    display_stats()
    
    while True:
        input("\nTo return to the main menu, press the Enter key...")
        main_menu()

#######################################################  MAIN MENU   ############################################################
def main_menu():
    create_players_table()
    create_choices_table()
    menu = Menu()
    menu.start()
    
    while True:
        print(color_text(""" 
            --------------------------------------------------------------------
            --------------------------------------------------------------------
            
        
            ███████╗██╗   ██╗██████╗ ██╗   ██╗██╗██╗   ██╗██╗███╗   ██╗ ██████╗     
            ██╔════╝██║   ██║██╔══██╗██║   ██║██║██║   ██║██║████╗  ██║██╔════╝     
            ███████╗██║   ██║██████╔╝██║   ██║██║██║   ██║██║██╔██╗ ██║██║  ███╗    
            ╚════██║██║   ██║██╔══██╗╚██╗ ██╔╝██║╚██╗ ██╔╝██║██║╚██╗██║██║   ██║    
            ███████║╚██████╔╝██║  ██║ ╚████╔╝ ██║ ╚████╔╝ ██║██║ ╚████║╚██████╔╝    
            ╚══════╝ ╚═════╝ ╚═╝███╗╝  ██╗██╗ ╚═██╗╚██████╗██╗═╝  ╚═══╝ ╚═════╝     
                                ████╗  ██║╚██╗ ██╔╝██╔════╝██║                      
                                ██╔██╗ ██║ ╚████╔╝ ██║     ██║                      
                                ██║╚██╗██║  ╚██╔╝  ██║     ╚═╝                      
                                ██║ ╚████║   ██║   ╚██████╗██╗                      
                                ╚═╝  ╚═══╝   ╚═╝    ╚═════╝╚═╝                      


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
            """, 33))
        print(color_text("                                1. Start Your Journey", 32))
        print("                                2. View Stats")
        print(color_text("                                3. Quit", 30))
        print(" ")

        choice = input("                                Enter your choice >>> ").strip()

        if choice == '1':
            if menu.sound_process:
                menu.sound_process.terminate()
            menu.sound_process = play_sound("CGA_sound.mp3")
            username = input("Enter your username: ").strip()
            cursor.execute('''
                INSERT INTO players (username)
                VALUES (?)
            ''', (username,))
            result = start_game(menu)
            if result == 'quit':
                return 'quit'
    
        elif choice == '2':
            display_stats()

        elif choice == '3':
            menu.quit()
            play_sound("GO_sound_03.mp3")
            print("Goodbye!")
            sys.exit()
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == '__main__':
    main_menu()