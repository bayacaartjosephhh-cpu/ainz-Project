import random


def display_title():
    print("=" * 55)
    print("       TREASURE HUNT: THE LOST TEMPLE OF GOLD       ")
    print("=" * 55)


def display_instructions():
    print("\n                 --- INSTRUCTIONS ---")
    print("1. Explore 5 ancient locations by choosing door A, B, or C.")
    print("2. Read clues carefully to deduce which door holds the treasure.")
    print("3. Choosing an empty door costs 1 Energy.")
    print("4. Some locations require specific tools (Torches, Keys).")
    print("5. Levels are randomized every time you restart!")
    print("6. Collect at least 3 treasures to conquer the temple!\n")


def choose_room(location_data, player_tools):
    """
    Handles door selection and room exploration logic.
    location_data format: [Room Name, Clue, Correct Door, Treasure, Tool Needed]
    """
    room_name = location_data[0]
    clue = location_data[1]
    correct = location_data[2]
    treasure = location_data[3]
    required_tool = location_data[4]

    print(f"\n---> Location: {room_name}")
    print(f"Clue: \"{clue}\"")

    if required_tool != "None":
        print(f"Notice: You need a [{required_tool}] to open this chest.")

    # Input validation loop
    choice = ""
    while choice not in ["A", "B", "C"]:
        choice = input("Choose door A, B, or C: ").strip().upper()
        if choice not in ["A", "B", "C"]:
            print("Invalid input! Please select A, B, or C.")

    if choice == correct:
        if required_tool != "None" and required_tool not in player_tools:
            print(f"\nYou found the chest, but you lack the [{required_tool}] to unlock it!")
            return None

        print(f"\nSUCCESS! You unlocked the secret path and found: [{treasure}]!")
        return treasure
    else:
        print(f"\nDoor {choice} was empty! You wasted energy searching.")
        return False


def view_inventory(inventory, tools):
    """Displays inventory status and handles item searching."""
    print("\n--- INVENTORY & EQUIPMENT ---")
    print(f"Treasures ({len(inventory)}): {inventory or 'None'}")
    print(f"Tools ({len(tools)}): {tools}")

    if inventory:
        # Search operation on list
        search_query = input("\nEnter treasure name to search: ").strip().title()
        if search_query in inventory:
            # Indexing operation on list
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
            # List pop() operation
            removed = inventory.pop(idx)
            print(f"You discarded [{removed}] from your backpack.")
        else:
            print("Invalid selection.")


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

    # List 4 (Nested List): Master list of 5 Levels
    # Format: [Location, Clue, Correct Door, Treasure, Required Tool]
    master_locations = [
        ["Sunken Grotto", "Where light reflects brightest on water", "A", "Golden Key", "None"],
        ["Whispering Crypt", "Listen closely to the middle shadow", "B", "Ruby Serpent", "Basic Torch"],
        ["Forgotten Vault", "The rightmost path shields ancient royalty", "C", "Ancient Crown", "Golden Key"],
        ["Chamber of Echoes", "The middle pillar vibrates with old magic", "B", "Silver Compass", "None"],
        ["Celestial Shrine", "High above, the left altar points to the North Star", "A", "Sun Crystal", "None"]
    ]

    # Feature: Randomize level order for every new play-through
    locations = master_locations.copy()
    random.shuffle(locations)

    energy = 3
    current_round = 0

    # Main gameplay loop across 5 levels
    while energy > 0 and current_round < len(locations):
        print(f"\n==================== LEVEL {current_round + 1} OF 5 ====================")
        print(f"Explorer: {explorer} | Energy: {energy}")

        # Indexing nested list
        current_location = locations[current_round]

        print("\nActions:")
        print("1. Explore Location")
        print("2. Check Backpack & Search Items")
        print("3. Drop an Item (pop)")
        action = input("Select an action (1-3): ").strip()

        if action == "1":
            result = choose_room(current_location, player_tools)

            if result:
                # List append() operation
                collected_treasures.append(result)
                expedition_history.append(f"Level {current_round + 1} ({current_location[0]}): Found {result}")

                # Automatically add key progression items to equipment
                if "Key" in result or "Torch" in result:
                    if result not in player_tools:
                        player_tools.append(result)
                        print(f"--> [{result}] added to your equipment tools!")

            elif result is False:
                energy -= 1
                expedition_history.append(f"Level {current_round + 1} ({current_location[0]}): Failed search")

            current_round += 1

        elif action == "2":
            view_inventory(collected_treasures, player_tools)

        elif action == "3":
            manage_backpack(collected_treasures)

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

    # ----------------------------------------------------
    # GAME OVER & SUMMARY
    # ----------------------------------------------------
    print("\n" + "=" * 55)
    print("               EXPEDITION SUMMARY              ")
    print("=" * 55)

    # len() check for win condition (3+ treasures out of 5)
    if len(collected_treasures) >= 3:
        print(f"YOU WIN! {explorer} conquered the temple with {len(collected_treasures)} treasures!")
    else:
        print(f"GAME OVER! {explorer}, you collected {len(collected_treasures)} treasures. The temple remains unconquered.")

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