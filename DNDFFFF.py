import random
import os

# Constants
SAVE_FILE = 'game_save.txt'  # Using a text file for saving game state
MAX_PLAYERS = 4

# Character Classes
classes = {
    "Warrior": {
        "health": 150,
        "power": 20,
        "abilities": ["Sword Slash", "Shield Bash", "Battle Roar", "Counter"],
        "effect": "High damage and tank.",
        "level": 1
    },
    "Mage": {
        "health": 80,
        "power": 30,
        "abilities": ["Fireball", "Ice Spike", "Arcane Shield", "Mana Drain"],
        "effect": "Magic damage and control.",
        "level": 1
    },
    "Rogue": {
        "health": 100,
        "power": 25,
        "abilities": ["Backstab", "Smoke Bomb", "Poison Dagger", "Shadow Step"],
        "effect": "Stealth and burst damage.",
        "level": 1
    },
    "Cleric": {
        "health": 120,
        "power": 15,
        "abilities": ["Heal", "Divine Strike", "Holy Shield", "Revive"],
        "effect": "Support and healing.",
        "level": 1
    },
    "Bard": {
        "health": 90,
        "power": 18,
        "abilities": ["Inspire", "Charm", "Song of Rest", "Fool's Gambit"],
        "effect": "Buff/debuff and morale.",
        "level": 1
    },
    "Necromancer": {
        "health": 70,
        "power": 35,
        "abilities": ["Summon Undead", "Life Drain", "Dark Pact", "Shadow Bolt"],
        "effect": "Manipulation of life and death.",
        "level": 1
    },
    "Ranger": {
        "health": 110,
        "power": 22,
        "abilities": ["Arrow Rain", "Trap", "Eagle Eye", "Quick Shot"],
        "effect": "Ranged attacks and crowd control.",
        "level": 1
    },
    "Druid": {
        "health": 90,
        "power": 20,
        "abilities": ["Entangle", "Healing Touch", "Nature's Wrath", "Shape Shift"],
        "effect": "Control over nature and healing.",
        "level": 1
    },
    "Berserker": {
        "health": 160,
        "power": 25,
        "abilities": ["Frenzy", "Rage", "Whirlwind Attack", "Bloodlust"],
        "effect": "High damage at low health.",
        "level": 1
    },
    "Alchemist": {
        "health": 90,
        "power": 18,
        "abilities": ["Transmute", "Potion Brew", "Explosive Flask", "Elixir of Life"],
        "effect": "Crafting and utility.",
        "level": 1
    },
    "Paladin": {
        "health": 140,
        "power": 22,
        "abilities": ["Holy Strike", "Divine Shield", "Smite", "Blessing"],
        "effect": "Tank and support with holy power.",
        "level": 1
    },
    "Warlock": {
        "health": 75,
        "power": 40,
        "abilities": ["Curse", "Shadow Bolt", "Life Tap", "Demonic Pact"],
        "effect": "High damage with curses.",
        "level": 1
    }
}

# Enemies and Bosses
enemies = [
    {"name": "Goblin", "health": 50, "power": 10, "abilities": ["Sneak Attack"], "intelligence": 3},
    {"name": "Skeleton", "health": 60, "power": 12, "abilities": ["Bone Spear"], "intelligence": 5},
    {"name": "Vampire", "health": 80, "power": 15, "abilities": ["Life Drain"], "intelligence": 6},
    {"name": "Demon", "health": 100, "power": 25, "abilities": ["Fireball", "Claw Swipe"], "intelligence": 7},
    {"name": "Wraith", "health": 90, "power": 20, "abilities": ["Soul Drain"], "intelligence": 8},
    {"name": "Shadow Beast", "health": 110, "power": 30, "abilities": ["Shadow Strike", "Fear"], "intelligence": 9},
    {"name": "Werewolf", "health": 120, "power": 28, "abilities": ["Feral Slash", "Howl"], "intelligence": 6},
    {"name": "Giant Spider", "health": 130, "power": 18, "abilities": ["Web Trap", "Bite"], "intelligence": 5},
    {"name": "Dark Knight", "health": 200, "power": 40, "abilities": ["Cursed Blade", "Shadow Slash"], "intelligence": 9},
    {"name": "Fallen Angel", "health": 180, "power": 35, "abilities": ["Divine Strike", "Heavenly Wrath"], "intelligence": 10},
    {"name": "Cultist", "health": 70, "power": 15, "abilities": ["Ritual of Pain"], "intelligence": 8},
    {"name": "Ghost", "health": 90, "power": 18, "abilities": ["Haunt"], "intelligence": 7},
]

bosses = [
    {"name": "Dark Sorcerer", "health": 250, "power": 40, "abilities": ["Shadow Bolt", "Summon Minions", "Cursed Touch"], "intelligence": 10},
    {"name": "Ancient Dragon", "health": 350, "power": 50, "abilities": ["Fire Breath", "Tail Swipe", "Wing Buffet"], "intelligence": 12},
    {"name": "Forgotten King", "health": 300, "power": 45, "abilities": ["Royal Decree", "Blade Dance", "Summon Spirits"], "intelligence": 11},
    {"name": "Corrupted Druid", "health": 280, "power": 30, "abilities": ["Nature's Fury", "Summon Beasts"], "intelligence": 9},
    {"name": "Lich", "health": 320, "power": 60, "abilities": ["Necrotic Touch", "Summon Undead", "Life Drain"], "intelligence": 12},
]

# Locations and Dialogues
locations = {
    "Dark Forest": [
        "You step into the dense trees, the air thick with mystery.",
        "A chilling wind whispers through the leaves, sending shivers down your spine.",
        "You hear the distant howl of a creature, making your heart race."
    ],
    "Abandoned Castle": [
        "The castle looms before you, its crumbling walls a testament to forgotten glory.",
        "You hear whispers echoing through the halls, beckoning you to enter.",
        "Shadows flit past the windows, as if hiding from your presence."
    ],
    "Haunted Village": [
        "Ghostly figures roam the streets, murmuring tales of sorrow.",
        "An eerie silence blankets the air, interrupted only by distant wails.",
        "A village elder beckons you closer, eyes filled with ancient knowledge."
    ],
    "Cursed Graveyard": [
        "The graves are overgrown, and shadows dance between the tombstones.",
        "A sense of foreboding fills the air as you approach the central crypt.",
        "You can hear the whispers of the dead, warning you to leave."
    ],
    "Mystic Cave": [
        "The cave walls glimmer with strange crystals, illuminating ancient runes.",
        "You can hear the distant sound of water dripping, echoing like a heartbeat.",
        "A faint glow draws you deeper into the cave, where secrets await."
    ],
    "Eldritch Abyss": [
        "The ground trembles as you approach a chasm filled with darkness.",
        "You can feel the weight of despair hanging in the air.",
        "An ancient voice calls from the depths, promising power."
    ],
    "Forgotten Temple": [
        "You find yourself at the entrance of an ancient temple, covered in vines.",
        "The air is thick with magic, and you can sense the presence of old gods.",
        "A guardian spirit warns you of the trials within."
    ],
    "Abandoned Ship": [
        "The ship creaks ominously, water sloshing below deck.",
        "You catch glimpses of shadowy figures darting past the windows.",
        "A treasure map flutters in the wind, leading to unknown fortunes."
    ],
}

# Craftable Items
craftable_items = {
    "Healing Potion": {"ingredients": ["Herb", "Water"], "effect": "Restores 50 health."},
    "Fire Bomb": {"ingredients": ["Sulfur", "Cloth"], "effect": "Deals 30 fire damage to an enemy."},
    "Mana Potion": {"ingredients": ["Mana Herb", "Water"], "effect": "Restores 30 mana."},
    "Strength Elixir": {"ingredients": ["Giant's Heart", "Water"], "effect": "Increases power by 10 for one battle."},
    "Invisibility Cloak": {"ingredients": ["Spider Silk", "Shadow Essence"], "effect": "Grants invisibility for one turn."},
}

# Define Quests
quests = {
    "Retrieve the Amulet": {
        "description": "Find the ancient amulet hidden in the Dark Forest.",
        "reward": "100 gold",
        "completed": False,
        "location": "Dark Forest"
    },
    "Slay the Vampire": {
        "description": "Defeat the Vampire haunting the Abandoned Castle.",
        "reward": "Vampire Fang",
        "completed": False,
        "location": "Abandoned Castle"
    },
}

# NPC Class
class NPC:
    def __init__(self, name, dialogue, quests):
        self.name = name
        self.dialogue = dialogue
        self.quests = quests

    def interact(self):
        print(f"{self.name} says: {self.dialogue}")
        for quest in self.quests:
            if not quests[quest]["completed"]:
                print(f"Quest: {quest} - {quests[quest]['description']}")

# Player Class
class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.health = classes[char_class]["health"]
        self.power = classes[char_class]["power"]
        self.abilities = classes[char_class]["abilities"]
        self.items = []
        self.crafted_items = []
        self.level = classes[char_class]["level"]
        self.experience = 0
        self.active_quests = []

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:  # Level up condition
            self.level += 1
            self.experience = 0
            print(f"{self.name} leveled up to level {self.level}!")

    def accept_quest(self, quest_name):
        if quest_name in quests and not quests[quest_name]["completed"]:
            self.active_quests.append(quest_name)
            print(f"You accepted the quest: {quest_name}")

    def complete_quest(self, quest_name):
        if quest_name in self.active_quests:
            quests[quest_name]["completed"] = True
            self.active_quests.remove(quest_name)
            print(f"You completed the quest: {quest_name} and received {quests[quest_name]['reward']}!")
            self.gain_experience(50)  # Reward experience for completing quests

    def check_inventory(self):
        print("Your inventory:")
        for item in self.items:
            print(f"- {item}")
        print("Crafted Items:")
        for item in self.crafted_items:
            print(f"- {item}")

# Combat Function
def combat(player, enemy):
    print(f"A wild {enemy['name']} appears!")
    while enemy["health"] > 0 and player.health > 0:
        action = input("Do you want to (1) Attack or (2) Use Ability? ")
        if action == "1":
            enemy["health"] -= player.power
            print(f"You dealt {player.power} damage to {enemy['name']}.")
            if enemy["health"] <= 0:
                print(f"You defeated {enemy['name']}!")
                player.gain_experience(30)  # Reward experience for defeating enemies
                return
            player.health -= enemy["power"]
            print(f"{enemy['name']} dealt {enemy['power']} damage to you.")
        elif action == "2":
            ability = input(f"Choose an ability: {', '.join(player.abilities)} ")
            if ability in player.abilities:
                damage = random.randint(15, 35)  # Random damage for abilities
                enemy["health"] -= damage
                print(f"You used {ability} and dealt {damage} damage to {enemy['name']}.")
                if enemy["health"] <= 0:
                    print(f"You defeated {enemy['name']}!")
                    player.gain_experience(30)
                    return
                player.health -= enemy["power"]
                print(f"{enemy['name']} dealt {enemy['power']} damage to you.")
            else:
                print("Invalid ability.")
        print(f"Your health: {player.health}, {enemy['name']}'s health: {enemy['health']}")

    if player.health <= 0:
        print("You have been defeated!")

# Environment Interaction Example
def search_environment():
    found_item = random.choice(["Gold", "Herbs", "Potion Ingredients", None])
    if found_item:
        print(f"You found {found_item}!")
        return found_item
    else:
        print("Nothing found.")

# Explore Function
def explore(player):
    location = random.choice(list(locations.keys()))
    print(f"You explore the {location}.")
    print(random.choice(locations[location]))

    # NPC interaction chance
    if random.random() < 0.2:  # 20% chance to encounter an NPC
        npc = NPC("Old Man", "Have you come to seek wisdom?", ["Retrieve the Amulet"])
        npc.interact()
        action = input("Do you want to accept the quest? (yes/no) ")
        if action.lower() == 'yes':
            player.accept_quest("Retrieve the Amulet")

    if random.random() < 0.3:  # 30% chance to encounter an enemy
        enemy = random.choice(enemies)
        combat(player, enemy)

    # Environment interaction
    if random.random() < 0.5:  # 50% chance to search the environment
        search_environment()

# Craft Item Function
def craft_item(player):
    print("Crafting Menu:")
    for item, details in craftable_items.items():
        print(f"{item}: {details['ingredients']}")
    choice = input("Which item would you like to craft? ").strip()
    if choice in craftable_items:
        required_items = craftable_items[choice]["ingredients"]
        if all(item in player.items for item in required_items):
            player.crafted_items.append(choice)
            for item in required_items:
                player.items.remove(item)
            print(f"You crafted a {choice}!")
            if choice == "Healing Potion":  # Example of additional effects
                player.health += 10  # Bonus effect on crafting
                print("You feel rejuvenated from crafting!")
        else:
            print("You don't have the required items to craft this.")
    else:
        print("Item not found.")

# Save and Load Game Functions
def save_game(player):
    with open(SAVE_FILE, 'w') as f:
        f.write(f"{player.name}\n{player.health}\n{player.power}\n{player.level}\n{player.experience}\n{','.join(player.items)}\n{','.join(player.crafted_items)}\n{','.join(player.active_quests)}")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No save file found.")
        return None
    with open(SAVE_FILE, 'r') as f:
        lines = f.readlines()
        name = lines[0].strip()
        health = int(lines[1].strip())
        power = int(lines[2].strip())
        level = int(lines[3].strip())
        experience = int(lines[4].strip())
        items = lines[5].strip().split(',') if lines[5].strip() else []
        crafted_items = lines[6].strip().split(',') if lines[6].strip() else []
        active_quests = lines[7].strip().split(',') if lines[7].strip() else []
        player = Player(name, "Warrior")  # Default class; could be made more complex
        player.health = health
        player.power = power
        player.level = level
        player.experience = experience
        player.items = items
        player.crafted_items = crafted_items
        player.active_quests = active_quests
        return player

# Main Game Loop
def main():
    print("Welcome to the Game!")
    action = input("Do you want to (1) Start a New Game or (2) Load Game? ")
    if action == "2":
        player = load_game()
        if not player:
            return
    else:
        name = input("Enter your character's name: ")
        char_class = input(f"Choose your class {list(classes.keys())}: ")
        if char_class in classes:
            player = Player(name, char_class)
        else:
            print("Invalid class. Exiting game.")
            return

    while player.health > 0:
        action = input("What would you like to do? (explore, craft, inventory, save, quit): ").strip().lower()
        if action == "explore":
            explore(player)
        elif action == "craft":
            craft_item(player)
        elif action == "inventory":
            player.check_inventory()
        elif action == "save":
            save_game(player)
            print("Game saved.")
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
