 
# The Last Signal

A Python-based, text-console survival adventure set aboard the Astra-9 research station. Players must make decisions, manage limited resources, collect equipment, and survive encounters with an unknown creature.

## 1. Current Features

The current version includes:

- **Story Introduction:** Introduces the Astra-9 research station, the missing crew, failing systems, and the unidentified creature.
- **Five Scenarios:** Players can explore the Medical Bay, Security Checkpoint, Crew Quarters, Engineering Deck, and Ventilation System.
- **Interactive Choices:** Each scenario presents three choices (A, B, or C), with different consequences.
- **Input Validation:** Accepts uppercase and lowercase choices and rejects invalid entries until a valid selection is provided.
- **Player Statistics:** Tracks health, oxygen, power, survival points, and remaining time.
- **Scoring System:** Rewards or penalizes players based on their decisions.
- **Resource Management:** Player decisions affect oxygen, health, power, and available time.
- **Item Collection:** Includes security keycards, ammunition, an energy pistol, an electrical tool, and a power cell.
- **Random Events:** Uses Python's random module to introduce unpredictable outcomes, including dangerous encounters.
- **Game Termination:** Certain dangerous events and outcomes immediately end the program.

## 2. Game Controls

The game uses a simple keyboard-based interface.

| Input | Action |
|---|---|
| A | Select the first available choice |
| B | Select the second available choice |
| C | Select the third available choice |
| Enter | Continue through the introduction and story prompts |

Players should enter A, B, or C when prompted to make a decision. Inputs are automatically converted to uppercase, so lowercase letters are also accepted. Invalid entries will prompt the player to enter a valid choice.

## 3. Running the Program

### Requirements
- Python 3.x
- A Python-compatible terminal or IDE (such as VS Code, IDLE, or PyCharm).

The program uses Python's built-in `random` and `sys` modules, so no external packages are required.

### Instructions
1. Download or clone the project repository.
2. Save the Python source code as `main.py`.
3. Open a terminal in the directory containing the file.
4. Run the following command:

```bash
python main.py
```

5. Follow the introduction and gameplay instructions.
6. Enter A, B, or C when prompted to make decisions.

## 4. Known Limitations

The current version is an early-stage implementation, and several features are still being developed.

- **Incomplete Story:** Only the first five scenarios are currently implemented. Scenarios six through ten are not yet available.
- **Limited Inventory Management:** Items are tracked using Boolean variables rather than a complete inventory system. The player cannot view or manage an inventory through a dedicated menu.
- **Resource Monitoring:** Although oxygen is tracked, the statistics display function does not currently print the oxygen value.
- **Game-State Validation:** Health, oxygen, power, and remaining time are not consistently checked for failure conditions after every decision.
- **Item Requirements:** Some choices reference equipment without consistently preventing the player from selecting them when the required item is unavailable.
- **Random Outcomes:** Certain choices use coin-flip outcomes that can immediately terminate the program.
- **Ending System:** The complete branching ending system has not yet been implemented.
- **Code Structure:** Scenario logic is currently written directly in the main program. Reusable functions and more organized game-state management are planned.

## 5. Planned Development

Future updates will expand the game and improve its functionality.

- **Complete Story Progression:** Implement scenarios six through ten, including the Research Laboratory, Command Center, Creature Encounter, Final Preparation, and Last Decision.
- **Improved Inventory System:** Develop a dedicated inventory system that allows players to collect, inspect, and use equipment.
- **Advanced Resource Management:** Implement consistent oxygen consumption, health monitoring, power management, and time tracking.
- **Conditional Choices:** Make certain decisions available only when the player possesses the required equipment, keycards, or access codes.
- **Improved Random Events:** Expand random encounters and introduce more varied consequences.
- **Creature Interaction:** Develop additional mechanics for avoiding, defending against, or containing the creature.
- **Multiple Endings:** Introduce branching endings based on player decisions, collected items, survival statistics, and completed objectives.
- **Code Optimization:** Organize scenarios into reusable functions to improve readability, reduce repeated code, and simplify future development.
- **Improved User Interface:** Add clearer menus, inventory displays, and more detailed player-statistics updates.

---

**Project Goal:** Develop a beginner-friendly Python adventure game that demonstrates programming fundamentals through interactive storytelling, conditional logic, resource management, random events, and decision-based gameplay.
