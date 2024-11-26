# Surviving NYC!

![Surviving NYC](snyc.png)

### Contributors: Marlon Munoz, Stephen Adler, Sama Durani


## Introduction 
Surviving NYC! is a Python CLI-based 'choose your own adventure' game that simulates a first-person experience navigating through a day in New York City. The game offers a series of interactive choices, where the player’s decisions impact the outcome of their journey on a regular work day. The decisions you make will either lead you home safely or to your final destination. From subway chaos to office dilemmas, every choice has a consequence. Learn if you have what it takes to survive in the Big Apple!

## Goals
- **Capture the Unique NYC Experience**: Inspired by our time at a NYC coding bootcamp, we wanted to bring the city’s chaotic yet vibrant atmosphere to life.
- **Create Relatable, Humorous Scenarios**: Highlight the resilience needed to navigate life’s unpredictable moments, inviting players to turn everyday challenges into lighthearted experiences.
- **Implement Game Design Principles**: Create an engaging narrative that balances challenge and reward, encouraging thoughtful decision-making based on ethical, practical, logical, and emotional factors.

## How to Play
1. Clone this repository.

2. Navigate to the project directory:
   ```sh
   cd surviving-nyc
3. Install the dependencies:
   ```sh
   pipenv install
4. Activate the virtual environment:
   ```sh
   pipenv shell
5. Run the game in the terminal:
   ```sh
   python cli.py

## Features
- **Interactive Main Menu**: Choose from options to start the game, view community statistics, or quit.
- **Game Soundtrack**: Enjoy immersive audio as you carefully make your choices.
- **Multiple Story Paths**: Make decisions at key moments that impact the outcome of the game, leading to survival or hilarious endings.
- **User Data**: Enter your username to track and save each game session.
- **Player Statistics**: Track your progress with in-game stats, including games played and survival rate.
- **Community Statistics**: View which choices are most popular among players.

## Tech Stack and Libraries
- **Python**: Core language for game logic and interaction.
- **SQLite3**: Database used to store player data and behavior, adding persistence across game sessions.
- **SQL**: Querying player data from the relational database for detailed tracking and decision analysis.
- **Subprocess**: Plays sound effects at different stages of the game.
- **Tabulate**: Displays statistics data in an easy-to-read, tabular format.

## Database Schema
- **Players Table**: Stores player usernames with a unique `ID`.
- **Choices Table**: Records each choice made by players during the game, including the related scenario. Uses `player_id` as a foreign key to link each choice back to the respective player.

## Future Goals
- **Multiple Endings**: Implement more branching storylines and additional character choices.
- **Expanded Soundtrack**: Add a wider variety of sound effects and music tracks to enhance the roleplay experience.
- **Leaderboard**: Generate a scoreboard that highlights top five players based on survival rate.
