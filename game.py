import random


def display_title():
    print("=" * 60)
    print("       TREASURE HUNT: THE LOST TEMPLE OF GOLD       ")
    print("=" * 60)


def display_instructions():
    print("\n--- INSTRUCTIONS ---")
    print("1. Explore 10 ancient locations by choosing door A, B, or C.")
    print("2. Read clues carefully to deduce which door holds the treasure.")
    print("3. Wrong doors trigger dangerous traps that deal 1 Damage (Cost 1 Life).")
    print("4. You start with 4 Lives (❤️ ❤️ ❤️ ❤️ ). Max life capacity is 4.")
    print("5. Finding a treasure room gives a chance to discover a Life Potion (+1 Life instantly).")
    print("6. Some locations require specific tools (Torches, Keys, Pickaxes, Crystals).")
    print("7. Dungeon levels are randomized every time you play.")
    print("8. Collect at least 6 treasures to conquer the temple!\n")


def choose_room(location_data, player_tools, collected_treasures, hazard_traps, current_lives):
    """
    Handles door selection, tool checks, hazard trap resolution, and Life Potion drops.
    location_data format: [Room Name, Clue, Correct Door, Treasure, Tool Needed]
    """
    room_name = location_data[0]
    clue = location_data[1]
    correct = location_data[2]
    treasure = location_data[3]
    required_tool = location_data[4]

    print(f"\n---> Location: {room_name}")
    print(f"Clue: \"{clue}\"")

    # Display inventory status if a lock requires an item
    if required_tool != "None":
        print(f"\n[!] LOCK WARNING: Opening the chest here requires a [{required_tool}].")
        print("--- YOUR CURRENT EQUIPMENT & INVENTORY ---")
        print(f" * Tools Carried: {player_tools}")
        print(f" * Treasures Backpack: {collected_treasures or 'Empty'}")
        
        if required_tool in player_tools:
            print(f" -> [STATUS]: You HAVE the [{required_tool}] ready in your equipment!")
        else:
            print(f" -> [STATUS]: MISSING ITEM! You do NOT have the [{required_tool}] yet.")
        print("-" * 45)

    # Input validation loop
    choice = ""
    while choice not in ["A", "B", "C"]:
        choice = input("Choose door A, B, or C: ").strip().upper()
        if choice not in ["A", "B", "C"]:
            print("Invalid input! Please select A, B, or C.")

    if choice == correct:
        if required_tool != "None" and required_tool not in player_tools:
            print(f"\nYou found the treasure chest, but you lack the [{required_tool}] to unlock it!")
            return None, False  # (Treasure, Found Life Potion)

        print(f"\nSUCCESS! You unlocked the secret path and found: [{treasure}]!")
        
        # FEATURE: Chance to find a Life Potion in correct rooms
        potion_found = False
        if random.random() < 0.15:  # 15% chance to find a Life Potion
            potion_found = True
            print("\n🧪 BONUS DISCOVERY! You found an Ancient Life Potion beside the chest!")
            if current_lives < 4:
                print("🧪 The potion is instantly consumed! +1 Life restored!")
            else:
                print("🧪 The potion is consumed, but your lives are already at MAX capacity (4/4)!")

        return treasure, potion_found
    else:
        # Trigger dynamic trap hazard from list
        trap_triggered = random.choice(hazard_traps)
        print(f"\n💥 TRAP TRIGGERED! Door {choice} was a trap: {trap_triggered}!")
        print("💥 You took 1 Damage and lost 1 Life!")
        return False, False


def view_inventory(inventory, tools):
    """Displays inventory status and handles item searching."""
    print("\n--- INVENTORY & EQUIPMENT ---")
    print(f"Treasures ({len(inventory)}): {inventory or 'None'}")
    print(f"Tools ({len(tools)}): {tools}")

    if inventory:
        # Requirement: Search operation on list
        search_query = input("\nEnter treasure name to search: ").strip().title()
        if search_query in inventory:
            # Requirement: Indexing operation on list
            idx = inventory.index(search_query)
            print(f"-> Found '{search_query}' at backpack index {idx}.")
        else:
            print(f"-> '{search_query}' is not in your inventory.")


def manage_backpack(inventory):
    """Handles item discarding using list pop()."""
    if not inventory:
        print("\nYour backpack is empty. Nothing to drop.")
        return

    print("\n--- BACKPACK ITEMS ---")
    for i, item in enumerate(inventory):
        print(f"{i + 1}. {item}")

    choice = input("Enter item number to drop (or press Enter to cancel): ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(inventory):
            # Requirement: List pop() operation
            removed = inventory.pop(idx)
            print(f"You discarded [{removed}] from your backpack.")
        else:
            print("Invalid selection.")


def sort_inventory_menu(inventory):
    """
    Dedicated Inventory Sorter Feature.
    Uses list.sort() to organize items dynamically.
    """
    if not inventory:
        print("\nYour backpack is empty. Nothing to sort.")
        return

    print("\n--- INVENTORY SORTER ---")
    print("Current Backpack Order:", inventory)
    print("1. Sort Alphabetically (A-Z)")
    print("2. Sort Alphabetically Reverse (Z-A)")
    print("3. Sort by Name Length (Shortest to Longest)")

    choice = input("Choose sorting method (1-3): ").strip()

    if choice == "1":
        # Requirement: sort() operation
        inventory.sort()
        print("\n[SUCCESS] Treasures sorted Alphabetically (A-Z)!")
    elif choice == "2":
        inventory.sort(reverse=True)
        print("\n[SUCCESS] Treasures sorted Reverse Alphabetically (Z-A)!")
    elif choice == "3":
        inventory.sort(key=len)
        print("\n[SUCCESS] Treasures sorted by Name Length!")
    else:
        print("\nInvalid choice. Inventory left unchanged.")

    print("Updated Backpack Order:", inventory)


def play_game():
    display_title()
    explorer = input("Explorer name: ").strip() or "Explorer"
    display_instructions()

    # ----------------------------------------------------
    # MANDATORY LIST DEFINITIONS (Requirement 1 & 2)
    # ----------------------------------------------------
    # List 1: Collected Treasures Inventory
    collected_treasures = []

    # List 2: Equipment Tools
    player_tools = ["Basic Torch"]

    # List 3: Expedition History Log
    expedition_history = []

    # List 4: Random Hazard Traps
    hazard_traps = [
        "Poison Dart Trap fired from the stone wall",
        "Floor crumbled into a Spike Pit",
        "Ancient Fire Breathing Statue activated",
        "Falling Boulder crushed the entryway",
        "Corrosive Acid Cloud filled the room"
    ]

    # List 5 (Nested List): Master list of 10 Levels
    # Format: [Location, Clue, Correct Door, Treasure, Required Tool]
    master_locations = [
        ["Sunken Grotto", "Where light reflects brightest on water", "A", "Golden Key", "None"],
        ["Whispering Crypt", "Listen closely to the middle shadow", "B", "Ruby Serpent", "Basic Torch"],
        ["Forgotten Vault", "The rightmost path shields ancient royalty", "C", "Ancient Crown", "Golden Key"],
        ["Dragon Peak", "High above, only the left ledge holds peril", "A", "Iron Pickaxe", "None"],
        ["Emerald Catacombs", "The middle archway smells of ancient moss", "B", "Emerald Scarab", "None"],
        ["Subterranean Lake", "Choose the rightmost tunnel where water drops sound closest", "C", "Golden Trident", "Iron Pickaxe"],
        ["Obsidian Mine", "Darkness covers the left wall, break through it", "A", "Diamond Gem", "Iron Pickaxe"],
        ["Chamber of Echoes", "The middle pillar vibrates with old magic", "B", "Silver Compass", "None"],
        ["Celestial Shrine", "The right altar points directly to the North Star", "C", "Sun Crystal", "Golden Key"],
        ["Forbidden Core", "The left door burns with ancient dragon fire", "A", "Heart of Gold", "Sun Crystal"]
    ]

    # Feature: Randomize level order for every new play-through
    locations = master_locations.copy()
    random.shuffle(locations)

    lives = 4
    max_lives = 4
    current_round = 0

    # Main gameplay loop across 10 levels
    while lives > 0 and current_round < len(locations):
        print(f"\n==================== LEVEL {current_round + 1} OF 10 ====================")
        print(f"Explorer: {explorer} | Lives: {'❤️ ' * lives} ({lives}/{max_lives})")

        # Indexing nested list
        current_location = locations[current_round]

        print("\nActions:")
        print("1. Explore Location")
        print("2. Check Backpack & Search Items")
        print("3. Drop an Item (pop)")
        print("4. Open Inventory Sorter (sort)")
        action = input("Select an action (1-4): ").strip()

        if action == "1":
            result, potion_found = choose_room(current_location, player_tools, collected_treasures, hazard_traps, lives)

            # Handle Life Potion heal with max cap of 4
            if potion_found:
                lives = min(max_lives, lives + 1)

            if result:
                # List append() operation
                collected_treasures.append(result)
                expedition_history.append(f"Level {current_round + 1} ({current_location[0]}): Found {result}")

                # Automatically add progression tools to equipment
                if any(tool_word in result for tool_word in ["Key", "Torch", "Pickaxe", "Crystal"]):
                    if result not in player_tools:
                        player_tools.append(result)
                        print(f"--> [{result}] added to your equipment tools!")

            elif result is False:
                lives -= 1
                expedition_history.append(f"Level {current_round + 1} ({current_location[0]}): Took Trap Damage")

            current_round += 1

        elif action == "2":
            view_inventory(collected_treasures, player_tools)

        elif action == "3":
            manage_backpack(collected_treasures)

        elif action == "4":
            sort_inventory_menu(collected_treasures)

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

    # ----------------------------------------------------
    # GAME OVER & SUMMARY
    # ----------------------------------------------------
    print("\n" + "=" * 60)
    print("               EXPEDITION SUMMARY              ")
    print("=" * 55)

    if lives <= 0:
        print(f"☠️ GAME OVER! {explorer} ran out of lives and collapsed in the dungeon.")
    elif len(collected_treasures) >= 6:
        print(f"🏆 VICTORY! {explorer} conquered the temple with {len(collected_treasures)}/10 treasures!")
    else:
        print(f"GAME OVER! {explorer}, you collected {len(collected_treasures)}/10 treasures. You needed at least 6 to conquer the temple.")

    # List sort() / sorted() operation
    print("\nTreasures Collected (Alphabetical Order):")
    sorted_items = sorted(collected_treasures)

    # List traversal with loop
    for item in sorted_items:
        print(f" - {item}")

    print("\nExpedition History Log:")
    for log in expedition_history:
        print(f" * {log}")


def main():
    while True:
        play_game()
        play_again = input("\nPlay again with a new randomized dungeon? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nThank you for playing Treasure Hunt!")
            break


if __name__ == "__main__":
    main()