# 🏆 Treasure Hunt: The Lost Temple of Gold

Course Project: Data Structures and Algorithms (Prelim Project)  
Group: Group 5  

---

📌 Project Overview
Treasure Hunt: The Lost Temple of Gold is an expanded, list-driven console exploration game refactored from a non-list starter codebase. Players navigate 10 randomized dungeon rooms, read clues to choose the correct doors, avoid deadly traps, manage tools, and collect ancient treasures while managing a 4-life health system.

---
⚙️ List Operation

Nested List (`base_locations`) = Stores master records: `[Room Name, Clue, Correct Door, Treasure, Tool Requirement]`.
Inventory List (`collected_treasures`) = Tracks items collected during the expedition and checks win condition (`len >= 6`).
Equipment List (`player_tools`) = Tracks carried tools (`Basic Torch`, `Golden Key`) to unlock gated rooms.
Trap Hazards List (`hazard_traps`) = Stores dynamic damage descriptions selected randomly upon picking wrong doors.
History Log (`expedition_history`) = Records room-by-room outcomes for the end-game summary.
`append()` Method = Dynamically adds treasures to inventory and tools to equipment upon discovery.
`pop()` Method = Removes items from `collected_treasures` when discarded in `manage_backpack()`.
`index()` & `in` Operations = Searches inventory for specific item locations and checks required tools.
`sort()` / `sorted()` = Displays final collected treasures in alphabetical order upon completion.
`len()` Function = Evaluates total collected treasures, active inventory counts, and loop boundaries.
Loop Traversal = Iterates through sorted lists to render end-of-game expedition logs.

---

👥 Group 5 Team Roles & Responsibilities
* Lead Developer / Refactoring Specialist: Redesigned initial repetitive scalar variables into structured Python lists, implemented main game loop, and handled input validation.
* Game Mechanics & Data Designer: Configured the 10-level nested list database, hazard trap randomizer, life potion mechanics, and tool check logic.
* Documentation & Testing Specialist: Conducted edge-case testing, authored `test-cases.md`, and formatted final repository documentation.

---

🎮 Gameplay Features
1. 10 Randomized Levels: Level sequence is shuffled on every new game session using `random.shuffle()`.
2. 4-Life Health System: Visual health meter (`❤️ ❤️ ❤️ ❤️`). Wrong door choices trigger dynamic hazard traps (poison darts, spike pits) costing 1 Life.
3. Life Potions: 15% random drop chance upon entering correct rooms, automatically restoring +1 Life (capped at max 4).
4. Tool Requirement Checks: Some rooms dynamically roll tool requirements (Golden Key, Iron Pickaxe, Sun Crystal) that inspect your inventory before allowing access.
5. Backpack & Equipment Management: Dedicated options to view, search, and drop items dynamically with exit/cancel options.

---

🖼️ Game Screenshots

1. Title Screen
<img width="661" height="325" alt="797772102_1099127385924739_888171309298452949_n" src="https://github.com/user-attachments/assets/42e0dd97-59f0-4baa-9194-f7fd0ed52a1e" />

2. Trap Event
<img width="670" height="358" alt="799262951_1410669751203637_1619897647126659169_n" src="https://github.com/user-attachments/assets/c51505c8-6f89-4edd-844a-b3804699aeb6" />

3. Final Summary
<img width="640" height="607" alt="794327084_2038179117503913_1918899020883806777_n" src="https://github.com/user-attachments/assets/b15e9f95-054e-414d-b960-83b962b36e09" />


