# Diamond Hernandez
# 05-11-2026
# Final Project
# Ankylosaurus leaf-gathering survival game

"""
🦕 ANKYLOSAURUS LEAF GATHERER 🍃
A text-based adventure where your ankylosaurus explores the forest
and collects leaves to fill its 10-slot inventory.
"""
 
import random
import time
 
# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
LEAF_TYPES = [
    "Fern Frond",
    "Cycad Leaf",
    "Ginkgo Leaf",
    "Horsetail Sprig",
    "Magnolia Leaf",
    "Conifer Needle Bundle",
    "Palmetto Leaf",
    "Broad Swamp Leaf",
]
 
AREAS = ["Dense Forest", "Sunny Clearing", "Swamp Edge", "Rocky Slope", "River Bank"]
 
MAX_SLOTS = 10
HUNGER_PER_TURN = 1
ENERGY_PER_TURN = 1
EAT_RESTORE = 4
REST_RESTORE = 4
MOVE_ENERGY_COST = 1
 
# ─────────────────────────────────────────────
#  SETUP FUNCTIONS
# ─────────────────────────────────────────────
 
def create_ankylosaurus(name: str) -> dict:
    """Create and return the player's ankylosaurus as a dictionary."""
    return {
        "name": name,
        "health": 10,
        "hunger": 0,          # 0 = full, 10 = starving
        "energy": 10,        # 0 = exhausted, 10 = fully rested
        "location": "Dense Forest",
        "turns_survived": 0,
        "leaves_ever_collected": 0,
        "status": "healthy",  # healthy | hungry | exhausted | critical
    }
 
 
def create_inventory() -> dict:
    """Create and return an empty 10-slot inventory dictionary."""
    return {i: None for i in range(1, MAX_SLOTS + 1)}
 
 
# ─────────────────────────────────────────────
#  DISPLAY FUNCTIONS
# ─────────────────────────────────────────────
 
def display_status(anky: dict, inventory: dict) -> None:
    """Print the ankylosaurus's current stats and inventory."""
    print("\n" + "═" * 50)
    print(f"  🦕  {anky['name'].upper()}  |  Turn {anky['turns_survived']}")
    print("═" * 50)
    print(f"  ❤️  Health  : {anky['health']:>3}/10   [{_bar(anky['health'])}]")
    print(f"  🍖 Hunger  : {anky['hunger']:>3}/10   [{_bar(anky['hunger'], invert=True)}]")
    print(f"  ⚡ Energy  : {anky['energy']:>3}/10   [{_bar(anky['energy'])}]")
    print(f"  📍 Location: {anky['location']}")
    print(f"  🏷️  Status  : {anky['status'].upper()}")
    print()
    display_inventory(inventory)
    print("═" * 50)
 
 
def _bar(value: int, invert: bool = False, width: int = 10) -> str:
    """Return a simple ASCII progress bar."""
    filled = round((value / 10) * width)
    if invert:
        filled = width - filled
    return "█" * filled + "░" * (width - filled)
 
 
def display_inventory(inventory: dict) -> None:
    """Print all 10 inventory slots."""
    filled = sum(1 for v in inventory.values() if v is not None)
    print(f"  🎒 Inventory [{filled}/{MAX_SLOTS} slots filled]")
    for slot, item in inventory.items():
        content = item if item else "— empty —"
        print(f"     Slot {slot:>2}: {content}")
 
 
# ─────────────────────────────────────────────
#  INVENTORY FUNCTIONS
# ─────────────────────────────────────────────
 
def inventory_full(inventory: dict) -> bool:
    """Return True if every slot is occupied."""
    return all(v is not None for v in inventory.values())
 
 
def inventory_empty(inventory: dict) -> bool:
    """Return True if every slot is empty."""
    return all(v is None for v in inventory.values())
 
 
def add_to_inventory(inventory: dict, item: str) -> bool:
    """Add an item to the first empty slot. Returns True on success."""
    for slot in inventory:
        if inventory[slot] is None:
            inventory[slot] = item
            return True
    return False
 
 
def eat_from_inventory(inventory: dict) -> str | None:
    """Remove and return the first leaf found in inventory (to eat)."""
    for slot in inventory:
        if inventory[slot] is not None:
            item = inventory[slot]
            inventory[slot] = None
            return item
    return None
 
 
# ─────────────────────────────────────────────
#  ACTION FUNCTIONS
# ─────────────────────────────────────────────
 
def forage(anky: dict, inventory: dict) -> None:
    """Attempt to find and collect leaves in the current area."""
    print(f"\n  🌿 {anky['name']} sniffs around the {anky['location']}...")
    time.sleep(0.8)
 
    if inventory_full(inventory):
        print("  ❌ Inventory is full! Eat some leaves or you can't carry more.")
        return
 
    # Chance to find 1–3 leaves, influenced by location
    luck = random.randint(1, 10)
    if luck <= 3:
        print("  😔 Nothing here. The area looks picked clean.")
        return
 
    found_count = random.randint(1, 3)
    print(f"  ✨ Found {found_count} leaf/leaves!")
    time.sleep(0.4)
 
    for _ in range(found_count):
        if inventory_full(inventory):
            print("  🎒 Inventory filled up — couldn't carry the rest!")
            break
        leaf = random.choice(LEAF_TYPES)
        add_to_inventory(inventory, leaf)
        anky["leaves_ever_collected"] += 1
        print(f"     + Added: {leaf}")
        time.sleep(0.2)
 
 
def eat(anky: dict, inventory: dict) -> None:
    """Eat a leaf from inventory to reduce hunger."""
    if inventory_empty(inventory):
        print("\n  ❌ Nothing to eat! Go forage for leaves first.")
        return
 
    item = eat_from_inventory(inventory)
    anky["hunger"] = max(0, anky["hunger"] - EAT_RESTORE)
    print(f"\n  😋 {anky['name']} munches on a {item}. Hunger reduced!")
    time.sleep(0.6)
 
 
def rest(anky: dict) -> None:
    """Rest to restore energy."""
    print(f"\n  😴 {anky['name']} takes a nap under a tree...")
    time.sleep(1.0)
    anky["energy"] = min(10, anky["energy"] + REST_RESTORE)
    anky["health"] = min(10, anky["health"] + REST_RESTORE)
    print(f"  ⚡ Energy restored! (+3)")
    print(f"  ❤️  Health restored! (+3)")
 
 
def move(anky: dict) -> None:
    """Move to a new random area."""
    available = [a for a in AREAS if a != anky["location"]]
    new_area = random.choice(available)
    print(f"\n  🚶 {anky['name']} lumbers toward the {new_area}...")
    time.sleep(0.8)
    anky["location"] = new_area
    anky["energy"] = max(0, anky["energy"] - MOVE_ENERGY_COST)
    print(f"  📍 Arrived at {new_area}!")
 
 
# ─────────────────────────────────────────────
#  TURN MANAGEMENT
# ─────────────────────────────────────────────
 
def update_ankylosaurus(anky: dict) -> None:
    """Update hunger, energy, health, and status at end of each turn."""
    anky["turns_survived"] += 1
    anky["hunger"] = min(10, anky["hunger"] + HUNGER_PER_TURN)
    anky["energy"] = max(0, anky["energy"] - ENERGY_PER_TURN)
 
    # Starvation & exhaustion damage health
    damage = 0
    if anky["hunger"] >= 5:
        damage += 1
    elif anky["energy"] <= 5:
        damage += 1
 
    anky["health"] = max(0, anky["health"] - damage)
 
    # Update status field
    if anky["health"] <= 3 or (anky["hunger"] >= 8 and anky["energy"] <= 2):
        anky["status"] = "critical"
    elif anky["hunger"] >= 7 or anky["energy"] <= 4:
        anky["status"] = "struggling"
    elif anky["hunger"] >= 5:
        anky["status"] = "hungry"
    elif anky["energy"] <= 5:
        anky["status"] = "tired"
    else:
        anky["status"] = "healthy"
 
 
def is_game_over(anky: dict) -> bool:
    """Return True if the ankylosaurus can no longer continue."""
    return anky["health"] <= 0
 
 
def check_win(inventory: dict) -> bool:
    """Return True if all 10 inventory slots are filled."""
    return inventory_full(inventory)
 
 
# ─────────────────────────────────────────────
#  MAIN GAME LOOP
# ─────────────────────────────────────────────
 
def print_intro() -> None:
    print("\n" + "╔" + "═" * 48 + "╗")
    print("║   🦕  ANKYLOSAURUS LEAF GATHERER  🍃        ║")
    print("╠" + "═" * 48 + "╣")
    print("║  Your ankylosaurus must fill all 10         ║")
    print("║  inventory slots with leaves to WIN.        ║")
    print("║                                             ║")
    print("║  But watch out — hunger and exhaustion      ║")
    print("║  will chip away at your health!             ║")
    print("╚" + "═" * 48 + "╝\n")
 
 
def get_menu_choice() -> str:
    """Display the action menu and return the player's validated choice."""
    print("\n  What does your ankylosaurus do?")
    print("  [1] Forage for leaves")
    print("  [2] Eat a leaf from inventory")
    print("  [3] Rest")
    print("  [4] Move to a new area")
    print("  [Q] Quit")
 
    while True:
        choice = input("\n  Enter choice: ").strip().upper()
        if choice in ("1", "2", "3", "4", "Q"):
            return choice
        print("  ⚠️  Invalid choice. Please enter 1–4 or Q.")
 
 
def print_game_over(anky: dict, won: bool) -> None:
    """Display the final game-over or victory screen."""
    print("\n" + "═" * 50)
    if won:
        print(f"  🎉 YOU WIN! {anky['name']} filled the entire leaf inventory!")
    else:
        print(f"  💀 GAME OVER. {anky['name']} collapsed from exhaustion and hunger.")
    print()
    print(f"  📊 Final Stats:")
    print(f"     Turns survived      : {anky['turns_survived']}")
    print(f"     Total leaves found  : {anky['leaves_ever_collected']}")
    print(f"     Final health        : {anky['health']}")
    print(f"     Final hunger        : {anky['hunger']}")
    print(f"     Final energy        : {anky['energy']}")
    print("═" * 50 + "\n")
 
 
def main() -> None:
    print_intro()
 
    name = input("  Enter your ankylosaurus's name: ").strip() or "Anky"
    print(f"\n  Welcome, {name}! Let the foraging begin!\n")
    time.sleep(0.5)
 
    anky = create_ankylosaurus(name)
    inventory = create_inventory()
 
    while True:
        # Check end conditions first
        if is_game_over(anky):
            print_game_over(anky, won=False)
            break
        if check_win(inventory):
            print_game_over(anky, won=True)
            break
 
        
        display_status(anky, inventory)
        choice = get_menu_choice()
 
        if choice == "Q":
            print(f"\n  👋 Goodbye! {anky['name']} wanders back into the forest.\n")
            break
        elif choice == "1":
            forage(anky, inventory)
        elif choice == "2":
            eat(anky, inventory)
        elif choice == "3":
            rest(anky)
        elif choice == "4":
            move(anky)
        
        update_ankylosaurus(anky)
 
        # Random event (10 % chance)
        if random.random() < 0.10:
            event = random.choice([
                ("🌧️  A sudden rainstorm refreshes the forest! Energy +2.", "energy", 2),
                ("🐊 A predator spooked you! Health -2.", "health", -2),
                ("🍄 You found a nutritious mushroom! Hunger -2.", "hunger", -2),
                ("🌟 A warm sun patch boosts your mood! Health +2.", "health", 2),
            ])
            print(f"\n  ⚡ RANDOM EVENT: {event[0]}")
            anky[event[1]] = max(0, min(10, anky[event[1]] + event[2]))
            time.sleep(0.5)
 
 
if __name__ == "__main__":
    main()
