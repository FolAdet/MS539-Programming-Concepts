# MS539-Programming-Concepts
Grad course at the University of Advancing Technology


# THE LAST SIGNAL 🚀
### A Python Text-Based Space Survival Adventure

## 📖 About the Game

**The Last Signal** is a text-based science fiction survival adventure written in Python. The player wakes up alone aboard the *Astra-9*, an advanced research station orbiting an uncharted planet.

The station is damaged, its crew is missing, emergency power is failing, and an unidentified creature is moving through the ventilation system.

As the commander, your objective is to explore the station, collect resources, investigate the disappearance of the crew, and make decisions that determine whether you survive.

Every decision has consequences. You must manage your health, oxygen, power, and remaining time while navigating the dangers of the station.

## 🎮 Game Objectives

- Explore different areas of the abandoned space station.
- Investigate the disappearance of the crew.
- Collect useful equipment, keycards, weapons, and oxygen supplies.
- Avoid or confront the unidentified creature.
- Manage limited resources and survive dangerous encounters.
- Decide whether to repair the station or escape.

## ⚙️ Gameplay Mechanics

The game uses a decision-based system where players select from three possible choices during each scenario.

Each decision affects the player's statistics and can influence future events and possible endings.

### Player Statistics

| Statistic | Starting Value | Description |
|---|---:|---|
| Health | 100 | Represents the player's physical condition. |
| Oxygen | 100 | Represents the player's remaining breathable air. |
| Power | 50 | Represents available station power resources. |
| Survival Points | 0 | Measures the quality of the player's decisions. |
| Time Remaining | 45 minutes | Represents the remaining survival time. |

### Scoring System

Player decisions are evaluated using a point system:

| Points | Decision Rating | Description |
|---:|---|---|
| +10 | Excellent | Improves survival chances significantly. |
| +5 | Good | Provides a useful advantage. |
| 0 | Neutral | Neither helps nor hurts significantly. |
| -5 | Poor | Creates additional problems. |
| -10 | Dangerous | Puts survival at risk. |

### Oxygen and Time Management

Time advances with every decision, and oxygen decreases as time passes.

| Time Passed | Oxygen Lost |
|---:|---:|
| 1 minute | 2 points |
| 2 minutes | 4 points |
| 3 minutes | 6 points |
| 5 minutes | 10 points |

**Survival Conditions:**
- If health reaches zero, the player dies.
- If oxygen reaches zero, the player dies.
- Certain items can unlock additional opportunities.
- Player decisions influence the final outcome.

## 🧰 Starting Inventory

The player begins with:
- Emergency flashlight
- Damaged communication device
- Basic medical kit (one use)

Additional equipment can be discovered throughout the adventure.

## 🗺️ Story Progression

The adventure is designed around 10 scenarios:

1. **The Medical Bay** – Wake up aboard the Astra-9 and investigate the initial emergency.
2. **The Security Checkpoint** – Find a way through the station's restricted security systems.
3. **The Crew Quarters** – Investigate the missing crew and discover a mysterious recording.
4. **The Engineering Deck** – Investigate the damaged reactor and restore station power.
5. **The Ventilation System** – Encounter evidence of the unidentified creature.
6. **The Research Laboratory** – Discover classified research and investigate the creature's origins.
7. **The Command Center** – Access emergency protocols and determine the station's condition.
8. **The Creature Revealed** – Face the unknown organism and attempt to survive.
9. **The Final Preparation** – Prepare the escape pod or make a final attempt to save the station.
10. **The Last Decision** – Decide the fate of the Astra-9.

## 🏆 Possible Endings

The game is designed to support multiple endings depending on player decisions, resources, and survival points.

- **A New Beginning:** Successfully escape the station.
- **Hero of Astra-9:** Contain the creature and stabilize the station.
- **Lost in Deep Space:** Fail to survive the station's emergency.
- **The Stowaway:** Escape the station, only to discover that the creature may have followed you.

## 💻 Technologies Used

- **Python 3**
- Standard Python libraries and built-in functions
- Console-based user interaction

## 🧠 Python Concepts Practiced

This project provides an opportunity to practice fundamental Python programming concepts, including:

- Variables and data types
- Functions and parameters
- User input and output
- Conditional statements (`if`, `elif`, `else`)
- Arithmetic operations and resource calculations
- String formatting using f-strings
- Decision-based logic
- Game-state management

## ▶️ How to Run

1. Clone or download this repository.
2. Make sure Python 3 is installed.
3. Open the project directory in your terminal or preferred IDE.
4. Run the Python file:

```bash
python main.py
```

5. Follow the console instructions and enter your decisions when prompted.

## 🚧 Future Development

Planned improvements include:

- Implementing all 10 scenarios.
- Developing a complete inventory management system.
- Adding random creature encounters.
- Implementing item collection and item usage.
- Creating a dynamic oxygen and time management system.
- Adding conditional story branches based on previous decisions.
- Developing multiple endings based on player performance.
- Adding a save and load feature.
- Improving the user interface with formatted console messages.

## 🎯 Project Goal

The goal of **The Last Signal** is to create an interactive survival adventure that combines storytelling, resource management, and decision-making while strengthening Python programming skills.

**Every decision matters. Every minute counts. Will you survive the last signal?**
