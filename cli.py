



import sqlite3
import os
conn = sqlite3.connect('surviving_nyc.db')



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
    sql = "DROP TABLE IF EXISTS citizen"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

class Game:
    def start(self):
        print("Game has started!")

class Stats:
    def view(self):
        print("Displaying stats...")

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



