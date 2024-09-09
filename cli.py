import sqlite3
import os
conn = sqlite3.connect('data.db')



def create_table():
    sql = """   
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY,
            username TEXT,
            score INTEGER,
            games_played INTEGER
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

def add_score(username, score):
    """Adds username and score to the db"""
    sql = """
        INSERT INTO player (username, score)
        VALUES (?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, [username, score])
    conn.commit()

add_score('bob', 4)

class Game:
    def start(self):
        print("Game has started!")

class Stats:
    def view(self):
        print("Displaying stats...")

story = {
    'start': {
        'text': 'You wake up in your Manhattan apartment. Your alarm is blaring at 6:30 AM. Do you:',
        'choices': {
            'A': ('Hit snooze and sleep in', 'snooze'),
            'B': ('Get up right away and start the day', 'morning_routine'),
        }
    },
    'snooze': {
        'text': "You hit snooze and oversleep. You're now late for work.",
        'choices': {
            'A': ('Take the subway and hope for the best', 'subway_chaos'),
            'B': ('Walk to work", "street_hazards'),
        }
    },
    'morning_routine': {
        'text': "You wake up on time, feeling slightly groggy but ready for the day .  Do You:",
        'choices': {
            'A': ('Take the subway to work', 'subway_chaos'),
            'B': ('Call a rideshare', 'rideshare_madness'),
            'C': ('Walk to work', 'street_hazards')
        }
    },
    'subway_chaos': {
        'text': "You enter the subway. It's packed, and tensions are high. A fight breaks out. Do you:",
        'choices': {
            'A': ('Try to stop the fight', 'death_subway_fight'),
            'B': ('Move to another car', 'rat_encounter'),
            'C': ('Ignore it and listen to music', 'death_electrocution')
        }
    },
    'rat_encounter': {
        'text': "You move to another car and find yourself face-to-face with a rat. Do you:",
        'choices': {
            'A': ('Kick the rat', 'death_rat_bite'),
            'B': ('Try to catch rat', 'hospital_escape'),
            'C': ('Ignore the rat', 'subway_survive')
        }
    },
    'street_hazards': {
        'text': "You decide to walk to work. Midway, you encounter a street performer juggling flaming swords. Do you:",
        'choices': {
            'A': ('Confront the performer', 'death_street_performer_sword'),
            'B': ('Try to walk around him', 'death_sewer_fall'),
            'C': ('Watch the performance', 'performer_survival')
        }
    },
    'rideshare_madness': {
        'text': "You call a rideshare. The driver is blasting music and speeding recklessly. Do you:",
        'choices': {
            'A': ('Tell the driver to slow down', 'death_rideshare_crash'),
            'B': ('Sit quietly and hope for the best', 'rideshare_survive')
        }
    },
    'workplace_dilemma': {
        'text': "You finally make it to your offic, but your boss is standing at the entrance looking furious. You're laste for an important meeting. Do you:",
        'choices': {
            'A': ('Make up an excuse', 'death_fired_by_boss'),
            'B': ('Apologize sincerely', 'office_drama'),
            'C': ('Sneak past and pretend nothing happened', 'death_fired_sneak')
        }
    },
    'office_drama': {
        'text': "You overhear a coworker gossiping about you. They say you're on the verge of being fired. Do you:",
        'choices': {
            'A': ('Confront them', 'death_office_fight'),
            'B': ('Ignore it and focus on work', 'survive_the_day')
        }
    },
    'unemployment_blues': {
        'text': "After being fired, you're walkling to the unemployment office. You pass a street vendor selling suspiciously cheap hot dogs. Do you:",
        'choices': {
            'A': ('Eat the hot dog', 'death_food_poisoning'),
            'B': ('Ignore it and keep walking', 'survive_unemployment')
        }
    },
    'death_subway_fight': {
        'text': "You try to break up the fight but get caught in the crossfire. A guy with a rusty needle stabs you. You die from blood poisoning.",
        'choices': {}
    },
    'death_electrocution': {
        'text': "While ignoring the fight, you get your headphones caught on a subway pole. A rat bites through the wires, electrocuting you. You are dead.",
        'choices': {}
    },
    'death_rat_bite': {
        'text': "You kick the rat, but it bites your foot, transmitting a deadly disease. You die shortly after.",
        'choices': {}
    },
    'death_street_performer_sword': {
        'text': "You confront the street performer, but he throws a flaming sword at you. You get impaled and die instantly.",
        'choices': {}
    },
    'death_sewer_fall': {
        'text': "While trying to avoid the street performer, you accidentally step into an open sewer grate. You fall to your doom.",
        'choices': {}
    },
    'death_rideshare_crash': {
        'text': "You tell the driver to slow down, but he gets offended and speeds up. The car crashes, and you die in the wreckage.",
        'choices': {}
    },
    'death_fired_by_boss': {
        'text': "Your boss doesn't believe your excuse and fires you on the spot. You're escorted out of the building, trip over a sidewalk crack, and get hit by a cyclist. You die.",
        'choices': {}
    },
    'death_fired_sneak': {
        'text': "You sneak past your boss, but he sees you later and fires you via email. You leave the office, get hit by a taxi, and die.",
        'choices': {}
    },
    'death_office_fight': {
        'text': "You confront your coworker, but the argument gets heated. Your boss walks in and fires both of you. You slip on a spilled coffee cup, hit your head, and die.",
        'choices': {}
    },
    'death_food_poisoning': {
        'text': "You eat the suspicious hot dog. It tastes awful. Within minutes, you collapse from food poisoning and die.",
        'choices': {}
    },
    'subway_survive': {
        'text': "You manage to avoid the chaos, and the rat scurries away. You reach work a bit shaken but alive.",
        'choices': {'Next': ("Go to Workplace Dilemma", 'workplace_dilemma')}
    },
    'hospital_escape': {
        'text': "You try to catch the rat, but you trip and knock yourself unconscious. You wake up in the hospital but survive the day.",
        'choices': {'Next': ("Go to Workplace Dilemma", 'workplace_dilemma')}
    },
    'performer_survival': {
        'text': "You decide to watch the street performance. The performer grabs you for his act, but you narrowly avoid being run over by a car that jumps the curb. You survive and make it to work!",
        'choices': {'Next': ("Go to Workplace Dilemma", 'workplace_dilemma')}
    },
    'rideshare_survive': {
        'text': "You sit quietly while the driver speeds through the streets. You narrowly avoid a crash and arrive at work, alive but late.",
        'choices': {'Next': ("Go to Workplace Dilemma", 'workplace_dilemma')}
    },
    'survive_the_day': {
        'text': "You wisely ignore the office gossip and make it through the day unscathed. You survive and head home.",
        'choices': {}
    },
    'survive_unemployment': {
        'text': "You avoid the hot dog and continue to the unemployment office. Not glamourous, but at least you're alive. You survive the day.",
        'choices': {}
    },
    'loser': {
        'text': "Oh no! Sadly, you met a tragic end. Would you like to play again? (Y/N)",
        'choices': {
            'Y': ('Yes', 'start'),
            'N': ('No', 'quit')
        }
    },
    'winner': {
        'text': "Congratulations! You survived. Would you like to play again? (Y/N)",
        'choices': {
            'Y': ('Yes', 'start'),
            'N': ('No', 'quit')
        }
    },
    'quit': {
        'text': "Thanks for playing. Goodbye.",
        'choices': {}
    }
}


def main_menu():
    create_table()
    game = Game()
    stats = Stats()
    
    print(""" 
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
        """)
    print("                                1. Start Your Journey")
    print("                                2. View Stats")
    print("                                3. Quit")
    print(" ")

    while True:
        choice = input("                                Enter your choice >>> ")

        if choice == '1':
            game.start()
        elif choice == '2':
            stats.view()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()



